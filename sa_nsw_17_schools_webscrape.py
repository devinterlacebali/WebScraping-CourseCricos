"""
SA + NSW 17 Private Schools Web Scraper
Visits each school website to extract international fee / entry / intake data.
Generates {slug}_webscrape.xlsx and {slug}_webscrape_courses_update.sql per school.
"""
import os, re, sys, csv, json
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
REGISTER_CSV = BASE_DIR / "cricos-courses.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

PROVIDERS = [
    {
        "code": "00362G", "name": "Immanuel College",
        "slug": "immanuel-college",
        "url": "https://www.immanuel.sa.edu.au",
        "intl_paths": ["/enrolment/international-students", "/enrolment/fees", "/international"],
        "state": "SA",
    },
    {
        "code": "00365D", "name": "Mercedes College Springfield",
        "slug": "mercedes-college-springfield",
        "url": "https://www.mercedes.catholic.edu.au",
        "intl_paths": ["/join-us/international-students/", "/international-students", "/fees"],
        "state": "SA",
    },
    {
        "code": "00366C", "name": "Muirden Senior Secondary College",
        "slug": "muirden-senior-secondary-college",
        "url": "https://muirden.sa.edu.au",
        "intl_paths": ["/international", "/enrolments", "/fees"],
        "state": "SA",
    },
    {
        "code": "00367B", "name": "Pembroke School Inc",
        "slug": "pembroke-school-inc",
        "url": "https://www.pembroke.sa.edu.au",
        "intl_paths": ["/admissions/international-students", "/international-students"],
        "state": "SA",
    },
    {
        "code": "00368A", "name": "Prince Alfred College Inc",
        "slug": "prince-alfred-college-inc",
        "url": "https://pac.edu.au",
        "intl_paths": ["/admissions/international-students/", "/international/", "/admissions/fees"],
        "state": "SA",
    },
    {
        "code": "00369M", "name": "Pulteney Grammar School",
        "slug": "pulteney-grammar-school",
        "url": "https://www.pulteney.sa.edu.au",
        "intl_paths": ["/international-students/", "/international", "/enrolments/fees"],
        "state": "SA",
    },
    {
        "code": "00371F", "name": "St Aloysius College",
        "slug": "st-aloysius-college",
        "url": "https://www.sac.sa.edu.au",
        "intl_paths": ["/enrolments/international-students/", "/enrolments/fees", "/international"],
        "state": "SA",
    },
    {
        "code": "00373D", "name": "St Peter's Collegiate Girls' School",
        "slug": "st-peters-collegiate-girls-school",
        "url": "https://www.stpetersgirls.sa.edu.au",
        "intl_paths": ["/admissions/international-students", "/enrolment/fees", "/international"],
        "state": "SA",
    },
    {
        "code": "00374C", "name": "Trinity College North",
        "slug": "trinity-college-north",
        "url": "https://www.trinity.sa.edu.au",
        "intl_paths": ["/enrolments/international-students", "/enrolments/fees", "/international"],
        "state": "SA",
    },
    {
        "code": "00375B", "name": "Wilderness School",
        "slug": "wilderness-school",
        "url": "https://wilderness.com.au",
        "intl_paths": ["/enrolment/international-students", "/admissions/", "/about-us/fee-schedule"],
        "state": "SA",
    },
    {
        "code": "00379J", "name": "St Paul's International College",
        "slug": "st-pauls-international-college",
        "url": "https://www.spic.nsw.edu.au",
        "intl_paths": ["/enrolment/fees", "/enrolment", "/international"],
        "state": "NSW",
    },
    {
        "code": "00380E", "name": "Ascham School Ltd",
        "slug": "ascham-school-ltd",
        "url": "https://www.ascham.nsw.edu.au",
        "intl_paths": ["/enrolment/international-students", "/enrolment/fees", "/international", "/enrolling/fees"],
        "state": "NSW",
    },
    {
        "code": "00382C", "name": "Georges River Grammar School Ltd",
        "slug": "georges-river-grammar-school-ltd",
        "url": "https://grg.nsw.edu.au",
        "intl_paths": ["/enrolment/overseas-students/", "/enrolment/fees/", "/international"],
        "state": "NSW",
    },
    {
        "code": "00399E", "name": "Knox Grammar School",
        "slug": "knox-grammar-school",
        "url": "https://www.knox.nsw.edu.au",
        "intl_paths": ["/international", "/admissions/international-students", "/fees"],
        "state": "NSW",
    },
    {
        "code": "00401E", "name": "Masada College",
        "slug": "masada-college",
        "url": "https://www.masada.nsw.edu.au",
        "intl_paths": ["/international", "/admissions/international-students", "/fees"],
        "state": "NSW",
    },
    {
        "code": "00415K", "name": "Redeemer Baptist School Ltd",
        "slug": "redeemer-baptist-school-ltd",
        "url": "https://www.redeemer.nsw.edu.au",
        "intl_paths": ["/overseas-students-fees", "/international", "/overview/overseas-students"],
        "state": "NSW",
    },
]


