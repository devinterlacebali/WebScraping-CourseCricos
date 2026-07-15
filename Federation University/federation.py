"""
Federation University course scraper (Scrapling, plain HTTP — no browser).

The site was rebuilt as a JS app, but the whole page is still server-rendered into a
`var props = {...}` JSON blob in the HTML. We parse that JSON directly instead of
driving Playwright: every field lives under
`CourseDetailPageStructure.international` (offshore) / `.domestics` (onshore).

Shape (repo standard): read federation.xlsx (title,url[,cricos]) -> scrape each page
-> write federation_courses_update.sql + rewrite the xlsx with the enriched record.
"""
import os
import re
import csv
import sys
import json
import pandas as pd
from bs4 import BeautifulSoup
from scrapling.fetchers import Fetcher

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants -------------------------------------------------------------
PROVIDER_CODE = "00103D"                       # Federation University Australia CRICOS
SLUG = "federation"
DIR = "Federation University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

# CRICOS register export — used to backfill CRICOS + fees for courses whose live
# page had no international tab (or 404'd) but which are still CRICOS-registered.
REGISTER_CSV = "cricos-courses.csv"
APPLY_FALLBACK = "https://federation.edu.au/international/study-at-federation/apply"

# Manual CRICOS overrides for register titles that map to >1 non-expired code
# (keyed by course title). Used to resolve genuine ambiguity the matcher can't.
MANUAL_CRICOS = {
    # Two live registrations share this name; 116xxx is the current generation.
    "Master of Engineering Technology (Renewable Energy and Electrical Power Systems)": "116405D",
}

MONTHS = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October",
    "nov": "November", "dec": "December", "january": "January",
    "february": "February", "march": "March", "april": "April", "june": "June",
    "july": "July", "august": "August", "september": "September",
    "october": "October", "november": "November", "december": "December",
}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- shared helpers --------------------------------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html: str) -> str:
    """Flatten wrapper divs/spans into clean, minimal semantic HTML."""
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img",
                            "svg", "button", "abbr"]):
        t.unwrap() if t.name == "abbr" else t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    for t in frag.find_all("span"):
        t.unwrap()
    # heading tags -> h5 (only h5 is allowed) so section sub-heads survive
    for t in frag.find_all(["h1", "h2", "h3", "h4", "h6"]):
        t.name = "h5"
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "table", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i", "h5"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def months_in(text: str):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", text or ""):
        k = tok.lower()
        if k in MONTHS and MONTHS[k] not in found:
            found.append(MONTHS[k])
    return found

# --- props / block access --------------------------------------------------
def fetch_props(url: str):
    page = Fetcher.get(url, stealthy_headers=True)
    html = str(page.html_content)
    so = html.find("var props =")
    if so < 0:
        return None
    start = html.find("{", so)
    props, _ = json.JSONDecoder().raw_decode(html[start:])
    return props

def get_structure(props):
    for c in props.get("components", []):
        if c.get("name") == "CourseDetailPageStructure":
            return c.get("props", {})
    return None

def first(blocks, name):
    for b in blocks:
        if b.get("name") == name:
            return b.get("props", {})
    return None

def all_of(blocks, name):
    return [b.get("props", {}) for b in blocks if b.get("name") == name]

# --- field extraction ------------------------------------------------------
def extract_years(blocks):
    """Return course length in years (float) from the Credit EFTSL or Duration item."""
    ess = first(blocks, "CourseEssentialsBlock") or {}
    items = {i.get("heading"): (i.get("summary") or "") for i in ess.get("items", [])}
    m = re.search(r"=\s*([\d.]+)\s*<", items.get("Credit", "")) \
        or re.search(r"([\d.]+)\s*EFTSL", re.sub(r"<[^>]+>", " ", items.get("Credit", "")))
    if m:
        return float(m.group(1))
    m = re.search(r"([\d.]+)\s*year", items.get("Duration", ""), re.I)
    if m:
        return float(m.group(1))
    return None

def extract_description(blocks):
    parts = []
    summary = first(blocks, "CourseSummaryBlock") or {}
    if summary.get("outline"):
        parts.append("<h4>Course overview</h4>" + sanitise(summary["outline"]))
    if summary.get("additionalProgramInformation"):
        parts.append("<h4>Additional information</h4>"
                     + sanitise(summary["additionalProgramInformation"]))
    return "".join(parts)

def _accordion_item(blocks, title_kw):
    for acc in all_of(blocks, "AccordionContainerBlock"):
        for it in acc.get("items", []):
            if title_kw.lower() in (it.get("title") or "").lower():
                return it.get("content") or ""
    return ""

def extract_entry_requirements(blocks):
    content = _accordion_item(blocks, "Entry requirements")
    pathways = _accordion_item(blocks, "Alternative pathways")
    out = ""
    if content:
        out += "<h4>Entry Requirements</h4>" + sanitise(content)
    if pathways:
        out += "<h4>Alternative Pathways</h4>" + sanitise(pathways)
    return out

