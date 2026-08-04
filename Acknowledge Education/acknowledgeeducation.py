"""
Acknowledge Education course scraper — template format (requests adaptation).

Next.js site; fee data lives in accordion collapse components.
CRICOS matched from cricos-courses.csv where page CRICOS extraction fails.
"""
import os
import re
import sys
import csv
import time

# Strip hermes-agent venv from sys.path to avoid numpy ABI conflict
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

import pandas as pd
import requests
from bs4 import BeautifulSoup

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants ---------------------------------------------------------------
PROVIDER_CODE = "00197D"          # Acknowledge Education
SLUG = "acknowledgeeducation"
DIR = "Acknowledge Education"
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
            return str(int(round(float(m.group(1)) * 52)))
        except ValueError:
            pass
    m = re.search(r"([\d.]+)\s*months?", str(text), re.I)
    if m:
        try:
            return str(int(round(float(m.group(1)) * 4.33)))
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

# --- build CSV lookup for this provider -------------------------------------
def build_cricos_lookup():
    """Build {normalized_title: (cricos_code, raw_name)} from CRICOS CSV."""
    lookup = {}
    try:
        with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                if not row or len(row) < 4:
                    continue
                if row[0].strip() == PROVIDER_CODE:
                    name = row[3].strip()
                    # Normalize for matching
                    norm = re.sub(r'[^a-z0-9\s]', ' ', name.lower())
                    norm = re.sub(r'\s+', ' ', norm).strip()
                    lookup[norm] = (row[2].strip(), name)
    except FileNotFoundError:
        pass
    return lookup

def match_cricos(lookup, title, url):
    """Try to find CRICOS by matching title or URL slug against lookup."""
    if not title:
        return ""

    norm_title = re.sub(r'[^a-z0-9\s]', ' ', title.lower())
    norm_title = re.sub(r'\s+', ' ', norm_title).strip()

    # Direct match
    if norm_title in lookup:
        return lookup[norm_title][0]

    # Slug-based match from URL
    slug = url.rstrip('/').split('/')[-1]
    norm_slug = slug.replace('-', ' ')

    for csv_key, (cricos_code, csv_name) in lookup.items():
        # Does title start from or contain the CSV name?
        if norm_title.startswith(csv_key) or csv_key.startswith(norm_title):
            return cricos_code

        # Word overlap match
        title_words = set(norm_title.split())
        csv_words = set(csv_key.split())
        if len(title_words) >= 2 and len(csv_words) >= 2:
            overlap = len(title_words & csv_words)
            ratio = overlap / max(len(title_words), len(csv_words))
            if ratio >= 0.6:
                return cricos_code

    return ""

# --- per-site extraction (template format) -----------------------------------

def extract_course_description(page):
    """page = BeautifulSoup object. Get overview text."""
    for heading_text in ["Course Overview", "Overview"]:
        heading = page.find(["h4", "h5", "h6"], string=re.compile(heading_text, re.I))
        if heading:
            parts = []
            for sib in heading.find_all_next():
                if sib.name in ["h4", "h5", "h6"] and not re.search(heading_text, sib.text, re.I):
                    break
                if sib.name == "p" and sib.text.strip():
                    parts.append(str(sib))
            if parts:
                return f"<h4>{heading_text}</h4>{sanitise(''.join(parts))}"
    return ""

def extract_entry_requirements(page):
    """page = BeautifulSoup. Get entry reqs from accordion."""
    patterns = [
        r"Entry requirements",
        r"Academic and English Requirements",
        r"Requirements.*International",
    ]
    for ptn in patterns:
        label = page.find("p", string=re.compile(ptn, re.I))
        if not label:
            label = page.find(["h4", "h5"], string=re.compile(ptn, re.I))
        if label:
            parent = label.find_parent()
            accordion_body = parent.find_next("div", class_="accordion-body") if parent else None
            if not accordion_body:
                sections = page.find_all("div", class_="accordion-body")
                for sec in sections:
                    if label.get_text() in sec.get_text()[:100]:
                        accordion_body = sec
                        break
            if accordion_body:
                return clean_html(sanitise(str(accordion_body)))
    return ""

