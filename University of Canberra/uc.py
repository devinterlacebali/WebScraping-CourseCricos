"""
University of Canberra course scraper — template format (requests adaptation).

SSR site with tab-based course details. Fee data is loaded dynamically via
JS tristate button (Per Unit / Per Annum / Full Course) — not in static HTML.
CRICOS matched from cricos-courses.csv (individual codes not on page —
only provider code 00212K in footer).
"""
import os
import re
import sys
import csv
import time
import requests
from bs4 import BeautifulSoup

sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# --- constants ---------------------------------------------------------------
PROVIDER_CODE = "00212K"          # University of Canberra
SLUG = "uc"
DIR = "University of Canberra"
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

def months_in(text):
    found = []
    for tok in re.findall(r"[A-Za-z]{3,9}", str(text)):
        k = tok.lower()
        if k in MONTHS and MONTHS[k] not in found:
            found.append(MONTHS[k])
    return found

def get_page(url, tries=3):
    last = RuntimeError("unreachable")
    for i in range(tries):
        try:
            return SESSION.get(url, timeout=TIMEOUT)
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last

# --- per-site extraction (template format) -----------------------------------

def extract_course_description(page):
    """page = BeautifulSoup. UC stores description in 'About this course' accordion."""
    # Find "About this course" heading (text inside h3 with possible icon child)
    about = None
    for h in page.find_all(['h3', 'h4']):
        text = h.get_text(strip=True)
        if 'About this course' == text:
            about = h
            break
    if about:
        # Content is in the next sibling with class 'collapse' or 'course-details section'
        parent_container = about.find_parent('div', class_=re.compile(r'bs-accordion'))
        if parent_container:
            content = parent_container.find('div', class_=re.compile(r'course-details|tab-content'))
            if content:
                # Remove the AQF Level / English requirements modal buttons
                for modal in content.find_all('div', class_='modal-content'):
                    modal.decompose()
                for button in content.find_all('button'):
                    button.decompose()
                html = sanitise(str(content))
                return clean_html(html)
        # Fallback: get text after heading in page
        parts = []
        for sib in about.find_all_next():
            if sib.name in ['h3', 'h4'] and 'About' not in sib.get_text(strip=True):
                break
            if sib.name == 'p' and sib.get_text(strip=True):
                parts.append(str(sib))
        if parts:
            return clean_html(sanitise(''.join(parts)))
    return ""

def extract_entry_requirements(page):
    """page = BeautifulSoup. UC has 'Admission requirements' accordion."""
    req = None
    for h in page.find_all(['h3', 'h4']):
        text = h.get_text(strip=True)
        if text.lower() in ('admission requirements', 'entry requirements', 'admission'):
            req = h
            break
    if req:
        parent_container = req.find_parent('div', class_=re.compile(r'bs-accordion'))
        if parent_container:
            content = parent_container.find('div', class_=re.compile(r'course-details|tab-content'))
            if content:
                for modal in content.find_all('div', class_='modal-content'):
                    modal.decompose()
                for button in content.find_all('button'):
                    button.decompose()
                html = sanitise(str(content))
                return clean_html(html)
    return ""

def extract_duration(full_text):
    """full_text = page inner text. UC says 'Standard X years full time'."""
    m = re.search(r'Standard\s+(\d+\.?\d*)\s*(year|month|week)', full_text, re.I)
    if m:
        num = float(m.group(1))
        unit = m.group(2).lower()
        if 'year' in unit:
            return str(int(round(num * 52)))
        elif 'month' in unit:
            return str(int(round(num * 4.33)))
        else:
            return str(int(num))
    # Fallback
    m = re.search(r'(\d+\.?\d*)\s*(year|month|week)s?\s+full[- ]?time', full_text, re.I)
    if m:
        num = float(m.group(1))
        unit = m.group(2).lower()
        if 'year' in unit:
            return str(int(round(num * 52)))
        elif 'month' in unit:
            return str(int(round(num * 4.33)))
    return ""

def extract_fees(page, full_text, duration_weeks):
    """UC fee is JS-loaded via tristate button — not in static HTML."""
    return "NULL", "NULL", "NULL", "NULL"

def extract_intake_months(page, full_text):
    """UC mentions intake/teaching periods."""
    # Look for "Available teaching periods"
    m = re.search(r'Available teaching periods[^.]*\.', full_text, re.I)
    if m:
        text = m.group()
        found = months_in(text)
        if found:
            return found
    # Fallback: look for "Semester 1|2|3" patterns
    sems = re.findall(r'Semester\s*(\d)', full_text)
    if sems:
        sem_months = {'1': 'February', '2': 'July', '3': 'November'}
        found = []
        for s in sems:
            m = sem_months.get(s)
            if m and m not in found:
                found.append(m)
        return found
    # Generic month search
    return months_in(full_text)

