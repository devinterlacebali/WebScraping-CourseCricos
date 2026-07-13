"""
The University of Queensland (UQ) — international program scraper.

Provider CRICOS code: 00025B.

UQ's study site (study.uq.edu.au) is Drupal. The program listing paginates via
`?page=N` (30 per page, ~335 programs). Each program page carries BOTH a domestic and an
international variant of its content, marked with `data-student-type="domestic"` /
`"international"`; only programs open to international students show a CRICOS code, so a
missing CRICOS is the natural filter (those are skipped).

Fees are stored as **total course fee** (user preference): UQ quotes an *indicative annual*
fee, so total = annual x duration years. offshore = international (AUD) annual x years;
onshore = domestic (CSP) annual x years where available.
"""
import re
import sys
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

PROVIDER_CODE = "00025B"
DIR = "The University of Queensland"
SLUG = "uq"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"
BASE = "https://study.uq.edu.au"
LIST_URL = BASE + "/study-options/programs"

MONTHS = {m[:3].lower(): m for m in
          ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"]}
MONTH_ORDER = list({v: None for v in MONTHS.values()})

ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}


# ---------- helpers ----------
def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()


def sanitise(html: str) -> str:
    frag = BeautifulSoup(html or "", "html.parser")
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    for t in frag.find_all("span"):
        t.unwrap()
    while True:
        div = frag.find("div")
        if div is None:
            break
        if div.find(["p", "ul", "ol", "li", "div", "table", "h5"]):
            div.unwrap()
        else:
            div.name = "p"
    for t in frag.find_all(["h1", "h2", "h3", "h4", "h6"]):
        t.name = "h5"
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)


def strip_domestic(node):
    """Remove domestic-only variants so we keep the international + shared content."""
    for e in node.find_all(attrs={"data-student-type": re.compile(r"^domestic")}):
        e.decompose()
    return node


def get(url):
    return Fetcher.get(url, stealthy_headers=True)


def parse_years(duration_text):
    m = re.search(r"(\d+(?:\.\d+)?)\s*year", duration_text or "", re.I)
    if m:
        return float(m.group(1))
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:month|semester)", duration_text or "", re.I)
    if m:
        n = float(m.group(1))
        return n / 12.0 if "month" in duration_text.lower() else n / 2.0
    return None


# ---------- program list ----------
def collect_programs():
    urls = []
    seen = set()
    for page in range(0, 20):
        soup = BeautifulSoup(get(f"{LIST_URL}?page={page}").html_content, "html.parser")
        found = [a["href"] for a in soup.find_all("a", href=True)
                 if "/study-options/programs/" in a["href"] and re.search(r"-\d{4}$", a["href"].rstrip("/"))]
        new = 0
        for h in found:
            u = h if h.startswith("http") else BASE + h
            u = u.split("?")[0]
            if u not in seen:
                seen.add(u)
                urls.append(u)
                new += 1
        if page > 0 and new == 0:
            break
    return urls


# ---------- per-program extraction ----------
def section_after(soup, name):
    """International+shared HTML of the <h2> section titled `name`."""
    h = soup.find("h2", string=re.compile(r"^\s*" + re.escape(name) + r"\s*$", re.I))
    if not h:
        return ""
    container = h.find_parent("section") or h.find_parent("div")
    if not container:
        return ""
    copy = BeautifulSoup(str(container), "html.parser")
    for hh in copy.find_all(["h1", "h2"]):
        hh.decompose()
    strip_domestic(copy)
    return sanitise(str(copy))


def money(text):
    m = re.search(r"\$\s*([\d,]{4,})", text or "")
    return float(m.group(1).replace(",", "")) if m else None