def extract_duration(full_text):
    """full_text = page inner text. Returns weeks as string."""
    m = re.search(r"(\d+\.?\d*)\s*(year|month|week)", full_text, re.I)
    if m:
        return parse_years_to_weeks(m.group(0))
    return ""

def extract_fees(page, full_text, duration_weeks):
    """
    page = BeautifulSoup
    full_text = page text
    duration_weeks = str

    Fee data lives in accordion collapse components.
    Acknowledge uses per-unit pricing in some courses.
    Returns (offshore, onshore, enrolment, materials).
    """
    raw_html = str(page)
    body = re.sub(r'<[^>]+>', ' ', raw_html)
    body = re.sub(r'\s+', ' ', body)

    offshore = "NULL"
    onshore = "NULL"
    materials = "NULL"
    enrolment = "NULL"

    # --- Try accordion-based extraction (most reliable for AE) ---
    accordions = page.find_all("div", class_="accordion-body")
    for acc in accordions:
        acc_text = acc.get_text(strip=True)
        # International fee section
        if "international" in acc_text.lower() and ("tuition" in acc_text.lower() or "fee" in acc_text.lower()):
            # Split the text to find the International segment
            intl_part = acc_text.lower().split("international", 1)[1] if "international" in acc_text.lower() else acc_text
            
            # Per-unit pricing: $X per unit x Y units
            per_unit = re.findall(r'\$([0-9,]+)\s*per\s*unit', intl_part, re.I)
            unit_counts = re.findall(r'x\s*(\d+)\s*units?', intl_part, re.I)
            if per_unit and unit_counts and len(per_unit) == len(unit_counts):
                total = 0
                for p, u in zip(per_unit, unit_counts):
                    total += int(p.replace(',', '')) * int(u)
                offshore = str(total)
            else:
                # Try "Full tuition fee: $XXXX" pattern
                m = re.search(r'full\s*tuition\s*fee[:\s]*\$([0-9,]+)', intl_part, re.I)
                if m:
                    offshore = str(int(m.group(1).replace(',', '')))
                else:
                    # First $ amount AFTER "International" in the accordion
                    dm = re.search(r'\$([0-9,]{3,})', intl_part)
                    if dm:
                        offshore = str(int(dm.group(1).replace(',', '')))

        # Domestic fee section
        if "domestic" in acc_text.lower() and ("tuition" in acc_text.lower() or "fee" in acc_text.lower()):
            m = re.search(r'\$([0-9,]+)', acc_text)
            if m:
                onshore = str(int(m.group(1).replace(',', '')))

        # Administration / enrolment fee
        adm_m = re.search(r'administration\s*fee[:\s]*\$([0-9,]+)', acc_text, re.I)
        if adm_m:
            enrolment = str(int(adm_m.group(1).replace(',', '')))

        # Materials fee
        mat_m = re.search(r'materials?\s*fee[:\s]*\$([0-9,]+)', acc_text, re.I)
        if mat_m:
            materials = str(int(mat_m.group(1).replace(',', '')))

    # --- Fallback: stripped body text ---
    if offshore == "NULL":
        intl_idx = body.lower().find("international student")
        if intl_idx >= 0:
            intl_block = body[intl_idx:intl_idx + 500]
            dm = re.search(r'\$([0-9,]{3,})', intl_block)  # 3+ digits to exclude RSC tokens
            if dm:
                offshore = str(int(dm.group(1).replace(',', '')))

    if offshore == "NULL":
        for m in re.finditer(r'International\s*Student.*?\$([0-9,]{3,})', raw_html, re.DOTALL):
            offshore = str(int(m.group(1).replace(',', '')))
            break

    if onshore == "NULL":
        dom_idx = body.lower().find("domestic student")
        if dom_idx >= 0:
            dom_block = body[dom_idx:dom_idx + 500]
            dm = re.search(r'\$([0-9,]{3,})', dom_block)
            if dm:
                onshore = str(int(dm.group(1).replace(',', '')))

    # Fallback enrolment/materials from body
    if enrolment == "NULL":
        enrol_m = re.search(r'Enrolment\s*fee[:\s]*\$([0-9,]+)', body, re.I)
        if enrol_m:
            enrolment = str(int(float(enrol_m.group(1).replace(',', ''))))

    if materials == "NULL":
        mat_m = re.search(r'Materials?\s*fee[:\s]*\$([0-9,]+)', body, re.I)
        if mat_m:
            materials = str(int(float(mat_m.group(1).replace(',', ''))))

    return offshore, onshore, enrolment, materials

