"""
Template course scraper (Scrapling). Copy to "<Institution>/<slug>.py" and fill the
TODOs. Standard shape: read xlsx (cricos,title,url) -> scrape each page -> write
<slug>_courses_update.sql + rewrite the xlsx with the full enriched record.

Only the extract_* functions change per site; everything else is boilerplate.
"""
import os
import re
import sys
import pandas as pd
from bs4 import BeautifulSoup            # only to sanitise small HTML fragments
from scrapling.fetchers import Fetcher

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- TODO: per-institution constants ---------------------------------------
PROVIDER_CODE = "<PROVIDER_CODE>"          # cricos_provider_code, e.g. "03844J"
SLUG = "<slug>"                            # file stem, e.g. "aibi"
DIR = "<Institution Name>"                 # folder name
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

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

# --- shared helpers (rarely need changing) ---------------------------------
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    return html.replace("'", "''").strip()

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def sanitise(html: str) -> str:
    frag = BeautifulSoup(html, "html.parser")
    for t in frag.find_all(["style", "script", "noscript", "form", "iframe", "img", "svg", "button"]):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != "href":
                del t[a]
    return str(frag)

def norm_title(s):
    s = re.sub(r"\b(in|of|the|and|a)\b", " ", s.lower())
    return re.sub(r"[^a-z0-9]", "", s)

def txt(el):
    return re.sub(r"\s+", " ", el.get_all_text()).strip()

def months_in(text):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", text):
        k = tok.lower()
        if k in MONTHS and MONTHS[k] not in found:
            found.append(MONTHS[k])
    return found

# --- per-site extraction (TODO: implement against the page builder) --------
def extract_course_description(page):
    # TODO: build "<h4>Section</h4>{sanitise(html)}" for each relevant section.
    return ""

def extract_entry_requirements(page):
    # TODO: return "<h4>Entry Requirements</h4>{sanitise(html)}".
    return ""

def extract_duration(full_text):
    # TODO: adapt to the site's wording ("78 weeks", "3 years full time", ...).
    m = re.search(r"(\d+(?:\.\d+)?\s*(?:weeks?|years?|months?))", full_text, re.IGNORECASE)
    return re.sub(r"\s+", " ", m.group(1)).lower() if m else ""

def extract_fees(page, full_text, duration):
    # TODO: offshore = international, onshore = domestic. Return TOTAL course fees.
    return "NULL", "NULL", "NULL", "NULL"   # offshore, onshore, enrolment, materials

def extract_intake_months(page, full_text):
    # TODO: pull the intake/start months for this course.
    return []

def extract_cricos(full_text):
    m = re.search(r"CRICOS (?:Course )?Code:\s*([0-9A-Z]{5,8})", full_text)
    return m.group(1) if m else ""

# --- per course ------------------------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    if cricos.lower() in ("nan", "none", "null"):
        cricos = ""
    m = re.search(r"[0-9A-Z]{5,8}", cricos)   # strip stray chars from pasted codes
    cricos = m.group(0) if m else ""
    title = str(row["title"]).strip()

    d = {"cricos": cricos, "title": title, "url": url, "course_description": "",
         "total_course_duration": "", "offshore_tuition_fee": "NULL",
         "onshore_tuition_fee": "NULL", "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}
    try:
        page = Fetcher.get(url, stealthy_headers=True)
        full = re.sub(r"\s+", " ", page.get_all_text())
        d["course_description"] = clean_html(extract_course_description(page))
        d["entry_requirements"] = clean_html(extract_entry_requirements(page))
        d["total_course_duration"] = extract_duration(full)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], d["enrolment_fee"], d["materials_fee"] = extract_fees(page, full, d["total_course_duration"])
        d["intake_months"] = extract_intake_months(page, full)
        # d["cricos"] = d["cricos"] or extract_cricos(full)   # enable if the page code is trustworthy
        print(f"✅ {url}")
    except Exception as e:
        print(f"❌ {url}: {e}")
    return d

# --- main ------------------------------------------------------------------
def main():
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel not found: {EXCEL_PATH}")
        return
    df = pd.read_excel(EXCEL_PATH)
    results = [scrape_course(r) for _, r in df.iterrows()]

    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⚠️ Skipped (no/unreliable CRICOS course code): {d['title']} | {d['url']}\n\n")
                continue
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
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
        "total_course_duration": d["total_course_duration"],
        "offshore_tuition_fee": cell(d["offshore_tuition_fee"]),
        "onshore_tuition_fee": cell(d["onshore_tuition_fee"]),
        "enrolment_fee": cell(d["enrolment_fee"]),
        "materials_fee": cell(d["materials_fee"]),
        "intake": ", ".join(d["intake_months"]),
        "course_description": cell(d["course_description"]),
        "entry_requirements": cell(d["entry_requirements"]),
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    print(f"\n✅ {len(results)} courses. Intake: {intake_date}\nSQL -> {SQL_PATH}\nxlsx -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
