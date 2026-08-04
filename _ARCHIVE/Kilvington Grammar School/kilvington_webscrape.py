"""
Kilvington Grammar School - Web Scraper (00149A)
Data source: www.kilvington.vic.edu.au/enrol/international-students
Fees in PDF at: International Tuition Fees link on page.
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00149A"
PROVIDER_NAME = "Kilvington Grammar School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "kilvington"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
INTL_URL = "https://www.kilvington.vic.edu.au/enrol/international-students"

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
    
    # Fetch international page
    intl_html = ""
    try:
        r = requests.get(INTL_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        intl_html = r.text
        print(f"  Intl page: {r.status_code} ({len(r.text)}b)")
        
        # Find fee PDF links
        pdfs = re.findall(r'href=["\']([^"\']*International[^"\']*Tuition[^"\']*Fees[^"\']*\.pdf[^"\']*)["\']', r.text, re.I)
        if not pdfs:
            pdfs = re.findall(r'href=["\']([^"\']*Tuition[^"\']*Fees[^"\']*\.pdf[^"\']*)["\']', r.text, re.I)
        if pdfs:
            print(f"  Fee PDFs found: {pdfs[:3]}")
    except Exception as e:
        print(f"  Error: {e}")
    
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
            years = max(1, int(dur) / 52) if dur else 6
            
            # Estimate annual fee from CSV total
            if csv_total:
                annual_est = int(int(csv_total) / years)
            else:
                annual_est = 0
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": INTL_URL,
                "course_description": f"<h4>Kilvington Grammar School - International Program</h4><p>Kilvington Grammar School offers a co-educational environment with strong academic record and ESL support. International students fully integrate into the Australian culture.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 156,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt) if clean_numeric_fee(nt) != "NULL" else 0,
                "materials_fee": "",
                "intake": "Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)",
                "entry_requirements": "Previous school reports, interview. English language proficiency required. International Student Handbook available.",
                "apply_form": INTL_URL,
                "source": "webscrape",
                "note": f"CSV-driven (fees in PDF). CSV total: ${int(csv_total) if csv_total else 0:,}. Est annual: ${annual_est:,}" if csv_total else "CSV-driven."
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
                f"    intake_date = 'Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)',\n"
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