def extract_cricos(page):
    """UC only has provider CRICOS in footer — individual codes not on page."""
    return ""

# --- per course (template format) --------------------------------------------
def scrape_course(row):
    url = str(row["url"]).strip()
    cricos = str(row.get("cricos", "")).strip()
    if cricos.lower() in ("nan", "none", "null", ""):
        cricos = ""
    cricos = re.sub(r'[^0-9A-Za-z]', '', cricos)
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

        d["course_description"] = clean_html(extract_course_description(soup))
        d["entry_requirements"] = clean_html(extract_entry_requirements(soup))
        d["course_duration_per_week"] = extract_duration(full)
        d["offshore_tuition_fee"], d["onshore_tuition_fee"], \
            d["enrolment_fee"], d["materials_fee"] = extract_fees(soup, full, d["course_duration_per_week"])
        d["intake_months"] = extract_intake_months(soup, full)

        print(f"  ✅ {title[:55] if title else url[:55]}")
    except Exception as e:
        print(f"  ❌ {url[:60]}: {e}")

    return d

# --- main (template format) --------------------------------------------------
def main():
    import pandas as pd

    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Excel not found: {EXCEL_PATH}")

        # Build driver from sitemap + CSV
        print("Building driver from sitemap...")
        r = SESSION.get('https://www.canberra.edu.au/services/wcm/site-map/course.xml', timeout=30)
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        course_map = {}
        for u in urls:
            parts = u.rstrip('/').split('/')
            if len(parts) >= 3:
                code = parts[-3]
                year = parts[-1]
                if code not in course_map or year > course_map[code][1]:
                    course_map[code] = (u, year)

        # Build CSV lookup
        csv_lookup = {}
        try:
            with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader)
                for row in reader:
                    if not row or len(row) < 4:
                        continue
                    if row[0].strip() == PROVIDER_CODE:
                        name = row[3].strip()
                        norm = re.sub(r'[^a-z0-9\s]', ' ', name.lower())
                        norm = re.sub(r'\s+', ' ', norm).strip()
                        csv_lookup[norm] = (row[2].strip(), name)
        except FileNotFoundError:
            pass

        rows = []
        for code, (url, year) in course_map.items():
            r = SESSION.get(url, timeout=20)
            if r.status_code != 200 or len(r.text) < 50000:
                continue
            soup = BeautifulSoup(r.text, 'html.parser')
            h1 = soup.find('h1')
            title = h1.get_text(strip=True) if h1 else code
            title_clean = title.split('(' + code)[0].strip()

            # CSV match
            norm_title = re.sub(r'[^a-z0-9\s]', ' ', title_clean.lower())
            norm_title = re.sub(r'\s+', ' ', norm_title).strip()
            cricos = csv_lookup.get(norm_title, ('',))[0]
            if not cricos:
                for csv_key, (cc, _) in csv_lookup.items():
                    tw = set(norm_title.split())
                    cw = set(csv_key.split())
                    if len(tw) >= 2 and len(cw) >= 2:
                        overlap = len(tw & cw)
                        if overlap / max(len(tw), len(cw)) >= 0.6:
                            cricos = cc
                            break

            rows.append({'cricos': cricos, 'title': title_clean, 'url': url})
            print(f'  {"✅" if cricos else "⏭️"} {title[:60]}')

        pd.DataFrame(rows).to_excel(EXCEL_PATH, index=False)
        print(f"\n✅ Driver saved: {len(rows)} courses")

    df = pd.read_excel(EXCEL_PATH)
    total = len(df)
    print(f"\n📊 Found {total} courses")

    results = []
    for i, (_, row) in enumerate(df.iterrows(), 1):
        d = scrape_course(row)
        results.append(d)
        if i % 15 == 0:
            time.sleep(1)

    months = set()
    for d in results:
        months.update(d["intake_months"])
    intake_date = ", ".join(m for m in MONTH_ORDER if m in months)

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

    with_cricos = sum(1 for d in results if d["cricos"])
    with_desc = sum(1 for d in results if d["course_description"])
    with_entry = sum(1 for d in results if d["entry_requirements"])
    with_dur = sum(1 for d in results if d["course_duration_per_week"])

    print(f"\n✅ {len(results)} courses processed.")
    print(f"   With CRICOS: {with_cricos}")
    print(f"   With description: {with_desc}")
    print(f"   With entry reqs: {with_entry}")
    print(f"   With duration: {with_dur}")
    print(f"   Intake: {intake_date}")
    print(f"   SQL   -> {SQL_PATH}")
    print(f"   xlsx  -> {EXCEL_PATH}")

if __name__ == "__main__":
    main()
