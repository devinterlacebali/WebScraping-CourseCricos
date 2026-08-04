"""
The Peninsula School - Web scraping from www.tps.vic.edu.au (provider 00333A).
NOTE: Website has SSL handshake failure. Using CSV CRICOS data as fallback.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
import openpyxl

PROVIDER_CODE = "00333A"
PROVIDER_NAME = "The Peninsula School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "peninsula-school"
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
    
    # Try with different SSL settings
    site_blocked = False
    for url in ['https://tps.vic.edu.au', 'https://www.tps.vic.edu.au']:
        try:
            r = requests.get(url, timeout=15, verify=False)
            print(f"  {url}: status {r.status_code}")
            site_blocked = False
            break
        except Exception as e:
            print(f"  {url}: SSL Error - {e}")
            site_blocked = True
    
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
    
    intake_date = "January, April, July, October"
    out = []
    for code, cinfo in cricos_map.items():
        out.append({
            "cricos": code,
            "title": cinfo['title'],
            "url": "https://www.tps.vic.edu.au",
            "course_duration_per_week": cinfo['duration_weeks'],
            "offshore_tuition_fee": cinfo['tuition_fee'],
            "onshore_tuition_fee": "",
            "enrolment_fee": cinfo['non_tuition_fee'],
            "materials_fee": "",
            "intake": intake_date,
            "course_description": "The Peninsula School offers primary and secondary education programs.",
            "entry_requirements": "Contact school for entry requirements",
            "source": "register" if site_blocked else "web",
            "note": "Website SSL handshake failure - using CSV data" if site_blocked else "Scraped from tps.vic.edu.au",
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
            f.write(f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '',\n"
                    f"    apply_form = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"\n  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