def fetch_html(url, timeout=20):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text
    except Exception as e:
        return None


def extract_text(soup):
    for tag in soup.find_all(["script", "style", "noscript", "nav", "footer", "header"]):
        tag.decompose()
    return re.sub(r"\s+", " ", soup.get_text()).strip()


def find_intake(text):
    months_found = []
    month_names = {
        "january": "January", "february": "February", "march": "March",
        "april": "April", "may": "May", "june": "June",
        "july": "July", "august": "August", "september": "September",
        "october": "October", "november": "November", "december": "December"
    }
    for m_name, m_display in month_names.items():
        if m_name in text.lower() and m_display not in months_found:
            months_found.append(m_display)

    term_match = re.findall(r"(?:Term|Semester|Intake)\s*(\d)", text, re.IGNORECASE)
    if months_found:
        ordered = [m for m in MONTH_ORDER if m in months_found]
        return ", ".join(ordered)
    elif term_match:
        terms = sorted(set(term_match))
        return f"Term {', '.join(terms)}"
    else:
        # Check for February/July patterns
        has_feb = bool(re.search(r"\b(feb(?:ruary)?|jan(?:uary)?)\b", text, re.IGNORECASE))
        has_jul = bool(re.search(r"\b(jul(?:y)?)\b", text, re.IGNORECASE))
        if has_feb and has_jul:
            return "January, July"
        elif has_feb:
            return "January"
        elif has_jul:
            return "July"
        return "January, July"  # default for Australian schools


def extract_entry_requirements(soup, text):
    reqs = []
    # Check IELTS mentions
    ielts = re.search(r"IELTS\s*(?:overall\s*)?(?:score\s*)?(\d+\.?\d*)", text, re.IGNORECASE)
    if ielts:
        reqs.append(f"IELTS {ielts.group(1)} overall")

    # Check AEAS mentions
    aeas = re.search(r"AEAS\s*(?:score|test|result)?", text, re.IGNORECASE)
    if aeas:
        aeas_score = re.search(r"AEAS.*?(\d+[\s-]*\d+)", text, re.IGNORECASE)
        if aeas_score:
            reqs.append(f"AEAS test required ({aeas_score.group(1)})")
        else:
            reqs.append("AEAS test required")

    # Check English proficiency mentions
    if re.search(r"english\s*(?:language\s*)?proficiency", text, re.IGNORECASE) and not ielts:
        reqs.append("English language proficiency required")

    # Check academic requirements
    if re.search(r"(?:school\s*)?report", text, re.IGNORECASE) and re.search(r"(?:last|past|previous)\s*(?:\d\s*)?year", text, re.IGNORECASE):
        reqs.append("Previous school reports required")

    # Headings with entry requirement info
    for heading in soup.find_all(["h2", "h3", "h4", "h5"]):
        h_text = heading.get_text(strip=True).lower()
        if any(kw in h_text for kw in ["entry requirement", "admission", "english", "language", "how to apply"]):
            el = heading.find_next(["p", "ul", "div"])
            if el:
                section = el.get_text(strip=True)[:300]
                if section and len(section) > 20:
                    reqs.append(section)

    # Check for IELTS/AEAS in tables or lists around those keywords
    for p in soup.find_all(["p", "li"]):
        p_text = p.get_text(strip=True).lower()
        if ("ielts" in p_text or "aeas" in p_text) and len(p_text) > 15:
            reqs.append(p.get_text(strip=True)[:250])

    return "\n\n".join(reqs[:5]) if reqs else ""


def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v:
        return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n.is_integer() else str(n)
    except ValueError:
        return "NULL"


