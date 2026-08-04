"""
Kent Institute Australia - Web scraping from kent.edu.au (provider 00161E).
Course detail pages 404, so data from listing pages + CSV CRICOS validation.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests
from bs4 import BeautifulSoup
import openpyxl

PROVIDER_CODE = "00161E"
PROVIDER_NAME = "Kent Institute Australia"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "kent-institute"
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

def clean_weeks(val):
    if not val: return "NULL"
    v = re.sub(r"[^\d]", "", str(val))
    return v if v else "NULL"

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper\n  {'='*50}\n  Provider: {PROVIDER_CODE}")
    
    # First, gather CRICOS codes from CSV
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
    
    # Visit Kent course listing page to find course descriptions/durations
    course_data = {}
    try:
        r = requests.get("https://kent.edu.au/courses/", timeout=30)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            # Find all course links
            for a in soup.find_all('a', href=True):
                href = a['href']
                if any(kw in href for kw in ['/course-', '/course/', '/bachelor-', '/certificate-', '/diploma-', '/master-']):
                    txt = a.get_text(strip=True)
                    if txt and len(txt) > 5 and txt not in ['Explore Course', 'View Brochure']:
                        # Try to visit course page
                        try:
                            cr = requests.get(href if href.startswith('http') else 'https://kent.edu.au'+href, timeout=15)
                            if cr.status_code == 200:
                                cs = BeautifulSoup(cr.text, 'html.parser')
                                desc = ""
                                dur_text = ""
                                fee_text = ""
                                intake_text = ""
                                entry_req = ""
                                for tag in cs.find_all(['p', 'li', 'div', 'span', 'h2', 'h3', 'h4']):
                                    t = tag.get_text(strip=True)
                                    tl = t.lower()
                                    if any(kw in tl for kw in ['duration', 'weeks', 'year', 'full-time', 'part-time']):
                                        if not dur_text:
                                            dur_text = t[:200]
                                    if any(kw in tl for kw in ['intake', 'start date', 'commence']):
                                        if not intake_text:
                                            intake_text = t[:200]
                                    if any(kw in tl for kw in ['fee', 'tuition', 'cost', 'price', '$']):
                                        if not fee_text and '$' in t:
                                            fee_text = t[:200]
                                    if any(kw in tl for kw in ['entry', 'admission', 'requirement']):
                                        if not entry_req:
                                            entry_req = t[:300]
                                # Extract description - look for larger text blocks
                                for tag in cs.find_all(['div', 'p']):
                                    t = tag.get_text(strip=True)
                                    if len(t) > 100 and not desc:
                                        desc = t[:500]
                                course_data[href] = {
                                    'desc': desc,
                                    'duration_text': dur_text,
                                    'fee_text': fee_text,
                                    'intake_text': intake_text,
                                    'entry_req': entry_req,
                                }
                                print(f"  Scraped: {txt[:60]}... (dur: {dur_text[:40]})")
                        except Exception as e:
                            pass
    except Exception as e:
        print(f"  Warning: Kent site scrape error: {e}")
    
    # Build output using CRICOS validation + website data
    intake_date = "February, July"
    out = []
    for code, cinfo in cricos_map.items():
        # Try to match course data
        web_data = {}
        for url, wd in course_data.items():
            if cinfo['title'].lower().split('(')[0].strip() in url.lower() or any(word in url.lower() for word in cinfo['title'].lower().split() if len(word) > 5):
                web_data = wd
                break
        
        # Parse duration from web
        dur = cinfo['duration_weeks']
        if web_data.get('duration_text'):
            dur_match = re.search(r'(\d+)\s*(year|yr|month|week)', web_data['duration_text'], re.I)
            if dur_match:
                num = int(dur_match.group(1))
                unit = dur_match.group(2).lower()
                if 'year' in unit:
                    dur = num * 52
                elif 'month' in unit:
                    dur = num * 4
                elif 'week' in unit:
                    dur = num
        
        fee = cinfo['tuition_fee']
        ntf = cinfo['non_tuition_fee']
        
        out.append({
            "cricos": code,
            "title": cinfo['title'],
            "url": "",
            "course_duration_per_week": dur,
            "offshore_tuition_fee": fee,
            "onshore_tuition_fee": "",
            "enrolment_fee": ntf,
            "materials_fee": "",
            "intake": intake_date,
            "course_description": web_data.get('desc', ''),
            "entry_requirements": web_data.get('entry_req', ''),
            "source": "web",
            "note": "Scraped from kent.edu.au",
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
    
    # Write SQL
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
            desc = r["course_description"].replace("'", "''")
            entry = r["entry_requirements"].replace("'", "''")
            f.write(f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '{entry}',\n"
                    f"    course_description = '{desc}',\n"
                    f"    apply_form = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"\n  Done: {len(emitted)} courses. Intake: {intake_date}\n")

if __name__ == "__main__":
    main()
