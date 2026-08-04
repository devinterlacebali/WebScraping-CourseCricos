"""
Pembroke School Inc (00367B) - Standalone Web Scraper.
Generated from sa_nsw_17_schools_webscrape.py
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

PROVIDER_CODE = "00367B"
PROVIDER_NAME = "Pembroke School Inc"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "pembroke-school-inc"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
BASE_URL = "https://www.pembroke.sa.edu.au"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

INTL_PATHS = ["/admissions/international-students", "/international-students"]
MONTH_ORDER = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]


def fetch_html(url, timeout=20):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text
    except Exception as e:
        print(f"  ⚠️  Failed {url}: {e}")
        return ""


def extract_text_from(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()
    return re.sub(r"\s+", " ", soup.get_text()).strip()


def find_intake(text):
    months = {}
    for m in ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]:
        if m in text.lower():
            months[m.capitalize()] = True
    ordered = [m for m in MONTH_ORDER if m.lower() in months]
    return ", ".join(ordered) if ordered else "January, July"


def clean_fee(val):
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


def main():
    print(f"\\n  {PROVIDER_NAME} Web Scraper")
    print(f"  {'='*40}")
    print(f"  Provider: {PROVIDER_CODE}\\n")

    # Load CRICOS register
    cricos_courses = []
    if REGISTER_CSV.exists():
        with open(REGISTER_CSV, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r["CRICOS Provider Code"].strip() != PROVIDER_CODE:
                    continue
                if r["Expired"].strip().lower() == "yes":
                    continue
                dur = re.sub(r"[^\d]", "", r.get("Duration (Weeks)") or "")
                fee = r.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
                nt = r.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
                cricos_courses.append({
                    "cricos": r["CRICOS Course Code"].strip(),
                    "title": r["Course Name"].strip(),
                    "duration": int(dur) if dur.isdigit() else "",
                    "fee": fee,
                    "non_tuition": nt,
                })
    print(f"  CRICOS courses: {len(cricos_courses)}")

    # Fetch international page
    html = ""
    found_url = ""
    for path in INTL_PATHS:
        url = BASE_URL.rstrip("/") + path
        h = fetch_html(url)
        if h:
            html = h
            found_url = url
            print(f"  ✅ Found: {url}")
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
        m = re.search(r"IELTS\s*(?:overall\s*)?(?:score\s*)?(\d+\.?\d*)", text, re.IGNORECASE)
        if m:
            entry_req += f"IELTS {m.group(1)} overall. "
        else:
            entry_req += "IELTS required. "
    if not entry_req:
        entry_req = "Contact school for entry requirements"

    # Build rows from CRICOS data
    rows = []
    for cc in cricos_courses:
        rows.append({
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
        })

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
        print(f"  ✅ XLSX: {OUTPUT_XLSX.name}")
    except Exception as e:
        print(f"  ❌ XLSX error: {e}")

    # Generate SQL
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write(f"-- {PROVIDER_NAME} ({PROVIDER_CODE})\n")
        f.write(f"UPDATE provider_institution SET intake_date='{intake}', updated_at=NOW() WHERE cricos_provider_code='{PROVIDER_CODE}';\n\n")
        for r in rows:
            if not r["cricos"]:
                continue
            dur = r["duration"] if r["duration"] else "NULL"
            off = clean_fee(r["offshore_fee"]) if r["offshore_fee"] else "NULL"
            er = r["entry_requirements"].replace("'", "''")
            f.write(f"UPDATE courses SET course_duration_per_week={dur}, offshore_tuition_fee={off}, "
                    f"entry_requirements='{er}', updated_at=NOW() "
                    f"WHERE cricos_course_code='{r['cricos']}';\n")
    print(f"  ✅ SQL: {OUTPUT_SQL.name}")
    print(f"  ✅ Done - {len(rows)} courses")


if __name__ == "__main__":
    main()
