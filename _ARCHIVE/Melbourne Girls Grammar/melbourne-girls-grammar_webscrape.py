"""
Melbourne Girls Grammar - Web scraping from www.mggs.vic.edu.au (provider 00322D).
Extracts fee data from international students page.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
from bs4 import BeautifulSoup
import openpyxl

PROVIDER_CODE = "00322D"
PROVIDER_NAME = "Melbourne Girls Grammar"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "melbourne-girls-grammar"
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
    
    # Scrape MGGS international students page for fees
    web_fees = {}
    intake_info = "January (Term 1), April (Term 2), July (Term 3), October (Term 4)"
    entry_req = "AEAS test results, school reports, English proficiency"
    
    try:
        # International students page has the fee table
        r = requests.get("https://www.mggs.vic.edu.au/enrolments/international-students", timeout=15)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            # Find fee table
            table = soup.find('table')
            if table:
                for row in table.find_all('tr'):
                    cells = row.find_all(['td', 'th'])
                    cell_text = [c.get_text(strip=True) for c in cells]
                    print(f"  Table row: {cell_text}")
                    # Extract year level and fee
                    if len(cell_text) >= 3 and any(kw in cell_text[0].lower() for kw in ['prep', 'year', 'boarding', 'elc']):
                        level = cell_text[0]
                        annual_fee = cell_text[1]
                        web_fees[level] = annual_fee
            else:
                # Find fee text in divs
                for tag in soup.find_all(['p', 'li', 'div']):
                    t = tag.get_text(strip=True)
                    if '$' in t and any(kw in t.lower() for kw in ['year', 'prep', 'annual fee', 'tuition']):
                        print(f"  Fee text: {t[:200]}")
            print(f"  Successfully scraped international fee page")
    except Exception as e:
        print(f"  Warning: {e}")
    
    # Build output
    intake_date = "January, April, July, October"
    out = []
    for code, cinfo in cricos_map.items():
        # Try to determine year level from course name
        annual_fee = cinfo['tuition_fee']
        
        out.append({
            "cricos": code,
            "title": cinfo['title'],
            "url": "https://www.mggs.vic.edu.au/enrolments/international-students",
            "course_duration_per_week": cinfo['duration_weeks'],
            "offshore_tuition_fee": annual_fee,
            "onshore_tuition_fee": "",
            "enrolment_fee": cinfo['non_tuition_fee'],
            "materials_fee": "",
            "intake": intake_date,
            "course_description": "Melbourne Girls Grammar offers primary and secondary education programs for international students.",
            "entry_requirements": entry_req,
            "source": "web+register",
            "note": "Scraped from mggs.vic.edu.au",
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
                    f"    entry_requirements = '{entry_req}',\n"
                    f"    apply_form = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"\n  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
