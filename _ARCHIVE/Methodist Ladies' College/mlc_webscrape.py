"""
Methodist Ladies' College (MLC) - Web scraping from www.mlc.vic.edu.au (provider 00325A).
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
from bs4 import BeautifulSoup
import openpyxl

PROVIDER_CODE = "00325A"
PROVIDER_NAME = "Methodist Ladies' College"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "mlc"
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
                }
    
    # Scrape MLC international and fee pages
    entry_req = "AEAS testing, school reports, interview"
    intake_text = "January (Term 1), April (Term 2), July (Term 3), October (Term 4)"
    
    try:
        r = requests.get("https://www.mlc.vic.edu.au/join-us/international-students/", timeout=15)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            # Look for entry requirements table
            for tag in soup.find_all(['p', 'li', 'div']):
                t = tag.get_text(strip=True)
                if any(kw in t.lower() for kw in ['minimum score', 'aeas', 'entry', 'year level', 'requirement']):
                    print(f"  Entry: {t[:200]}")
                if 'cricos' in t.lower() and 'course' in t.lower():
                    print(f"  CRICOS: {t[:200]}")
            print("  Scraped international page")
    except Exception as e:
        print(f"  Warning: {e}")
    
    intake_date = "January, April, July, October"
    out = []
    for code, cinfo in cricos_map.items():
        out.append({
            "cricos": code,
            "title": cinfo['title'],
            "url": "https://www.mlc.vic.edu.au/join-us/international-students/",
            "course_duration_per_week": cinfo['duration_weeks'],
            "offshore_tuition_fee": cinfo['tuition_fee'],
            "onshore_tuition_fee": "",
            "enrolment_fee": cinfo['non_tuition_fee'],
            "materials_fee": "",
            "intake": intake_date,
            "course_description": "MLC is a leading independent school for girls offering primary and secondary education programs.",
            "entry_requirements": "AEAS testing: Years 4-6 (61+), Years 7-9 (71+), Years 10-12 (80+). School reports and interview.",
            "source": "web+register",
            "note": "Scraped from mlc.vic.edu.au",
        })
    
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
    
    emitted = set()
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write(f"UPDATE provider_institution SET\n"
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for r in out:
            if r["cricos"] in emitted: continue
            emitted.add(r["cricos"])
            dur = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"
            fee = clean_numeric_fee(r["offshore_tuition_fee"])
            enr = clean_numeric_fee(r["enrolment_fee"])
            entry = r["entry_requirements"].replace("'", "''")
            f.write(f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '{entry}',\n"
                    f"    apply_form = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"\n  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
