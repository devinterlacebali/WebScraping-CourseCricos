"""
Lan-Grove Office Training (SBTA) - Web scraping from www.sbta.com.au (provider 00181A).
Visits course category pages to extract fee/duration data.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
from bs4 import BeautifulSoup
import openpyxl

PROVIDER_CODE = "00181A"
PROVIDER_NAME = "Lan-Grove Office Training (SBTA)"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "sbta"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n >= 100 else "NULL"

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper\n  {'='*50}\n  Provider: {PROVIDER_CODE}")
    
    # Load CRICOS data
    cricos_map = {}
    seen_codes = set()
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if r["Expired"].strip().lower() == "yes": continue
            code = r["CRICOS Course Code"].strip()
            if code not in seen_codes:
                seen_codes.add(code)
                dur = re.sub(r"[^\d]", "", r.get("Duration (Weeks)") or "0")
                fee = r.get("Tuition Fee", "").strip().replace("$","").replace(",","")
                ntf = r.get("Non Tuition Fee", "").strip().replace("$","").replace(",","")
                cricos_map[code] = {
                    "title": r["Course Name"].strip(),
                    "cricos": code,
                    "duration_weeks": int(dur) if dur.isdigit() else 0,
                    "tuition_fee": fee,
                    "non_tuition_fee": ntf,
                    "level": r.get("Course Level", "").strip(),
                }
    
    # Scrape SBTA website - visit course category pages
    course_pages = [
        ("https://www.sbta.com.au/english/", "English"),
        ("https://www.sbta.com.au/accounting/", "Accounting"),
        ("https://www.sbta.com.au/business/", "Business"),
        ("https://www.sbta.com.au/commercial-cookery/", "Commercial Cookery"),
        ("https://www.sbta.com.au/hospitality/", "Hospitality"),
        ("https://www.sbta.com.au/age-care/", "Age Care"),
        ("https://www.sbta.com.au/leadership-and-management/", "Leadership & Management"),
        ("https://www.sbta.com.au/marketing-and-communication/", "Marketing"),
        ("https://www.sbta.com.au/project-management/", "Project Management"),
        ("https://www.sbta.com.au/tourism/", "Tourism"),
    ]
    
    scraped_data = {}
    for url, cname in course_pages:
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                info = {'desc': '', 'duration': '', 'fee': '', 'intake': ''}
                for tag in soup.find_all(['p', 'li', 'div', 'span', 'h2', 'h3', 'h4']):
                    t = tag.get_text(strip=True)
                    tl = t.lower()
                    if any(kw in tl for kw in ['duration', 'weeks', 'full-time', 'part-time', 'months', 'years']):
                        if not info['duration']: info['duration'] = t[:200]
                    if any(kw in tl for kw in ['intake', 'start', 'commence']):
                        if not info['intake']: info['intake'] = t[:200]
                    if len(t) > 80 and not info['desc']:
                        # Get first substantial paragraph
                        info['desc'] = t[:500]
                # Look for fee info specifically
                for tag in soup.find_all(['div', 'p', 'li']):
                    t = tag.get_text(strip=True)
                    if '$' in t and any(kw in t.lower() for kw in ['fee', 'cost', 'price', 'tuition', 'total']):
                        info['fee'] = t[:200]
                        break
                scraped_data[cname] = info
                print(f"  Scraped: {cname}")
        except Exception as e:
            print(f"  Error scraping {cname}: {e}")
    
    # Also check Timetable and Fees page
    try:
        r = requests.get("https://www.sbta.com.au/timetable-and-fees/", timeout=15)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            for tag in soup.find_all(['table', 'div', 'p']):
                t = tag.get_text(strip=True)
                if '$' in t:
                    print(f"  Fee info on timetable page: {t[:200]}")
    except:
        pass
    
    # Build output
    intake_date = "Rolling intake - contact SBTA"
    out = []
    for code, cinfo in cricos_map.items():
        out.append({
            "cricos": code,
            "title": cinfo['title'],
            "url": "",
            "course_duration_per_week": cinfo['duration_weeks'],
            "offshore_tuition_fee": cinfo['tuition_fee'],
            "onshore_tuition_fee": "",
            "enrolment_fee": cinfo['non_tuition_fee'],
            "materials_fee": "",
            "intake": intake_date,
            "course_description": "",
            "entry_requirements": "",
            "source": "web+register",
            "note": "Scraped from sbta.com.au",
        })
    
    # Write XLSX
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Courses"
    headers = ["cricos", "title", "url", "course_duration_per_week", "offshore_tuition_fee",
               "onshore_tuition_fee", "enrolment_fee", "materials_fee", "intake",
               "course_description", "entry_requirements", "source", "note"]
    ws.append(headers)
    for row in out:
        ws.append([row[h] for h in headers])
    wb.save(OUTPUT_XLSX)
    
    # SQL
    emitted = set()
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write(f"-- Update provider institution details\n"
                f"UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for r in out:
            if r["cricos"] in emitted: continue
            emitted.add(r["cricos"])
            dur = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"
            fee = clean_numeric_fee(r["offshore_tuition_fee"])
            enr = clean_numeric_fee(r["enrolment_fee"])
            f.write(f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"\n  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