def extract_cricos(blocks):
    content = _accordion_item(blocks, "How to apply")
    if not content:
        return ""
    soup = BeautifulSoup(content, "html.parser")
    for dt in soup.find_all("dt"):
        if "cricos" in dt.get_text().lower():
            dd = dt.find_next_sibling("dd")
            if dd:
                m = re.search(r"[0-9]{5,7}[A-Z]", dd.get_text(strip=True))
                if m:
                    return m.group(0)
    return ""

def extract_fee(blocks):
    """Return (amount, is_annual) from the Fees & scholarships wysiwyg.

    Federation usually quotes an *annual* "indicative full-time fee" (multiply by
    years for the total). Some courses instead quote a "total estimated cost of
    course" figure (already a total — do not multiply).
    """
    for w in all_of(blocks, "WysiwygBlock"):
        content = w.get("content") or ""
        if w.get("anchorId") != "fees" and "fee" not in content.lower():
            continue
        m = re.search(r"indicative full-time fee[:\s]*\$([\d,]+)", content, re.I)
        if m:
            return int(m.group(1).replace(",", "")), True
        m = re.search(r"total estimated cost[^$]*\$([\d,]+)", content, re.I)
        if m:
            return int(m.group(1).replace(",", "")), False
        m = re.search(r"\$([\d,]+)", content)
        if m:
            return int(m.group(1).replace(",", "")), False   # unknown basis: don't scale
    return None, False

def total_fee(blocks, years):
    amount, is_annual = extract_fee(blocks)
    if amount is None:
        return "NULL"
    if is_annual and years:
        # Scale the annual indicative fee up for multi-year courses, but never below
        # it: for sub-year courses (EFTSL < 1) the quoted fee already is the course
        # total (verified against the CRICOS register), so don't discount it.
        return str(int(round(amount * max(1.0, years))))
    return str(amount)

def extract_intake_months(blocks):
    ess = first(blocks, "CourseEssentialsBlock") or {}
    for i in ess.get("items", []):
        if i.get("heading") == "Start dates":
            return months_in(re.sub(r"<[^>]+>", " ", i.get("summary") or ""))
    return []

# --- per course ------------------------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    title = str(row.get("title", "")).strip()

    d = {"cricos": "", "title": title, "url": url, "course_description": "",
         "course_duration_per_week": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL",
         "materials_fee": "NULL", "entry_requirements": "", "apply_form": url,
         "intake_months": [], "note": "", "source": "page"}
    try:
        props = fetch_props(url)
        if not props:
            d["note"] = "no props JSON on page"
            print(f"⚠️  {url}: no props JSON")
            return d
        st = get_structure(props)
        if not st:
            if any(c.get("name") == "ErrorBlock" for c in props.get("components", [])):
                d["note"] = "404 page (course removed or URL changed)"
                print(f"⚠️  {url}: 404 (removed/renamed)")
            else:
                d["note"] = "no CourseDetailPageStructure"
                print(f"⚠️  {url}: no course structure")
            return d

        intl = st.get("international") or []
        dom = st.get("domestics") or []
        stype = first(intl, "StudentTypeBlock") or first(dom, "StudentTypeBlock") or {}
        has_intl = bool(stype.get("hasInternational"))

        primary = intl if (has_intl and intl) else dom   # description/entry/cricos source
        years = extract_years(primary) or extract_years(dom)

        hdr = first(primary, "CourseHeaderBlock") or {}
        d["title"] = hdr.get("heading") or title
        d["cricos"] = extract_cricos(primary) or extract_cricos(dom)
        d["course_description"] = clean_html(extract_description(primary))
        d["entry_requirements"] = clean_html(extract_entry_requirements(primary))
        d["course_duration_per_week"] = str(int(round(years * 52))) if years else ""
        d["intake_months"] = extract_intake_months(primary) or extract_intake_months(dom)

        if has_intl and intl:
            d["offshore_tuition_fee"] = total_fee(intl, years)
        else:
            d["note"] = "no international offering (offshore fee NULL)"
        d["onshore_tuition_fee"] = total_fee(dom, years)

        print(f"✅ {d['title']} → CRICOS {d['cricos'] or '—'} | "
              f"offshore {d['offshore_tuition_fee']} onshore {d['onshore_tuition_fee']} "
              f"| {d['course_duration_per_week'] or '?'}w")
    except Exception as e:
        d["note"] = f"error: {e}"
        print(f"❌ {url}: {e}")
    return d

# --- CRICOS register backfill ----------------------------------------------
def _norm_title(s):
    s = str(s).lower()
    s = re.sub(r"\b(in|of|the|and|a|an|de)\b", " ", s)
    return re.sub(r"[^a-z0-9]", "", s)          # keep parenthetical words, drop punctuation

def load_register():
    """Return (by_title, by_code) for provider 00103D, non-expired register rows.

    by_title: normalised title -> row, keeping only titles that map to exactly one
    CRICOS code (ambiguous names are dropped so we never guess).
    by_code:  CRICOS course code -> row, for resolving MANUAL_CRICOS overrides.
    Both empty if the CSV isn't present.
    """
    if not os.path.exists(REGISTER_CSV):
        return {}, {}
    buckets, by_code = {}, {}
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                continue
            if r["Expired"].strip().lower() == "yes":
                continue
            buckets.setdefault(_norm_title(r["Course Name"]), []).append(r)
            by_code[r["CRICOS Course Code"].strip()] = r
    by_title = {k: rows[0] for k, rows in buckets.items()
                if len({r["CRICOS Course Code"] for r in rows}) == 1}
    return by_title, by_code

