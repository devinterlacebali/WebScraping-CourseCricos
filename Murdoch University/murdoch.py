"""
Murdoch University (Murdoch) course scraper — template format (requests).

Extracts from SSR course pages via meta tags + body parsing.
Sitefinity CMS, meta tags: course_cricos, course_code, course_name, etc.
Fees from <dl> details list in international/domestic tab.
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
PROVIDER_CODE = "00125J"          # Murdoch University
SLUG = "murdoch"
DIR = "Murdoch University"
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
            time.sleep(1.5 * (i + 1))
    raise last

# --- per-site extraction -----------------------------------------------------

def extract_meta(text, name):
    m = re.search(rf'<meta[^>]*name="{name}"[^>]*content="([^"]*)"', text, re.I)
    return m.group(1).strip() if m else ""

def extract_course_description(soup, text):
    """Get course overview section."""
    desc = ""
    # Look for the course overview heading and its content
    for heading_text in ['Course overview', 'course overview']:
        h = soup.find(lambda t: t.name in ['h2', 'h3', 'h4'] and heading_text in t.get_text())
        if h:
            # Get all content until next heading
            parts = []
            el = h.find_next_sibling()
            while el and el.name not in ['h2', 'h3', 'h4']:
                if el.name and el.get_text(strip=True):
                    parts.append(str(el))
                el = el.find_next_sibling()
            if parts:
                desc = sanitise(' '.join(parts))
                break
    return desc

def extract_entry_requirements(soup, text):
    """Get admission requirements section."""
    entry = ""
    for heading_text in ['Admission requirements', 'admission requirements', 'Entry requirements', 'entry requirements']:
        h = soup.find(lambda t: t.name in ['h2', 'h3', 'h4'] and heading_text in t.get_text())
        if h:
            parts = []
            el = h.find_next_sibling()
            while el and el.name not in ['h2', 'h3', 'h4']:
                if el.name and el.get_text(strip=True):
                    parts.append(str(el))
                el = el.find_next_sibling()
            if parts:
                entry = sanitise(' '.join(parts))
                break
    return entry

def extract_duration(full_text):
    """Extract duration from the page."""
    # Look for "Full time duration X" pattern
    m = re.search(r'Full time duration[^<]*?(\d+(?:\.\d+)?)', full_text, re.I)
    if m:
        return parse_years_to_weeks(m.group(1))
    # Fallback to scan for "X year(s)" 
    m = re.search(r'(\d+(?:\.\d+)?)\s*(year|semester|month)[s]?\s*\(?f', full_text, re.I)
    if m:
        return parse_years_to_weeks(m.group(0))
    return ""

def extract_fees(soup, text, duration_weeks):
    """Extract fees from the international/domestic tabs."""
    offshore = "NULL"
    onshore = "NULL"
    enrolment = "NULL"

    # Find international tab content
    # The page has student type selector with domestic/international tabs
    # Fee structure: First year fee and Full course fee
    
    # Check meta tags first
    cricos_code = extract_meta(text, 'course_cricos')
    
    # Find all <dl> blocks in the page
    for dl in soup.find_all('dl'):
        dl_text = dl.get_text()
        
        # Determine if this is international or domestic
        is_intl = False
        is_dom = False
        
        # Check parent for student-type class
        parent = dl.parent
        if parent:
            parent_classes = ' '.join(parent.get('class', []))
            if 'international' in parent_classes.lower():
                is_intl = True
            elif 'domestic' in parent_classes.lower():
                is_dom = True
        
        # Also check the text for clues
        dl_lower = dl_text.lower()
        if 'full course fee' in dl_lower:
            # Get the amounts
            amounts = re.findall(r'\$([0-9,]+)', dl_text)
            if amounts and 'full' in dl_lower:
                # Full course fee is the total
                total = float(amounts[-1].replace(',', ''))
                if is_intl:
                    offshore = str(int(total))
                elif is_dom:
                    onshore = str(int(total))
                else:
                    offshore = str(int(total))

    # If no international tab found, try finding via HTML attributes
    if offshore == "NULL":
        # Look for data-student-type-toggle="international" area
        intl_section = re.search(r'data-student-type-toggle="international"[^>]*>(.*?)(?:data-student-type-toggle|</section)', text, re.DOTALL)
        if intl_section:
            block = intl_section.group(1)
            amounts = re.findall(r'\$([0-9,]+)', block)
            if len(amounts) >= 2:
                # Full course fee (last/second amount)
                total = float(amounts[-1].replace(',', ''))
                offshore = str(int(total))
            elif len(amounts) == 1:
                offshore = str(int(float(amounts[0].replace(',', ''))))
        
        # Domestic
        dom_section = re.search(r'data-student-type-toggle="domestic"[^>]*>(.*?)(?:data-student-type-toggle|</section)', text, re.DOTALL)
        if dom_section:
            block = dom_section.group(1)
            amounts = re.findall(r'\$([0-9,]+)', block)
            if len(amounts) >= 2:
                total = float(amounts[-1].replace(',', ''))
                onshore = str(int(total))
            elif len(amounts) == 1:
                onshore = str(int(float(amounts[0].replace(',', ''))))

    return offshore, onshore, enrolment, "NULL"

def extract_intake_months(soup, text):
    """Extract intake/start months from the page."""
    found = set()
    # Look for "Semester 1, 2026" patterns
    for m in re.finditer(r'(Semester|Trimester)\s+(\d)[,\s]+(\d{4})', text):
        # Map semester to months
        sem = int(m.group(2))
        if sem == 1:
            found.update(['February', 'July'])  # Sem 1 = Feb/Jul start
        elif sem == 2:
            found.update(['July', 'August'])
    
    # Also check for month names
    found.update(months_in(text))
    
    return [m for m in MONTH_ORDER if m in found]

def extract_cricos(text):
    """Extract CRICOS course code from meta tag."""
    # Clean CRICOS - handle "See below" etc.
    cricos_code = extract_meta(text, 'course_cricos')
    if cricos_code and cricos_code.lower() in ('see below', 'multiple', 'various', ''):
        cricos_code = ""
    if cricos_code:
        m = re.search(r'[0-9A-Z]{5,8}', cricos_code)
        cricos_code = m.group(0) if m else cricos_code
    return cricos_code or ""

# --- per course ---------------------------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row.get("cricos", "")).strip()
    if cricos.lower() in ("nan", "none", "null"):
        cricos = ""
    cricos = re.sub(r'[^0-9A-Za-z]', '', cricos)
    title = str(row.get("title", "")).strip()
    if title.lower() in ('nan', '', 'none'):
        title = ''

    d = {"cricos": cricos, "title": title, "url": url,
         "course_description": "", "course_duration_per_week": "",
         "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
         "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}

    try:
        r = get_page(url)
        soup = BeautifulSoup(r.text, "html.parser")
        full = re.sub(r"\s+", " ", soup.get_text())

        # Title from h1 / meta
        d["title"] = title or extract_meta(r.text, 'course_name') or extract_meta(r.text, 'title')

        # Description + entry requirements
        d["course_description"] = clean_html(extract_course_description(soup, r.text))
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup, r.text))

        # Duration
        d["course_duration_per_week"] = extract_duration(full)

        # Fees
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], \
            d["enrolment_fee"], d["materials_fee"] = extract_fees(soup, r.text, d["course_duration_per_week"])

        # CRICOS
        d["cricos"] = d["cricos"] or extract_cricos(r.text)

        # Intake
        d["intake_months"] = extract_intake_months(soup, r.text)

        print(f"  ✅ {d['title'][:50] if d['title'] else url[:50]}")
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
        if i % 20 == 0:
            time.sleep(1.5)

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
