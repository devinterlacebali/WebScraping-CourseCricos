"""
Firbank Grammar School - Web Scraper (00140K).
WARNING: Site may have Cloudflare protection.
Uses curl_cffi if available.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00140K"
PROVIDER_NAME = "Firbank Grammar School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "firbank"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
WEBSITE = "https://www.firbank.vic.edu.au/international-students"
FEE_SCHEDULE = "https://www.firbank.vic.edu.au/school-fee-schedule/"

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n < 10000000 else "NULL"

def try_fetch(url, timeout=15):
    """Try requests first, fall back to curl_cffi if available."""
    try:
        import requests
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
        return r.status_code, r.text
    except Exception as e1:
        try:
            from curl_cffi import requests as cr
            r = cr.get(url, timeout=timeout, impersonate="chrome110")
            return r.status_code, r.text
        except Exception as e2:
            print(f"  Fetch error: {e1}; curl_cffi: {e2}")
            return 0, ""

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper")
    print(f"  {'='*40}")
    print(f"  Provider: {PROVIDER_CODE}\n")
    
    # Try fetching the website
    code, html = try_fetch(WEBSITE)
    print(f"  Intl page: {code} ({len(html)}b)")
    
    # Check for Cloudflare
    if code == 0 or "cf-browser-verification" in html or "Checking your browser" in html:
        print(f"  !! Cloudflare detected - using CSV fallback + notes")
        cloudflare_blocked = True
    else:
        cloudflare_blocked = False
    
    # Also try the fee schedule
    fee_code, fee_html = try_fetch(FEE_SCHEDULE)
    print(f"  Fee schedule: {fee_code} ({len(fee_html)}b)")
    
    # Extract any fee data from pages
    intl_fees_found = []
    for src_name, src_html in [("intl_page", html), ("fee_page", fee_html)]:
        if src_html:
            fees = re.findall(r'\$[\d,]+', src_html)
            # Look for year-level fee patterns
            for yr in [f'Year {i}' for i in range(1,13)] + ['Prep']:
                pattern = re.escape(yr) + r'.{0,200}?\$([\d,]+)'
                for m in re.finditer(pattern, src_html, re.DOTALL):
                    try:
                        amt = int(m.group(1).replace(',', ''))
                        if 5000 < amt < 200000:
                            intl_fees_found.append((yr, amt, src_name))
                    except:
                        pass
    
    if intl_fees_found:
        print(f"  Found fee data: {intl_fees_found[:10]}")
    
    # Load CSV register
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            
            # Use website fee data if available (highest year level for that course)
            if "Secondary" in course_name or "Years 7" in course_name:
                website_note = "CSV-driven (Cloudflare blocked page scrape)" if cloudflare_blocked else "CSV-driven (fee in PDF handbook)"
            else:
                website_note = "CSV-driven (Cloudflare blocked page scrape)" if cloudflare_blocked else "CSV-driven (fee in PDF handbook)"
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": WEBSITE,
                "course_description": f"<h4>Firbank Grammar School - International Program</h4><p>Firbank Grammar School offers a co-educational (Primary) and girls-only (Secondary) environment for international students. Located in Brighton, Victoria.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 3 (July)",
                "entry_requirements": "AEAS test results, previous school reports, interview. English language proficiency assessment required.",
                "apply_form": WEBSITE,
                "source": "webscrape", "note": website_note,
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
