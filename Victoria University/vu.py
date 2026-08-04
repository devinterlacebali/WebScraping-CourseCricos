"""
Victoria University (VU) course scraper — template format (requests adaptation).

Fee is quoted per semester; multiply by 2 (semesters/year) × years for total.
CRICOS code in <span> or page body.
Intake months from body text.
"""
import os
import re
import sys

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
PROVIDER_CODE = "00124K"          # Victoria University
SLUG = "vu"
DIR = "Victoria University"
EXCEL_PATH = f"{DIR}/{SLUG}.xlsx"
SQL_PATH = f"{DIR}/{SLUG}_courses_update.sql"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
SESSION = requests.Session()
SESSION.headers.update(HEADERS)
TIMEOUT = 60

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

def clean_numeric_fee(val) -> str:
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def norm_title(s):
    s = re.sub(r"\b(in|of|the|and|a)\b", " ", s.lower())
    return re.sub(r"[^a-z0-9]", "", s)

def months_in(text):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", str(text)):
        k = tok.lower()
        if k in MONTHS and MONTHS[k] not in found:
            found.append(MONTHS[k])
    return found

def parse_years_to_weeks(text):
    m = re.search(r"([\d.]+)\s*years?", str(text), re.I)
    if m:
        try:
            years = float(m.group(1))
            return str(int(round(years * 52)))
        except ValueError:
            pass
    m = re.search(r"([\d.]+)\s*months?", str(text), re.I)
    if m:
        try:
            months = float(m.group(1))
            return str(int(round(months * 4.33)))
        except ValueError:
            pass
    m = re.search(r"(\d+)\s*weeks?", str(text), re.I)
    if m:
        return m.group(1)
    return ""

def get_page(url, tries=3):
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return SESSION.get(url, timeout=TIMEOUT)
        except Exception as e:
            last = e
            import time
            time.sleep(1.5 * (i + 1))
    raise last

# --- per-site extraction (template-shaped) -----------------------------------

def extract_course_description(page):
    """page is a BeautifulSoup object."""
    overview = page.select_one('#overview')
    if not overview:
        overview = page.find('div', id='overview')
    if overview:
        return sanitise(str(overview))
    return ""

def extract_entry_requirements(page):
    entry_el = page.select_one('#entry-requirements')
    if not entry_el:
        entry_el = page.find('div', id='entry-requirements')
    if entry_el:
        return sanitise(str(entry_el))
    return ""

def extract_duration(full_text):
    return parse_years_to_weeks(full_text)

def extract_fees(page, full_text, duration_weeks):
    years = 1
    ym = re.search(r"([\d.]+)\s*years?", full_text, re.I)
    if ym:
        years = float(ym.group(1))

    offshore = "NULL"
    onshore = "NULL"
    enrolment = "NULL"

    # International fee: "AU$18,400 per semester"
    for m in re.finditer(r'\$([0-9,]+)', full_text):
        start = max(0, m.start() - 80)
        ctx = full_text[start:m.end() + 100].strip()
        ctx_clean = re.sub(r'\s+', ' ', ctx).lower()
        if 'semester' in ctx_clean and any(kw in ctx_clean for kw in ['international', 'tuition']):
            per_sem = float(m.group(1).replace(',', ''))
            total = int(round(per_sem * 2 * years))
            offshore = str(total)
        elif 'per year' in ctx_clean and any(kw in ctx_clean for kw in ['indicative', 'fee']):
            annual = float(m.group(1).replace(',', ''))
            total = int(round(annual * years))
            if 'international' in ctx_clean:
                offshore = str(total)
            elif onshore == "NULL":
                onshore = str(total)

    # Application fee
    for m in re.finditer(r'\$([0-9,]+)', full_text):
        start = max(0, m.start() - 40)
        ctx = full_text[start:m.end() + 40].strip()
        ctx = re.sub(r'\s+', ' ', ctx)
        if 'application' in ctx.lower():
            enrolment = str(int(float(m.group(1).replace(',', ''))))
            break

    return offshore, onshore, enrolment, "NULL"

def extract_intake_months(page, full_text):
    found = months_in(full_text)
    return [m for m in MONTH_ORDER if m in found]

def extract_cricos(full_text):
    # VU: CRICOS code in <span> or body regex
    m = re.search(r'\b([0-9]{6,7}[A-Za-z]?)\b', full_text)
    return m.group(1) if m else ""

# --- per course (template-shaped) -------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row.get("cricos", "")).strip()
    if cricos.lower() in ("nan", "none", "null"):
        cricos = ""
    m = re.search(r"[0-9A-Z]{5,8}", cricos)
    cricos = m.group(0) if m else ""
    title = str(row.get("title", "")).strip()

    d = {"cricos": cricos, "title": title, "url": url,
         "course_description": "", "course_duration_per_week": "",
         "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
         "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}

    try:
        r = get_page(url)
        soup = BeautifulSoup(r.text, "html.parser")
        full = re.sub(r"\s+", " ", soup.get_text())

        # If international page empty, try domestic version
        empty_page = not soup.select_one('#overview') and not soup.select_one('#entry-requirements')
        if empty_page and '/international' in url:
            domestic_url = url.replace('/international', '')
            try:
                r2 = SESSION.get(domestic_url, timeout=TIMEOUT)
                soup2 = BeautifulSoup(r2.text, "html.parser")
                if soup2.select_one('#overview') or soup2.select_one('#entry-requirements'):
                    soup = soup2
                    full = re.sub(r"\s+", " ", soup2.get_text())
            except Exception:
                pass

        d["course_description"] = clean_html(extract_course_description(soup))
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup))

        # Use h1 as title if the driver title was empty
        h1 = soup.find('h1')
        if (not title or title == 'nan') and h1:
            d["title"] = h1.get_text(strip=True)

        d["course_duration_per_week"] = extract_duration(full)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], \
            d["enrolment_fee"], d["materials_fee"] = extract_fees(soup, full, d["course_duration_per_week"])
        d["cricos"] = d["cricos"] or extract_cricos(full)
        d["intake_months"] = extract_intake_months(soup, full)

        print(f"  ✅ {d['title'][:50] if d['title'] else url[:50]}")
    except Exception as e:
        print(f"  ❌ {url[:60]}: {e}")

    return d

# --- main (template-shaped) --------------------------------------------------
def main():
    import time as ttime

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
        if i % 20 == 0:
            ttime.sleep(1.5)

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
                f.write(f"-- ⚠️ Skipped (no CRICOS): {d['title']} | {d['url']}\n\n")
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
    print(f"\n✅ {len(results)} courses processed.")
    print(f"   With CRICOS: {with_cricos}")
    print(f"   With fee: {with_fee}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL   -> {SQL_PATH}")
    print(f"   xlsx  -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