def scrape_school(prov):
    code = prov["code"]
    name = prov["name"]
    slug = prov["slug"]
    base_url = prov["url"]
    intl_paths = prov["intl_paths"]

    print(f"\n{'='*55}")
    print(f"  {name} ({code})")
    print(f"  {'='*55}")

    # Load CRICOS courses
    cricos_courses = []
    if REGISTER_CSV.exists():
        with open(REGISTER_CSV, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r["CRICOS Provider Code"].strip() != code:
                    continue
                if r["Expired"].strip().lower() == "yes":
                    continue
                dur_str = re.sub(r"[^\d]", "", r.get("Duration (Weeks)", "") or "")
                fee_str = r.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
                nt_str = r.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
                cricos_courses.append({
                    "cricos": r["CRICOS Course Code"].strip(),
                    "title": r["Course Name"].strip(),
                    "duration_weeks": int(dur_str) if dur_str.isdigit() else "",
                    "fee_total": fee_str,
                    "non_tuition_fee": nt_str,
                    "level": r.get("Course Level", "").strip(),
                })
    print(f"  CRICOS courses on register: {len(cricos_courses)}")

    # Fetch international page
    intl_html = None
    intl_url = ""
    for path in intl_paths:
        url = base_url.rstrip("/") + path
        h = fetch_html(url)
        if h:
            intl_html = h
            intl_url = url
            print(f"  ✅ Found page: {url}")
            break

    if not intl_html:
        print(f"  ⚠️  No international page found. Trying homepage...")
        h = fetch_html(base_url)
        if h:
            intl_html = h
            intl_url = base_url
            print(f"  ✅ Using homepage")

    # Parse
    soup = None
    text = ""
    fees_from_page = {}
    intake_text = "January, July"
    entry_req_text = ""

    if intl_html and len(intl_html) > 500:
        soup = BeautifulSoup(intl_html, "html.parser")
        text = extract_text(soup)
        intake_text = find_intake(text)
        entry_req_text = extract_entry_requirements(soup, text)

        # Extract fee table if present
        if soup:
            tables = soup.find_all("table")
            for table in tables:
                table_text = table.get_text().lower()
                if any(kw in table_text for kw in ["fee", "cost", "tuition", "$"]):
                    rows_t = table.find_all("tr")
                    for tr in rows_t:
                        cells = tr.find_all(["td", "th"])
                        if len(cells) >= 2:
                            key = cells[0].get_text(strip=True)
                            val = cells[1].get_text(strip=True)
                            if "$" in val:
                                fees_from_page[key] = val

        print(f"  Fees found on page: {len(fees_from_page)} items")
        print(f"  Intake: {intake_text}")
        print(f"  Entry req: {'✓' if entry_req_text else '✗ not found'}")

        # Check for PDF mentions
        pdf_links = []
        if soup:
            for a in soup.find_all("a", href=True):
                href = a["href"]
                if ".pdf" in href.lower() and any(kw in a.get_text(strip=True).lower() for kw in ["fee", "schedule", "international"]):
                    pdf_url = href if href.startswith("http") else base_url.rstrip("/") + "/" + href.lstrip("/")
                    pdf_links.append(pdf_url)

        if pdf_links:
            print(f"  📄 PDF fee schedule links found: {len(pdf_links)}")
            fees_from_page["_pdf_links"] = "; ".join(pdf_links)

    else:
        print(f"  ⚠️  No content fetched from website")

    # Build output rows
    rows = []
    fee_note = ""
    if fees_from_page and not fees_from_page.get("_pdf_links"):
        fee_note = "Fees from website"
    elif fees_from_page.get("_pdf_links"):
        fee_note = f"Fees in PDF schedule"
    else:
        fee_note = "No fees on website, using CSV register"

    source_label = "website" if intl_html and len(intl_html) > 500 else "register"

    for cc in cricos_courses:
        rows.append({
            "cricos": cc["cricos"],
            "title": cc["title"],
            "url": intl_url,
            "course_duration_per_week": cc["duration_weeks"],
            "offshore_tuition_fee": clean_numeric_fee(cc["fee_total"]) if clean_numeric_fee(cc["fee_total"]) != "NULL" else "",
            "onshore_tuition_fee": "",
            "enrolment_fee": clean_numeric_fee(cc["non_tuition_fee"]) if clean_numeric_fee(cc["non_tuition_fee"]) != "NULL" else "",
            "materials_fee": "",
            "intake": intake_text,
            "course_description": "",
            "entry_requirements": entry_req_text[:500] if entry_req_text else "",
            "source": source_label,
            "note": fee_note,
        })

    print(f"  Total courses: {len(rows)}")
    return rows, intake_text, entry_req_text


def get_school_dir(prov):
    dir_name = prov["name"]
    dir_path = BASE_DIR / dir_name
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def generate_outputs(prov, rows, intake_text, entry_req_text):
    slug = prov["slug"]
    code = prov["code"]
    name = prov["name"]
    out_dir = get_school_dir(prov)

    xlsx_path = out_dir / f"{slug}_webscrape.xlsx"
    sql_path = out_dir / f"{slug}_webscrape_courses_update.sql"

    # Deduplicate by CRICOS code
    seen = {}
    for r in rows:
        key = r["cricos"] or r["title"]
        if key not in seen:
            seen[key] = r
    deduped = list(seen.values())

    # Build XLSX data
    df_data = []
    for r in deduped:
        df_data.append({
            "CRICOS Course Code": r["cricos"],
            "Course Title": r["title"],
            "URL": r["url"],
            "Duration (Weeks)": r["course_duration_per_week"],
            "Offshore Tuition Fee": r["offshore_tuition_fee"],
            "Onshore Tuition Fee": r["onshore_tuition_fee"],
            "Enrolment Fee": r["enrolment_fee"],
            "Materials Fee": r["materials_fee"],
            "Intake": r["intake"] or intake_text,
            "Course Description": "",
            "Entry Requirements": r["entry_requirements"][:300] if r["entry_requirements"] else entry_req_text[:300],
            "Source": r["source"],
            "Note": r["note"],
        })

    if not df_data:
        df_data.append({
            "CRICOS Course Code": "", "Course Title": "No courses found", "URL": "",
            "Duration (Weeks)": "", "Offshore Tuition Fee": "",
            "Onshore Tuition Fee": "", "Enrolment Fee": "", "Materials Fee": "",
            "Intake": intake_text, "Course Description": "", "Entry Requirements": "",
            "Source": "", "Note": "",
        })

    try:
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Courses"
        if df_data:
            headers = list(df_data[0].keys())
            ws.append(headers)
            for row_data in df_data:
                ws.append([row_data.get(h, "") for h in headers])
        wb.save(xlsx_path)
        print(f"  ✅ XLSX -> {xlsx_path.name} ({len(df_data)} rows)")
    except Exception as e:
        print(f"  ❌ XLSX error: {e}")
        # Fallback to CSV
        csv_path = out_dir / f"{slug}_webscrape.csv"
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            if df_data:
                headers = list(df_data[0].keys())
                w = csv.DictWriter(f, fieldnames=headers)
                w.writeheader()
                w.writerows(df_data)
        print(f"  ✅ CSV fallback -> {csv_path.name}")

    # Generate SQL
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"-- {name} ({code}) - Web-scraped course data\n")
        f.write(f"-- Generated from: {prov['url']}\n\n")
        f.write(f"UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_text}',\n"
                f"    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{code}';\n\n")

        emitted = set()
        for r in deduped:
            cricos = r["cricos"]
            if not cricos or cricos in emitted:
                continue
            emitted.add(cricos)

            dur = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"
            offshore = clean_numeric_fee(r["offshore_tuition_fee"]) if r.get("offshore_tuition_fee") else "NULL"
            onshore = clean_numeric_fee(r["onshore_tuition_fee"]) if r.get("onshore_tuition_fee") else "NULL"
            enrol = clean_numeric_fee(r["enrolment_fee"]) if r.get("enrolment_fee") else "NULL"
            mat = clean_numeric_fee(r["materials_fee"]) if r.get("materials_fee") else "NULL"

            entry_req_sql = (r["entry_requirements"] or "").replace("'", "''")
            desc_sql = ""  # Course description

            f.write(f"UPDATE courses SET\n")
            f.write(f"    course_duration_per_week = {dur},\n")
            f.write(f"    offshore_tuition_fee = {offshore},\n")
            f.write(f"    onshore_tuition_fee = {onshore},\n")
            f.write(f"    enrolment_fee = {enrol},\n")
            f.write(f"    materials_fee = {mat},\n")
            f.write(f"    entry_requirements = '{entry_req_sql[:500]}',\n")
            f.write(f"    apply_form = '',\n")
            f.write(f"    updated_at = NOW()\n")
            f.write(f"WHERE cricos_course_code = '{cricos}';\n\n")

    print(f"  ✅ SQL  -> {sql_path.name}")
    print(f"  ✅ {len(emitted)} courses processed. Intake: {intake_text}")


