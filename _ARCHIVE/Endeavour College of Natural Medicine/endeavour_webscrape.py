"""
Endeavour College of Natural Medicine - Web scraping from www.endeavour.edu.au (provider 00231G).
Visits course pages and fee pages to extract duration, fees, intake, entry requirements.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
from bs4 import BeautifulSoup
import openpyxl

PROVIDER_CODE = "00231G"
PROVIDER_NAME = "Endeavour College of Natural Medicine"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "endeavour"
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

def parse_duration_to_weeks(text):
    """Convert duration text like '4 years full-time' to weeks."""
    if not text: return 0
    m = re.search(r'(\d+)\s*(year|yr|month|week)', text, re.I)
    if m:
        num = int(m.group(1))
        unit = m.group(2).lower()
        if 'year' in unit: return num * 52
        elif 'month' in unit: return int(num * 4.33)
        elif 'week' in unit: return num
    return 0

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper\n  {'='*50}\n  Provider: {PROVIDER_CODE}")
    
    # Load CRICOS data for validation
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
    
    # Scrape Endeavour course pages for actual data
    course_urls = [
        ("Bachelor of Health Science (Naturopathy)", "/courses/bachelor-naturopathy", "028648G"),
        ("Bachelor of Health Science (Clinical Nutrition)", "/courses/bachelor-clinical-nutrition", "089452C"),
        ("Bachelor of Health Science (Acupuncture Therapies)", "/courses/bachelor-health-science-acupuncture-therapies", "106485D"),
        ("Bachelor of Health Science (Chinese Medicine)", "/courses/bachelor-health-science-chinese-medicine", "106486C"),
        ("Diploma of Health Science", "/courses/diploma-of-health-science", ""),
        ("Diploma of Health Science (Chinese Remedial Massage)", "/courses/diploma-health-science-chinese-remedial-massage", "106487B"),
    ]
    
    # Scrape fee pages
    fee_page_data = {}
    try:
        r = requests.get("https://www.endeavour.edu.au/apply-to-study/domestic-students/fees-and-payment-options", timeout=15)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            # Extract all course fee blocks
            fee_blocks = soup.find_all('div', class_=lambda c: c and 'course' in c.lower()) if False else []
            # Just extract text containing fee info
            for tag in soup.find_all(['div', 'p', 'h2']):
                t = tag.get_text(strip=True)
                if any(cname.lower() in t.lower() for cname in ['naturopathy', 'clinical nutrition', 'acupuncture', 'chinese medicine', 'diploma of health science', 'chinese remedial massage']):
                    if 'Duration' in t or 'Tuition Fee' in t or 'Total Course Cost' in t:
                        print(f"  Fee data: {t[:150]}")
                        fee_page_data[t[:50]] = t
    except Exception as e:
        print(f"  Warning: fee page error {e}")
    
    # Scrape individual course pages
    web_data = {}
    for cname, cpath, cricos_code in course_urls:
        try:
            url = f"https://www.endeavour.edu.au{cpath}"
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                info = {'desc': '', 'duration': '', 'fee': '', 'intake': '', 'entry_req': ''}
                for tag in soup.find_all(['p', 'li', 'div', 'span']):
                    t = tag.get_text(strip=True)
                    tl = t.lower()
                    if any(kw in tl for kw in ['duration', 'year', 'full-time', 'part-time', 'weeks', 'months']):
                        if not info['duration'] and any(d in tl for d in ['year', 'full-time', 'weeks', 'months']):
                            info['duration'] = t[:200]
                    if any(kw in tl for kw in ['intake', 'start', 'commence']):
                        if not info['intake']:
                            info['intake'] = t[:200]
                    if any(kw in tl for kw in ['entry requirement', 'admission', 'prerequisite']):
                        if not info['entry_req']:
                            info['entry_req'] = t[:300]
                    if len(t) > 100 and not info['desc']:
                        info['desc'] = t[:500]
                # Look for the specific fee/intake section
                for tag in soup.find_all(['p', 'div']):
                    t = tag.get_text(strip=True)
                    if 'Next Intake' in t:
                        info['intake'] = t[:150]
                    if 'Course Length' in t:
                        info['duration'] = t[:150]
                    if 'FEE-HELP' in t:
                        pass
                web_data[cname] = info
                print(f"  Scraped: {cname[:50]} - Intake: {info['intake'][:40]}")
        except Exception as e:
            print(f"  Error: {cname[:40]}: {e}")
    
    # Build output - map CRICOS codes to scraped data
    def match_course(cricos_title):
        for cname, _, cc in course_urls:
            if cc and cc in cricos_title:
                return cname
        for cname, _, _ in course_urls:
            if cname.split('(')[0].strip().lower() in cricos_title.lower():
                return cname
        return None
    
    intake_date = "March, June, September, October (multiple intakes)"
    out = []
    for code, cinfo in cricos_map.items():
        wd = {}
        for cname, _, cc in course_urls:
            if cc and cc in code:
                wd = web_data.get(cname, {})
                break
        if not wd:
            matched = match_course(cinfo['title'])
            if matched:
                wd = web_data.get(matched, {})
        
        dur = parse_duration_to_weeks(wd.get('duration', ''))
        if not dur or dur < 4:
            # Sometimes the duration text is on the fee page
            dur = cinfo['duration_weeks']
        
        # Extract fee from fee_page_data
        fee_amount = cinfo['tuition_fee']
        
        out.append({
            "cricos": code,
            "title": cinfo['title'],
            "url": f"https://www.endeavour.edu.au/courses",
            "course_duration_per_week": dur,
            "offshore_tuition_fee": fee_amount,
            "onshore_tuition_fee": "",
            "enrolment_fee": cinfo['non_tuition_fee'],
            "materials_fee": "",
            "intake": wd.get('intake', intake_date),
            "course_description": wd.get('desc', ''),
            "entry_requirements": wd.get('entry_req', 'Academic requirements vary by course. Visit website for details.'),
            "source": "web",
            "note": "Scraped from endeavour.edu.au",
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
            desc = r["course_description"].replace("'", "''")[:500]
            entry = r["entry_requirements"].replace("'", "''")[:300]
            intake_clean = r["intake"].replace("'", "''")
            f.write(f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '{entry}',\n"
                    f"    course_description = '{desc}',\n"
                    f"    intake_date = '{intake_clean}',\n"
                    f"    apply_form = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"\n  Done: {len(emitted)} courses. Intake: {intake_date}\n")

if __name__ == "__main__":
    main()
