"""
University of Melbourne course scraper (Scrapling, plain HTTP).

UniMelb's Handbook is behind Imperva bot-protection, but two open sources cover
everything:
  * the **CRICOS register** (cricos-courses.csv, provider 00116K) is the authoritative
    list of registered courses (435) with code + duration(weeks) + TOTAL tuition;
  * **study.unimelb.edu.au** course pages expose clean <meta> tags (description,
    english_language_requirements, intakes_international, duration_international) and
    the course CRICOS in an embedded blob.

Strategy: the register is the spine (so every registered course is inserted), and each
course is enriched from its study.unimelb page when we can find it by name-slug AND the
page CRICOS matches. Register-only courses emit a *partial* UPDATE (code+fees+duration,
no description) so existing DB text isn't wiped.
"""
import re
import sys
import csv
import time
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
PROVIDER_CODE = "00116K"                         # The University of Melbourne
SLUG = "unimelb"
DIR = "The University of Melbourne (UniMelb)"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
REGISTER_CSV = "cricos-courses.csv"
SITEMAP_URL = "https://study.unimelb.edu.au/sitemaps/find-a-course.xml"

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
CRICOS_RE = re.compile(r"\b(\d{6}[A-Z]|\d{7})\b")

# --- helpers ---------------------------------------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5"}

def sanitise(html: str) -> str:
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    for t in frag.find_all("span"):
        t.unwrap()
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def slugify(s):
    s = re.sub(r"\(.*?\)", " ", s.lower())       # drop parentheticals
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

def num_fee(val):
    v = re.sub(r"[^\d.]", "", str(val or ""))
    return str(int(float(v))) if v else "NULL"

def get_page(url, tries=3):
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return Fetcher.get(url, stealthy_headers=True)
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

# --- register --------------------------------------------------------------
def load_register():
    out = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                continue
            if r["Expired"].strip().lower() == "yes":
                continue
            out.append({
                "cricos": r["CRICOS Course Code"].strip(),
                "title": r["Course Name"].strip(),
                "weeks": re.sub(r"[^\d]", "", r.get("Duration (Weeks)") or ""),
                "tuition": num_fee(r.get("Tuition Fee")),
                "non_tuition": num_fee(r.get("Non Tuition Fee")),
            })
    return out

# --- sitemap slug -> url ---------------------------------------------------
def load_sitemap():
    h = str(get_page(SITEMAP_URL).html_content)
    by_slug = {}
    for loc in re.findall(r"<loc>([^<]+)</loc>", h):
        if "/courses/" not in loc:
            continue
        by_slug.setdefault(loc.rstrip("/").split("/")[-1], []).append(loc)
    return by_slug

def candidate_url(title, by_slug):
    sl = slugify(title)
    if sl in by_slug and len(by_slug[sl]) == 1:
        return by_slug[sl][0]
    # prefix match (register name is a prefix of the page slug, or vice-versa)
    cands = []
    for s, urls in by_slug.items():
        if len(urls) == 1 and (s.startswith(sl) or sl.startswith(s)) and abs(len(s) - len(sl)) <= 6:
            cands.append(urls[0])
    return cands[0] if len(cands) == 1 else None

# --- page enrichment -------------------------------------------------------
def enrich(url):
    """Return (page_cricos, description, entry, intake_months) from a study page."""
    h = str(get_page(url).html_content)
    soup = BeautifulSoup(h, "html.parser")

    m = re.search(r'CRICOS code"[,:]\s*"([0-9A-Z]{6,7})"', h)
    page_cricos = m.group(1) if m else ""

    def meta(name):
        el = soup.find("meta", attrs={"name": name})
        return (el.get("content") or "").strip() if el else ""

    desc = meta("description")
    description = f"<h4>Course overview</h4><p>{desc}</p>" if desc else ""

    eng = meta("english_language_requirements")
    entry = f"<h4>Entry Requirements</h4><h5>English language requirements</h5>{sanitise(eng)}" if eng else ""

    intake = meta("intakes_international") or meta("intakes_domestic")
    months = [mo for mo in MONTH_ORDER if re.search(rf"\b{mo}\b", intake)]
    return page_cricos, description, entry, months

# --- per course ------------------------------------------------------------
def process(r, by_slug):
    d = {"cricos": r["cricos"], "title": r["title"],
         "url": "", "course_description": "", "course_duration_per_week": r["weeks"],
         "offshore_tuition_fee": r["tuition"], "onshore_tuition_fee": "NULL",
         "enrolment_fee": r["non_tuition"], "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": "",
         "intake_months": [], "source": "register", "note": ""}
    url = candidate_url(r["title"], by_slug)
    if url:
        try:
            pc, desc, entry, months = enrich(url)
            if pc == r["cricos"]:
                d.update(url=url, apply_form=url, source="page",
                         course_description=clean_html(desc),
                         entry_requirements=clean_html(entry), intake_months=months)
            else:
                d["note"] = f"slug match CRICOS {pc or '—'} != register {r['cricos']}; register-only"
        except Exception as e:
            d["note"] = f"enrich error: {e}"
    tag = "✅" if d["source"] == "page" else "🗂️ "
    print(f"{tag} {d['title'][:44]:44} → {d['cricos']} | off {d['offshore_tuition_fee']} "
          f"| {d['course_duration_per_week'] or '?'}w | {d['source']}")
    return d

# --- main ------------------------------------------------------------------
def main():
    register = load_register()
    by_slug = load_sitemap()
    print(f"Register: {len(register)} courses | sitemap slugs: {len(by_slug)}\n")
    results = [process(r, by_slug) for r in register]

    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

    enriched = sum(1 for d in results if d["source"] == "page")
    emitted = set()
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if d["cricos"] in emitted:
                f.write(f"-- ⚠️ Skipped (CRICOS {d['cricos']} already emitted): {d['title']}\n\n")
                continue
            emitted.add(d["cricos"])
            if d["source"] == "register":
                # no description from the register -> partial UPDATE (don't wipe text)
                f.write(f"""-- Register-only (no study.unimelb match): {d['title']}
UPDATE courses SET
    course_duration_per_week = {d["course_duration_per_week"] or "NULL"},
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
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
        "enrolment_fee": cell(d["enrolment_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
        "source": d["source"], "note": d["note"],
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    print(f"\n✅ {len(emitted)} courses inserted ({enriched} enriched from site, "
          f"{len(emitted)-enriched} register-only). Intake: {intake_date}\n"
          f"SQL  -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
