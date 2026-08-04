"""
UWA course scraper — template format (requests).
Sitecore CMS with tab UI — fee/intake not available in static HTML.
CRICOS matched from CRICOS CSV database.
"""
import os
import re
import sys
import time

# Strip hermes-agent venv from sys.path to avoid numpy ABI conflict
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

import requests
import pandas as pd
from bs4 import BeautifulSoup

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants ---------------------------------------------------------------
PROVIDER_CODE = "00126G"          # UWA
SLUG = "uwa"
DIR = "The University of Western Australia"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
SESSION = requests.Session()
SESSION.headers.update(HEADERS)
TIMEOUT = 30

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# --- shared helpers (from template) ------------------------------------------
ALLOWED_TAGS = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "a", "br", "h5",
                "table", "thead", "tbody", "tr", "td", "th"}

def sanitise(html: str) -> str:
    if not html:
        return ""
    frag = BeautifulSoup(html, "html.parser")
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
    for p in frag.find_all("p"):
        s = p.get_text(strip=True)
        if s.endswith(":") and len(s) < 60 and not p.find(["strong", "b", "a"]):
            p.string = ""
            strong = frag.new_tag("strong")
            strong.string = s
            p.append(strong)
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    for t in frag.find_all(["p", "li", "strong", "b", "em", "i"]):
        if not t.get_text(strip=True) and not t.find("br"):
            t.decompose()
    return str(frag)

def clean_html(html: str) -> str:
    if not html:
        return ""
    return re.sub(r"\s+", " ", html).replace("'", "''").strip()

def get_page(url, tries=2):
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return SESSION.get(url, timeout=TIMEOUT)
        except Exception as e:
            last = e
            time.sleep(2)
    raise last

# --- extraction --------------------------------------------------------------

def extract_course_description(soup, text):
    """Get description from DEGREE OVERVIEW tab."""
    # Find "About the..." heading text that contains the overview
    h2 = soup.find(lambda t: t.name == 'h2' and 'About the' in t.get_text())
    if h2:
        parts = []
        el = h2.find_next_sibling()
        while el and el.name not in ['h2', 'h3', 'h4']:
            if el.name and el.get_text(strip=True):
                parts.append(str(el))
            el = el.find_next_sibling()
        if parts:
            return sanitise(' '.join(parts))
    return ""

def extract_entry_requirements(soup, text):
    """Get entry requirements from tabpanel."""
    # UWA puts entry requirements in a role="tabpanel"
    entry_tab = soup.find(lambda t: t.get('role') == 'tabpanel' and
                          'entry requirement' in (t.get_text(strip=True) or '').lower())
    if entry_tab:
        content = entry_tab.decode_contents()
        # Remove the heading part (first h2 or heading)
        content = re.sub(r'^.*?<h[23][^>]*>.*?</h[23]>\s*', '', content, flags=re.DOTALL)
        return sanitise(content.strip())
    
    # Fallback: find h2 with "Entry requirements"
    h2 = soup.find(lambda t: t.name == 'h2' and 'Entry requirements' == t.get_text(strip=True))
    if h2:
        parts = []
        el = h2.find_next_sibling()
        while el and el.name not in ['h2', 'h3', 'h4']:
            if el.name and el.get_text(strip=True):
                parts.append(str(el))
            el = el.find_next_sibling()
        if parts:
            return sanitise(' '.join(parts))
    return ""

def extract_duration(full_text):
    """Extract duration weeks from body text."""
    m = re.search(r'(\d+(?:\.\d+)?)\s*(year|semester|month)[s]?\s*full.?time', full_text, re.I)
    if m:
        try:
            val = float(m.group(1))
            unit = m.group(2).lower()
            if unit == 'year' or unit == 'years':
                return str(int(round(val * 52)))
            elif unit in ('month', 'months'):
                return str(int(round(val * 4.33)))
            elif unit in ('semester', 'semesters'):
                return str(int(round(val * 26)))
        except:
            pass
    return ""

def extract_fees(page, full_text, duration_weeks):
    """UWA fees are per-unit via fee calculator — not available in static HTML."""
    return ("NULL", "NULL", "NULL", "NULL")

def extract_intake_months(page, full_text):
    """UWA intake info is JS-rendered in tabs."""
    found = set()
    m = re.search(r'INTAKE\s+(?:-\s+)?(\w+)', full_text, re.I)
    if m:
        month = m.group(1)
        if month.lower() == 'february':
            found.update(['February', 'July'])
        elif month == 'Semester':
            found.update(['February', 'July'])
    return [m for m in MONTH_ORDER if m in found]

def extract_cricos(full_text):
    """CRICOS already matched from CSV — no extraction needed."""
    return ""

# --- per course --------------------------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row.get("cricos", "")).strip()
    if cricos.lower() in ("nan", "none", "null", ""):
        cricos = ""
    title = str(row.get("title", "")).strip()
    if title.lower() in ('nan', '', 'none'):
        title = ''

    d = {"cricos": cricos, "title": title, "url": url,
         "course_description": "", "course_duration_per_week": "",
         "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
         "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}

    if not cricos:
        print(f"  ⏭️ {title[:50] if title else url[:50]} (no CRICOS)")
        return d

    try:
        r = get_page(url)
        soup = BeautifulSoup(r.text, "html.parser")
        full = re.sub(r"\s+", " ", soup.get_text())

        d["title"] = title
        d["course_description"] = clean_html(extract_course_description(soup, r.text))
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup, r.text))
        d["course_duration_per_week"] = extract_duration(full)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], d["enrolment_fee"], d["materials_fee"] = extract_fees(soup, full, "")
        d["intake_months"] = extract_intake_months(soup, full)

        print(f"  ✅ {d['title'][:50]}")
    except Exception as e:
        print(f"  ❌ {url[:60]}: {e}")

    return d

# --- main ----------------------------------------------------------------------
def main():
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel not found: {EXCEL_PATH}")
        return

    df = pd.read_excel(EXCEL_PATH)
    total = len(df)
    print(f"📊 Found {total} courses")

    results = []
    for i, (_, row) in enumerate(df.iterrows(), 1):
        d = scrape_course(row)
        results.append(d)
        if i % 30 == 0:
            time.sleep(1)

    # Collect intake months
    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

    # Write SQL
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        f.write("-- UPDATE provider institution\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d["cricos"]:
                f.write(f"-- ⏭️ Skipped (no CRICOS): {d['title']} | {d['url']}\n\n")
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

    # Write enriched Excel
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
    } for d in results]).to_excel(EXCEL_PATH, index=False)

    # Stats
    with_cricos = sum(1 for d in results if d["cricos"])
    with_fee = sum(1 for d in results if d["offshore_tuition_fee"] not in ("NULL", ""))
    with_desc = sum(1 for d in results if d["course_description"])
    with_entry = sum(1 for d in results if d["entry_requirements"])
    print(f"\n✅ {len(results)} courses processed.")
    print(f"   With CRICOS: {with_cricos}")
    print(f"   With description: {with_desc}")
    print(f"   With entry reqs: {with_entry}")
    print(f"   With fee: {with_fee}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL   -> {SQL_PATH}")
    print(f"   xlsx  -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