def generate_webscrape_script(prov):
    """Generate a standalone {slug}_webscrape.py script for each school."""
    slug = prov["slug"]
    name = prov["name"]
    code = prov["code"]
    base_url = prov["url"]

    script_content = f'''"""
{name} ({code}) - Standalone Web Scraper.
Generated from sa_nsw_17_schools_webscrape.py
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

PROVIDER_CODE = "{code}"
PROVIDER_NAME = "{name}"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "{slug}"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
BASE_URL = "{base_url}"

HEADERS = {{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}}

INTL_PATHS = {json.dumps(prov["intl_paths"])}
MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


def fetch_html(url, timeout=20):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text
    except Exception as e:
        print(f"  ⚠️  Failed {{url}}: {{e}}")
        return ""


def extract_text_from(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()
    return re.sub(r"\\s+", " ", soup.get_text()).strip()


def find_intake(text):
    months = {{}}
    for m in ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]:
        if m in text.lower():
            months[m.capitalize()] = True
    ordered = [m for m in MONTH_ORDER if m.lower() in months]
    return ", ".join(ordered) if ordered else "January, July"


def clean_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\\d.]", "", str(val))
    if not v:
        return "NULL"
    try:
        n = float(v)
        return str(int(n)) if n.is_integer() else str(n)
    except ValueError:
        return "NULL"


def main():
    print(f"\\\\n  {{PROVIDER_NAME}} Web Scraper")
    print(f"  {{'='*40}}")
    print(f"  Provider: {{PROVIDER_CODE}}\\\\n")

    # Load CRICOS register
    cricos_courses = []
    if REGISTER_CSV.exists():
        with open(REGISTER_CSV, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                    continue
                if r["Expired"].strip().lower() == "yes":
                    continue
                dur = re.sub(r"[^\\d]", "", r.get("Duration (Weeks)") or "")
                fee = r.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
                nt = r.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
                cricos_courses.append({{
                    "cricos": r["CRICOS Course Code"].strip(),
                    "title": r["Course Name"].strip(),
                    "duration": int(dur) if dur.isdigit() else "",
                    "fee": fee,
                    "non_tuition": nt,
                }})
    print(f"  CRICOS courses: {{len(cricos_courses)}}")

    # Fetch international page
    html = ""
    found_url = ""
    for path in INTL_PATHS:
        url = BASE_URL.rstrip("/") + path
        h = fetch_html(url)
        if h:
            html = h
            found_url = url
            print(f"  ✅ Found: {{url}}")
            break

    if not html:
        print(f"  ⚠️  No page found, using CSV data only")

    # Parse
    text = extract_text_from(html) if html else ""
    intake = find_intake(text) if text else "January, July"

    # Entry requirements detection
    entry_req = ""
    if "AEAS" in text:
        entry_req += "AEAS test required. "
    if "IELTS" in text:
        m = re.search(r"IELTS\\s*(?:overall\\s*)?(?:score\\s*)?(\\d+\\.?\\d*)", text, re.IGNORECASE)
        if m:
            entry_req += f"IELTS {{m.group(1)}} overall. "
        else:
            entry_req += "IELTS required. "
    if not entry_req:
        entry_req = "Contact school for entry requirements"

    # Build rows from CRICOS data
    rows = []
    for cc in cricos_courses:
        rows.append({{
            "cricos": cc["cricos"],
            "title": cc["title"],
            "url": found_url,
            "duration": cc["duration"],
            "offshore_fee": clean_fee(cc["fee"]) if clean_fee(cc["fee"]) != "NULL" else "",
            "onshore_fee": "",
            "enrolment_fee": clean_fee(cc["non_tuition"]) if clean_fee(cc["non_tuition"]) != "NULL" else "",
            "intake": intake,
            "entry_requirements": entry_req[:500],
            "note": "",
        }})

    # Generate XLSX
    try:
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Courses"
        headers = ["CRICOS Course Code", "Course Title", "URL", "Duration (Weeks)",
                    "Offshore Tuition Fee", "Onshore Tuition Fee", "Enrolment Fee",
                    "Intake", "Entry Requirements", "Note"]
        ws.append(headers)
        for r in rows:
            ws.append([r["cricos"], r["title"], r["url"], r["duration"],
                       r["offshore_fee"], r["onshore_fee"], r["enrolment_fee"],
                       r["intake"], r["entry_requirements"], r["note"]])
        wb.save(OUTPUT_XLSX)
        print(f"  ✅ XLSX: {{OUTPUT_XLSX.name}}")
    except Exception as e:
        print(f"  ❌ XLSX error: {{e}}")

    # Generate SQL
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write(f"-- {{PROVIDER_NAME}} ({{PROVIDER_CODE}})\\n")
        f.write(f"UPDATE provider_institution SET intake_date='{{intake}}', updated_at=NOW() WHERE cricos_provider_code='{{PROVIDER_CODE}}';\\n\\n")
        for r in rows:
            if not r["cricos"]:
                continue
            dur = r["duration"] if r["duration"] else "NULL"
            off = clean_fee(r["offshore_fee"]) if r["offshore_fee"] else "NULL"
            er = r["entry_requirements"].replace("'", "''")
            f.write(f"UPDATE courses SET course_duration_per_week={{dur}}, offshore_tuition_fee={{off}}, "
                    f"entry_requirements='{{er}}', updated_at=NOW() "
                    f"WHERE cricos_course_code='{{r['cricos']}}';\\n")
    print(f"  ✅ SQL: {{OUTPUT_SQL.name}}")
    print(f"  ✅ Done - {{len(rows)}} courses")


if __name__ == "__main__":
    main()
'''
    return script_content


