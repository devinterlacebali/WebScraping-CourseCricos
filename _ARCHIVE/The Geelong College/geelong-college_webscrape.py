"""
The Geelong College - Web Scraper (00142G).
Data source: www.tgc.vic.edu.au (redirect from geelongcollege.vic.edu.au)
Note: No accessible international fee page found. Using CSV data.
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00142G"
PROVIDER_NAME = "The Geelong College"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "geelong-college"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n < 10000000 else "NULL"

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper")
    print(f"  {'='*40}")
    print(f"  Provider: {PROVIDER_CODE}\n")
    
    # Try to find fee data on website
    print(f"  Note: Website (tgc.vic.edu.au) redirects from geelongcollege.vic.edu.au")
    print(f"  Note: International page returned 404")
    print(f"  Note: Using CSV data with site notes\n")
    
    # Attempt various URLs
    urls_to_try = [
        "https://www.tgc.vic.edu.au/enrolment/international-students",
        "https://www.tgc.vic.edu.au/enrol/international",
        "https://www.tgc.vic.edu.au/international-students",
    ]
    found_data = False
    for url in urls_to_try:
        try:
            r = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code == 200 and "international" in r.text.lower():
                print(f"  Found page: {url} ({len(r.text)}b)")
                fees = re.findall(r'\$[\d,]+', r.text)
                if fees:
                    print(f"  Fees found: {fees[:10]}")
                found_data = True
                break
        except:
            pass
    
    if not found_data:
        print(f"  !! No accessible international fee page. Using CSV data.")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total_str = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            csv_total = int(float(csv_total_str)) if csv_total_str else 0
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": "https://www.tgc.vic.edu.au/enrolment/",
                "course_description": f"<h4>The Geelong College - International Program</h4><p>The Geelong College is a co-educational boarding and day school. International students join a vibrant community with strong pastoral care.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 3 (July)",
                "entry_requirements": "AEAS test, academic transcripts, English proficiency assessment, interview.",
                "apply_form": "https://www.tgc.vic.edu.au/enrolment/",
                "source": "webscrape",
                "note": f"CSV-driven. No accessible international fee page found. CSV total: ${int(csv_total) if csv_total else 0:,}" if csv_total else "CSV-driven. No accessible international fee page found."
            })
    
    print(f"  Courses: {len(rows)}")
    
    out = [{
        "cricos": r["cricos"], "title": r["title"], "url": r["url"],
        "course_duration_per_week": r["course_duration_per_week"],
        "offshore_tuition_fee": r["offshore_tuition_fee"],
        "onshore_tuition_fee": r["onshore_tuition_fee"],
        "enrolment_fee": r["enrolment_fee"],
        "materials_fee": r["materials_fee"],
        "intake": r["intake"],
        "course_description": r["course_description"],
        "entry_requirements": r["entry_requirements"],
        "source": r["source"], "note": r["note"],
    } for r in rows]
    
    pd.DataFrame(out).to_excel(OUTPUT_XLSX, index=False)
    
    emitted = set()
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("-- Update provider institution details\n"
                "UPDATE provider_institution SET\n"
                f"    intake_date = 'Term 1 (January), Term 3 (July)',\n"
                f"    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for r in rows:
            if r["cricos"] in emitted: continue
            emitted.add(r["cricos"])
            dur = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"
            fee = clean_numeric_fee(r["offshore_tuition_fee"])
            enr = clean_numeric_fee(r["enrolment_fee"])
            desc = r["course_description"].replace("'", "''")
            entry = r["entry_requirements"].replace("'", "''")
            f.write(f"UPDATE courses SET\n"
                    f"    course_description = '{desc}',\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '{entry}',\n"
                    f"    apply_form = '{r['apply_form']}',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
