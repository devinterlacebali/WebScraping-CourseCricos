"""
Fintona Girls School - Web Scraper (00139C).
Data source: www.fintona.vic.edu.au/enrolment/fees
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00139C"
PROVIDER_NAME = "Fintona Girls School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "fintona"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
FEES_URL = "https://www.fintona.vic.edu.au/enrolment/fees"
INTL_URL = "https://www.fintona.vic.edu.au/enrolment/"

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def extract_fees(html):
    """Extract international fee table from Fintona fees page."""
    # Find the International Students 2026 table section
    intl_section = re.search(r'Annual Fees International Students 2026(.*?)(?:<h[23]|$)', html, re.DOTALL | re.IGNORECASE)
    if not intl_section:
        return None
    section = intl_section.group(1)
    # Extract year-level fees: pattern "Year X" followed by a dollar amount
    fees = {}
    for m in re.finditer(r'(Prep|Year\s*\d+)[^\$]*?\$(\d[\d,]+)', section, re.IGNORECASE):
        year = m.group(1).strip()
        fee = int(m.group(2).replace(',', ''))
        fees[year] = fee
    return fees

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper")
    print(f"  {'='*40}")
    print(f"  Provider: {PROVIDER_CODE}\n")
    
    # Fetch fees page
    try:
        r = requests.get(FEES_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
        fees_data = extract_fees(r.text) if r.status_code == 200 else None
        print(f"  Fees page: {r.status_code} ({len(r.text)}b)")
        if fees_data:
            print(f"  Found international fee table with {len(fees_data)} year levels")
            for yr, amt in sorted(fees_data.items()):
                print(f"    {yr}: ${amt:,}")
    except Exception as e:
        print(f"  Fees page error: {e}")
        fees_data = None
    
    # Load CSV register
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_fee = rec.get("Tuition Fee", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            total_csv_str = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            total_csv = int(float(total_csv_str)) if total_csv_str else 0
            
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            
            # Determine annual fee from website based on course
            # Secondary (Years 7-12): use Year 12 fee $59,270 × 6 = $355,620
            # Primary (P-6): use Year 6 fee $46,580 × 7 = $326,060
            if "Secondary" in course_name or "Years 7" in course_name:
                annual_fee = fees_data.get("Year 12", 59270) if fees_data else 59270
                years = max(1, int(dur) / 52) if dur else 6
                website_fee = int(annual_fee * years)
                entry_req = 'AEAS test and interview. Minimum English proficiency required.'
                year_range = "7-12"
            else:
                annual_fee = fees_data.get("Year 6", 46580) if fees_data else 46580
                years = max(1, int(dur) / 52) if dur else 7
                website_fee = int(annual_fee * years)
                entry_req = 'AEAS test and interview. Minimum English proficiency required.'
                year_range = "P-6"
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": FEES_URL,
                "course_description": f"<h4>Fintona Girls School - International Program</h4><p>Fintona offers a quality education for international students in {year_range}. The school provides a supportive learning environment with ESL support.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": website_fee,
                "onshore_tuition_fee": "",
                "enrolment_fee": 1800,
                "materials_fee": "",
                "intake": "Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)",
                "entry_requirements": entry_req,
                "apply_form": "https://www.fintona.vic.edu.au/enrolment",
                "source": "webscrape",
                "note": f"Annual fee ${annual_fee:,} (Year {year_range}) × {years:.0f} years = ${website_fee:,}. CSV total: ${total_csv:,}" if total_csv else f"Annual fee ${annual_fee:,} × {years:.0f} years = ${website_fee:,}"
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
                    f"    course_description = '<h4>Course overview</h4><p>{desc}</p>',\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '<h4>Entry Requirements</h4><p>{entry}</p>',\n"
                    f"    apply_form = '{r['apply_form']}',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    print(f"     xlsx -> {OUTPUT_XLSX.name}")
    print(f"     sql  -> {OUTPUT_SQL.name}")
    print(f"  Done: {len(emitted)} courses.\n")

if __name__ == "__main__":
    main()