def _fee_num(val):
    v = re.sub(r"[^\d.]", "", str(val or ""))
    return str(int(float(v))) if v else "NULL"

def backfill_from_register(results):
    """For rows the page left without a CRICOS, pull code + register fees by exact
    title. The register's 'Tuition Fee' is the whole-course total (already), so no
    per-year scaling. Description/entry stay empty (register has none).

    The driver list contains duplicate slugs for one course (a dead old slug + the
    live one); we never assign a code already owned by a page-scraped row (or an
    earlier register row), so no two UPDATEs ever target the same course."""
    by_title, by_code = load_register()
    manual = {_norm_title(k): v for k, v in MANUAL_CRICOS.items()}
    used = {d["cricos"] for d in results if d["cricos"]}   # codes already taken by pages
    filled = 0

    # 1) fill missing codes from the register (skipping already-used codes)
    for d in results:
        if d["cricos"]:
            continue
        nt = _norm_title(d["title"])
        row = by_code.get(manual[nt]) if nt in manual else by_title.get(nt)
        if not row:
            continue
        code = row["CRICOS Course Code"].strip()
        if code in used:
            d["note"] = (f"register match {code} already used by another row "
                         f"(duplicate slug); left uncoded ({d['note']})").strip()
            print(f"⏭️  duplicate: {d['title'][:50]} → {code} already used; skipped")
            continue
        used.add(code)
        d["cricos"] = code
        d["offshore_tuition_fee"] = _fee_num(row.get("Tuition Fee"))
        d["enrolment_fee"] = _fee_num(row.get("Non Tuition Fee"))
        dur = re.sub(r"[^\d]", "", str(row.get("Duration (Weeks)") or ""))
        if dur:
            d["course_duration_per_week"] = dur
        d["apply_form"] = APPLY_FALLBACK
        d["source"] = "register"
        d["note"] = f"CRICOS + fees from CRICOS register ({d['note']})".strip()
        filled += 1
        print(f"🗂️  register: {d['title'][:55]} → CRICOS {d['cricos']} "
              f"| offshore {d['offshore_tuition_fee']} | {d['course_duration_per_week'] or '?'}w")

    # 2) page rows that have a CRICOS but no offshore fee: fill fee from register
    for d in results:
        if d["source"] != "page" or not d["cricos"]:
            continue
        if d["offshore_tuition_fee"] not in ("NULL", "", None):
            continue
        row = by_code.get(d["cricos"]) or by_title.get(_norm_title(d["title"]))
        if not row or row["CRICOS Course Code"].strip() != d["cricos"]:
            continue
        fee = _fee_num(row.get("Tuition Fee"))
        if fee != "NULL":
            d["offshore_tuition_fee"] = fee
            if d["enrolment_fee"] in ("NULL", "", None):
                d["enrolment_fee"] = _fee_num(row.get("Non Tuition Fee"))
            d["note"] = f"offshore fee from CRICOS register ({d['note']})".strip()
            print(f"💲 fee-fill: {d['title'][:50]} → offshore {fee}")
    return filled

# --- main ------------------------------------------------------------------
def main():
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel not found: {EXCEL_PATH}")
        return
    df = pd.read_excel(EXCEL_PATH)
    results = [scrape_course(r) for _, r in df.iterrows()]

    backfilled = backfill_from_register(results)

    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        emitted = set()
        for d in results:
            if not d["cricos"]:
                reason = (d["note"] or "no CRICOS course code found").replace("\n", " ").replace("\r", "")
                f.write(f"-- ⚠️ Skipped ({reason}): {d['title']} | {d['url']}\n\n")
                continue
            if d["cricos"] in emitted:   # safety net: never repeat a WHERE code
                f.write(f"-- ⚠️ Skipped (CRICOS {d['cricos']} already emitted "
                        f"— duplicate slug): {d['title']} | {d['url']}\n\n")
                continue
            emitted.add(d["cricos"])
            if d["source"] == "register":
                # Register-sourced: we have code + fees + duration but no description/
                # entry — emit a partial UPDATE so existing DB text is not wiped.
                f.write(f"""-- From CRICOS register (page had no international offering): {d['title']}
UPDATE courses SET
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
                continue
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    onshore_tuition_fee = {d["onshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")

    def cell(v):
        v = "" if v in (None, "NULL") else str(v).replace("''", "'")
        return v[:32000]
    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "course_duration_per_week": int(d["course_duration_per_week"]) if str(d["course_duration_per_week"]).isdigit() else "",
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]),
        "materials_fee": cell(d["materials_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
        "source": d["source"],
        "note": d["note"],
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    ok = sum(1 for d in results if d["cricos"])
    print(f"\n✅ {ok}/{len(results)} courses with CRICOS "
          f"({ok - backfilled} from page, {backfilled} from register). "
          f"Intake: {intake_date}\nSQL  -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
