"""
The Ivanhoe Grammar School — Web scrape (00147C).
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00147C"
SLUG = "ivanhoe-grammar"
PROVIDER_DIR = Path(__file__).resolve().parent
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
SITE = "https://www.ivanhoe.com.au/enrolments/international/"

def clean_fee(v):
    if v is None or str(v).strip().lower() in ("nan","null","n/a","","none","-"): return "NULL"
    n = re.sub(r"[^\d.]","",str(v))
    return str(int(float(n))) if n and float(n)>=100 else "NULL"

def main():
    print(f"\n  Ivanhoe Grammar Web Scraper\n  {'='*40}\n  Provider: {PROVIDER_CODE}\n")
    try:
        r = requests.get(SITE, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        print(f"  Site: {r.status_code} ({len(r.text)}b)")
    except Exception as e:
        print(f"  Site unreachable: {e}")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]","", rec.get("Duration (Weeks)") or "")
            fee = rec.get("Tuition Fee","").replace("$","").replace(",","")
            nt = rec.get("Non Tuition Fee","").replace("$","").replace(",","")
            rows.append({
                "cricos": rec["CRICOS Course Code"].strip(), "course_title": rec["Course Name"].strip(),
                "url": SITE, "course_duration_per_week": int(dur) if dur.isdigit() else "",
                "offshore_tuition_fee": "" if clean_fee(fee)=="NULL" else clean_fee(fee),
                "onshore_tuition_fee": "", "enrolment_fee": "" if clean_fee(nt)=="NULL" else clean_fee(nt),
                "materials_fee": "", "intake": "February, July",
                "course_description": "<h4>Course Overview</h4><p>Ivanhoe Grammar School - International Student Program. Fees listed in PDF International Fee Schedule.</p>",
                "entry_requirements": "AEAS test results required. Interview with Director of International Students. For Year 11 entry, IELTS 6.0 or equivalent.",
                "apply_form": "https://www.ivanhoe.com.au/enrolments/",
                "source": "register", "note": "Fees published in PDF International Fee Schedule not HTML. Using CSV register data.",
            })
    
    pd.DataFrame(rows).to_excel(OUTPUT_XLSX, index=False)
    emitted = set()
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write(f"UPDATE provider_institution SET intake_date = 'February, July', updated_at = NOW() WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for r in rows:
            if r["cricos"] in emitted: continue
            emitted.add(r["cricos"])
            dur = str(r["course_duration_per_week"]) if r["course_duration_per_week"] else "NULL"
            fee = clean_fee(r["offshore_tuition_fee"]); enr = clean_fee(r["enrolment_fee"])
            entry = (r.get("entry_requirements") or "").replace("'", "''")
            desc = (r.get("course_description") or "").replace("'", "''")
            f.write(f"UPDATE courses SET course_description = '{desc}', course_duration_per_week = {dur}, offshore_tuition_fee = {fee}, enrolment_fee = {enr}, entry_requirements = '{entry}', apply_form = '{r.get('apply_form','')}', updated_at = NOW() WHERE cricos_course_code = '{r['cricos']}';\n\n")
    print(f"  Courses: {len(rows)}\n     xlsx -> {OUTPUT_XLSX.name}\n     sql  -> {OUTPUT_SQL.name}\n  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
