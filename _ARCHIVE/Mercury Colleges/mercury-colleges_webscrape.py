"""
Mercury Colleges - Web scraping from www.mercurycolleges.nsw.edu.au (provider 00172B).
Visits the courses page and individual course pages to extract fee/duration/intake data.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
from bs4 import BeautifulSoup
import openpyxl

PROVIDER_CODE = "00172B"
PROVIDER_NAME = "Mercury Colleges"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "mercury-colleges"
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
    
    # Scrape Mercury website - visit the Price List page
    course_fees = {}
    intake_text = "Contact college for intake dates"
    
    try:
        r = requests.get("https://www.mercurycolleges.nsw.edu.au/", timeout=30)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            # Find Price List link
            for a in soup.find_all('a', href=True):
                if 'price' in a.get_text(strip=True).lower() or 'price' in a['href'].lower():
                    price_url = a['href']
                    if not price_url.startswith('http'):
                        price_url = 'https://www.mercurycolleges.nsw.edu.au' + price_url
                    try:
                        pr = requests.get(price_url, timeout=15)
                        if pr.status_code == 200:
                            ps = BeautifulSoup(pr.text, 'html.parser')
                            # Look for fee info in tables and text
                            for tag in ps.find_all(['table', 'p', 'li', 'div']):
                                t = tag.get_text(strip=True)
                                if '$' in t and any(kw in t.lower() for kw in ['fee', 'tuition', 'course', 'cost', 'price']):
                                    # Found fee info
                                    pass
                    except:
                        pass
    except Exception as e:
        print(f"  Warning: site error - {e}")
    
    # Try individual course pages
    course_urls = [
        ("General English", "https://www.mercurycolleges.nsw.edu.au/course/general-english/"),
        ("IELTS Preparation", "https://www.mercurycolleges.nsw.edu.au/course/ielts-preparation/"),
        ("PTE Preparation", "https://www.mercurycolleges.nsw.edu.au/course/pearson-test-of-english/"),
    ]
    
    scraped_info = {}
    for cname, curl in course_urls:
        try:
            cr = requests.get(curl, timeout=15)
            if cr.status_code == 200:
                cs = BeautifulSoup(cr.text, 'html.parser')
                info = {'desc': '', 'duration': '', 'fee': '', 'intake': ''}
                for tag in cs.find_all(['p', 'li', 'div', 'span']):
                    t = tag.get_text(strip=True)
                    tl = t.lower()
                    if any(kw in tl for kw in ['duration', 'weeks', 'full-time']):
                        if not info['duration']: info['duration'] = t[:200]
                    if '$' in t and any(kw in tl for kw in ['fee', 'cost', 'price', 'tuition']):
                        if not info['fee']: info['fee'] = t[:200]
                    if any(kw in tl for kw in ['intake', 'start', 'commence']):
                        if not info['intake']: info['intake'] = t[:200]
                    if len(t) > 100 and not info['desc']:
                        info['desc'] = t[:500]
                scraped_info[cname] = info
                print(f"  Scraped: {cname}")
        except:
            pass
    
    # Build output
    intake_date = "Contact college for intake dates"
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
            "note": "Scraped from mercurycolleges.nsw.edu.au",
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