def extract_intake_months(page, full_text):
    """Return list of month strings."""
    found = months_in(full_text)
    return [m for m in MONTH_ORDER if m in found]

def extract_cricos(page):
    """page = BeautifulSoup. Extract CRICOS from CRICOS link."""
    a = page.find("a", href=re.compile(r"cricos\.education\.gov\.au", re.I))
    if a:
        text = a.get_text(strip=True)
        m = re.match(r'^(\d{6,7}[A-Za-z]?)$', text)
        if m:
            return m.group(1)
    m = re.search(r'\b(\d{6,7}[A-Za-z]?)\b', page.get_text())
    return m.group(1) if m else ""

# --- per course (template format) --------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row.get("cricos", "")).strip()
    if cricos.lower() in ("nan", "none", "null", ""):
        cricos = ""
    cricos = re.sub(r'[^0-9A-Za-z]', '', cricos)
    title = str(row.get("title", "")).strip()
    if title.lower() in ('nan', '', 'none'):
        title = ''  # will fill from page

    d = {"cricos": cricos, "title": title, "url": url,
         "course_description": "", "course_duration_per_week": "",
         "offshore_tuition_fee": "NULL", "onshore_tuition_fee": "NULL",
         "enrolment_fee": "NULL", "materials_fee": "NULL",
         "entry_requirements": "", "apply_form": url, "intake_months": []}

    try:
        r = get_page(url)
        soup = BeautifulSoup(r.text, "html.parser")
        full = re.sub(r"\s+", " ", soup.get_text())

        # Title from page heading if empty
        if not d["title"]:
            h1 = soup.find("h1")
            if h1:
                d["title"] = h1.get_text(strip=True)

        d["course_description"] = clean_html(extract_course_description(soup))
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup))
        d["course_duration_per_week"] = extract_duration(full)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], \
            d["enrolment_fee"], d["materials_fee"] = extract_fees(soup, full, d["course_duration_per_week"])

        # CRICOS from page if not in driver
        if not d["cricos"]:
            d["cricos"] = extract_cricos(soup)

        d["intake_months"] = extract_intake_months(soup, full)

        print(f"  ✅ {d['title'][:50] if d['title'] else url[:50]}")
    except Exception as e:
        print(f"  ❌ {url[:60]}: {e}")

    return d

# --- main (template format) --------------------------------------------------
def main():
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel not found: {EXCEL_PATH}")
        return

    # Build CSV lookup
    csv_lookup = build_cricos_lookup()
    print(f"📚 CRICOS CSV lookup: {len(csv_lookup)} courses for {PROVIDER_CODE}")

    df = pd.read_excel(EXCEL_PATH)
    total = len(df)
    print(f"📊 Found {total} courses")

    # Try to fill missing CRICOS from CSV before scraping
    csv_matched = 0
    for i, (_, row) in enumerate(df.iterrows()):
        if not row.get("cricos") or str(row.get("cricos", "")).strip().lower() in ("nan", "", "none"):
            matched = match_cricos(csv_lookup, str(row.get("title", "")), str(row.get("url", "")))
            if matched:
                df.at[i, "cricos"] = matched
                csv_matched += 1
    print(f"  → CRICOS matched from CSV: {csv_matched}")

    results = []
    for i, (_, row) in enumerate(df.iterrows(), 1):
        d = scrape_course(row)
        results.append(d)
        if i % 10 == 0:
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
    print(f"\n✅ {len(results)} courses processed.")
    print(f"   With CRICOS: {with_cricos}")
    print(f"   With fee: {with_fee}")
    print(f"   With description: {with_desc}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL   -> {SQL_PATH}")
    print(f"   xlsx  -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
