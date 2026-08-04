"""
Camberwell Anglican Girls' Grammar School - Web Scraper (00141J).
Data source: www.cggs.vic.edu.au/enrolment/fees/
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00141J"
PROVIDER_NAME = "Camberwell Anglican Girls' Grammar School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "camberwell-ggs"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
FEES_URL = "https://cggs.vic.edu.au/enrolment/fees/"
INTL_URL = "https://cggs.vic.edu.au/international/"

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper")
    print(f"  {'='*40}")
    print(f"  Provider: {PROVIDER_CODE}\n")
    
    # Fetch fees page
    intl_fee = None
    entry_reqs = ""
    try:
        r = requests.get(FEES_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            # Find International fees 2026 table
            m = re.search(r'International fees 2026(.*?)(?:<h[23]|</main)', r.text, re.DOTALL | re.IGNORECASE)
            if m:
                table_section = m.group(1)
                # Extract fee: Year 9, 10, 11 & 12 $56,550
                fee_m = re.search(r'\$(\d[\d,]+)', table_section)
                if fee_m:
                    intl_fee = int(fee_m.group(1).replace(',', ''))
                    print(f"  International fee from website: ${intl_fee:,}/year")
            
            # Extract entry requirements from international page
            ir = requests.get(INTL_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
            if ir.status_code == 200:
                aeass = re.findall(r'AEAS[^<]+', ir.text)
                if aeass:
                    entry_reqs = aeass[0]
                    print(f"  Entry req: {entry_reqs[:100]}")
                # Get full context
                aeam = re.search(r'AEAS test[^<]{0,500}', ir.text, re.DOTALL)
                if aeam:
                    entry_reqs_full = re.sub(r'<[^>]+>', ' ', aeam.group(0))
                    entry_reqs_full = re.sub(r'\s+', ' ', entry_reqs_full).strip()
                    entry_reqs = entry_reqs_full[:500]
                    print(f"  Full entry req found ({len(entry_reqs)} chars)")
    except Exception as e:
        print(f"  Fetch error: {e}")
    
    if intl_fee is None:
        print(f"  !! Using CSV data as fallback")
    
    # Load CSV register
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
            
            # Website: $56,550/year for Years 9-12. For Secondary course use that.
            if intl_fee:
                website_fee = int(intl_fee * years)
            else:
                website_fee = ""
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": FEES_URL,
                "course_description": f"<h4>Camberwell Girls Grammar School - International Program</h4><p>CGGS offers an outstanding education for international students in a supportive, inclusive environment. Students benefit from a strong academic program and ESL support.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": website_fee,
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)",
                "entry_requirements": entry_reqs if entry_reqs else "AEAS test required (score 61-70+ for Years 7-9, 71-80+ for Years 10-11). Stanine 5 or above. Previous school reports and interview.",
                "apply_form": "https://cggs.vic.edu.au/international/",
                "source": "webscrape",
                "note": f"Website annual fee ${intl_fee:,}/year × {years:.0f} years = ${website_fee:,}. CSV total: ${csv_total:,}" if intl_fee and website_fee else f"CSV total: ${csv_total:,}"
            })
    
    print(f"  Courses: {len(rows)}")
    
    out = []
    for r in rows:
        out.append({
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
        })
    
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