def scrape_program(url):
    d = {"cricos": "", "title": "", "url": url, "course_description": "",
         "total_course_duration": "", "offshore_tuition_fee": None,
         "onshore_tuition_fee": None, "enrolment_fee": None, "materials_fee": None,
         "entry_requirements": "", "apply_form": url, "intake": "", "months": []}
    r = get(url)
    if r.status != 200:
        return d
    soup = BeautifulSoup(r.html_content, "html.parser")
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))

    h1 = soup.find("h1")
    d["title"] = h1.get_text(" ", strip=True) if h1 else ""

    m = re.search(r"CRICOS Code\s*([0-9]{6}[A-Z])", text)
    d["cricos"] = m.group(1) if m else ""

    # Duration sits between the "Duration" label and the next key fact ("Start"/"Location"/…).
    md = re.search(r"Duration\s+(\d+(?:\.\d+)?\s*(?:Years?|Semesters?|months?).*?)"
                   r"\s+(?:Start|Location|CRICOS|Program Code|Fees|Scholarships)\b", text, re.I)
    if not md:
        md = re.search(r"Duration\s+(\d+(?:\.\d+)?\s*(?:Years?|Semesters?|months?)[^.]*)", text, re.I)
    duration_text = md.group(1).strip() if md else ""
    d["total_course_duration"] = clean_html(duration_text)
    years = parse_years(duration_text)

    # Fees: international is prefixed "AUD $"; domestic is "$X 20YY". Both are indicative
    # annual figures -> multiply by duration years for the total course fee.
    intl_annual = None
    mi = re.search(r"AUD\s*\$\s*([\d,]+)", text)
    if mi:
        intl_annual = float(mi.group(1).replace(",", ""))
    dom_annual = None
    for mm in re.finditer(r"(AUD\s*)?\$\s*([\d,]{4,})\s*20\d\d", text):
        if not mm.group(1):
            dom_annual = float(mm.group(2).replace(",", ""))
            break
    if intl_annual is not None:
        d["offshore_tuition_fee"] = str(round(intl_annual * years)) if years else str(round(intl_annual))
    if dom_annual is not None:
        d["onshore_tuition_fee"] = str(round(dom_annual * years)) if years else str(round(dom_annual))

    # Intake months from the "Start Semester" key fact, e.g.
    # "Start Semester Semester 1 (22 Feb, 2027), Semester 2 (26 Jul, 2027), Summer Semester (29 Nov, 2027)".
    # Require the "Start Semester" label (not a stray "Start application" button) and read
    # months only from the "(DD Mon, YYYY)" date tokens so nothing else contaminates it.
    ms = re.search(r"Start\s+Semester\s+(.{0,200})", text)
    months = []
    if ms:
        for mm in re.findall(r"\(\s*\d{1,2}\s+([A-Za-z]{3,9})\s*,\s*20\d\d", ms.group(1)):
            mon = MONTHS.get(mm[:3].lower())
            if mon and mon not in months:
                months.append(mon)
    d["months"] = months
    d["intake"] = ", ".join(m for m in MONTH_ORDER if m in months)

    desc = section_after(soup, "Overview")
    if desc:
        d["course_description"] = clean_html(f"<h4>Overview</h4>{desc}")[:32000]
    entry = section_after(soup, "Entry requirements")
    if entry:
        d["entry_requirements"] = clean_html(f"<h4>Entry Requirements</h4>{entry}")[:32000]

    return d


# ---------- main ----------
def main():
    programs = collect_programs()
    print(f"📋 {len(programs)} programs discovered\n")

    results = []
    all_months = set()
    for i, url in enumerate(programs, 1):
        try:
            d = scrape_program(url)
        except Exception as e:
            print(f"❌ [{i}/{len(programs)}] {url}: {e}")
            continue
        if d["cricos"]:
            all_months.update(d["months"])
        results.append(d)
        tag = f"CRICOS {d['cricos']}" if d["cricos"] else "no CRICOS (skip)"
        print(f"✅ [{i}/{len(programs)}] {d['title'][:40]:42} | {tag} | off ${d['offshore_tuition_fee'] or '-'}")
        time.sleep(0.25)

    intake_date = ", ".join(m for m in MONTH_ORDER if m in all_months)

    def sql_num(v):
        return v if v else "NULL"

    print(f"\n💾 SQL -> {SQL_PATH}")
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        written = 0
        seen = {}
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no CRICOS course code): {d['title']} | {d['url']}\n\n")
                continue
            # Campus variants of the same program share one CRICOS; one DB row -> one
            # UPDATE, or the WHERE-clauses clobber each other. Note the extra variants.
            if d["cricos"] in seen:
                f.write(f"-- Shared CRICOS {d['cricos']} (already updated above): "
                        f"{d['title']} | {d['url']}\n\n")
                continue
            seen[d["cricos"]] = True
            written += 1
            f.write(
                "UPDATE courses SET\n"
                f"    course_description = '{d['course_description']}',\n"
                f"    total_course_duration = '{d['total_course_duration']}',\n"
                f"    offshore_tuition_fee = {sql_num(d['offshore_tuition_fee'])},\n"
                f"    onshore_tuition_fee = {sql_num(d['onshore_tuition_fee'])},\n"
                f"    enrolment_fee = {sql_num(d['enrolment_fee'])},\n"
                f"    materials_fee = {sql_num(d['materials_fee'])},\n"
                f"    entry_requirements = '{d['entry_requirements']}',\n"
                f"    apply_form = '{d['apply_form']}',\n"
                "    updated_at = NOW()\n"
                f"WHERE cricos_course_code = '{d['cricos']}';\n\n"
            )

    print(f"💾 xlsx -> {EXCEL_PATH}")

    def cell(v):
        return ("" if v in (None, "NULL") else str(v).replace("''", "'"))[:32000]

    pd.DataFrame([{
        "cricos": d["cricos"], "title": d["title"], "url": d["url"],
        "total_course_duration": cell(d["total_course_duration"]),
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "intake": cell(d["intake"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    skipped = sum(1 for d in results if not d["cricos"])
    print(f"\n🏁 Done. {written} course UPDATEs, {skipped} skipped. Provider intake: {intake_date}")


if __name__ == "__main__":
    main()