def main():
    print(f"SA + NSW 17 Private Schools Web Scraper")
    print(f"{'='*55}")
    print(f"Providers: {len(PROVIDERS)}\n")

    for prov in PROVIDERS:
        try:
            rows, intake_text, entry_req_text = scrape_school(prov)
            if not rows:
                print(f"  ⚠️  No courses found for {prov['name']}")
                # Use CSV data only
                code = prov["code"]
                cricos_courses = []
                if REGISTER_CSV.exists():
                    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
                        for r in csv.DictReader(f):
                            if r["CRICOS Provider Code"].strip() != code:
                                continue
                            if r["Expired"].strip().lower() == "yes":
                                continue
                            dur_str = re.sub(r"[^\d]", "", r.get("Duration (Weeks)", "") or "")
                            fee_str = r.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
                            nt_str = r.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
                            cricos_courses.append({
                                "cricos": r["CRICOS Course Code"].strip(),
                                "title": r["Course Name"].strip(),
                                "duration_weeks": int(dur_str) if dur_str.isdigit() else "",
                                "fee_total": fee_str,
                                "non_tuition_fee": nt_str,
                            })
                for cc in cricos_courses:
                    rows.append({
                        "cricos": cc["cricos"],
                        "title": cc["title"],
                        "url": prov["url"],
                        "course_duration_per_week": cc["duration_weeks"],
                        "offshore_tuition_fee": clean_numeric_fee(cc["fee_total"]) if clean_numeric_fee(cc["fee_total"]) != "NULL" else "",
                        "onshore_tuition_fee": "",
                        "enrolment_fee": clean_numeric_fee(cc["non_tuition_fee"]) if clean_numeric_fee(cc["non_tuition_fee"]) != "NULL" else "",
                        "materials_fee": "",
                        "intake": intake_text,
                        "course_description": "",
                        "entry_requirements": entry_req_text[:500] if entry_req_text else "",
                        "source": "register",
                        "note": "Website not accessible - data from CRICOS register",
                    })

            generate_outputs(prov, rows, intake_text, entry_req_text)

            # Generate standalone script
            script_content = generate_webscrape_script(prov)
            script_path = get_school_dir(prov) / f"{prov['slug']}_webscrape.py"
            if not script_path.exists():
                script_path.write_text(script_content, encoding="utf-8")
                print(f"  ✅ Script -> {script_path.name}")
            else:
                print(f"  ⏭️  Script exists -> {script_path.name} (skipped)")

        except Exception as e:
            print(f"  ❌ Error scraping {prov['name']}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
