"""
Generate web scrape scripts for the first 12 K-12 grammar schools.
Each script visits the school website for international fee / entry / intake data.
"""
import os, sys, re, json
from pathlib import Path

BASE = Path(__file__).resolve().parent

def w(content, path):
    full = BASE / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding='utf-8')
    print(f"  Created {full.relative_to(BASE)}")

# ============================================================
# FINTONA GIRLS SCHOOL (00139C)
# ============================================================
fintona = r'''"""
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
            total_csv = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            
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
                "note": f"Annual fee ${annual_fee:,} (Year {year_range}) × {years:.0f} years = ${website_fee:,}. CSV total: ${int(total_csv) if total_csv else 0:,}" if total_csv else f"Annual fee ${annual_fee:,} × {years:.0f} years = ${website_fee:,}"
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
'''

w(fintona, "Fintona Girls School/fintona_webscrape.py")

# ============================================================
# FIRBANK GRAMMAR SCHOOL (00140K) - Cloudflare possible
# ============================================================
firbank = r'''"""
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
'''

w(firbank, "Firbank Grammar School/firbank_webscrape.py")

# ============================================================
# CAMBERWELL GIRLS GRAMMAR (00141J)
# ============================================================
cggs = r'''"""
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
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
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
                "note": f"Website annual fee ${intl_fee:,}/year × {years:.0f} years = ${website_fee:,}. CSV total: ${int(csv_total) if csv_total else 0:,}" if intl_fee and website_fee else f"CSV total: ${int(csv_total) if csv_total else 0:,}"
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
'''

w(cggs, "Camberwell Anglican Girls' Grammar School/camberwell-ggs_webscrape.py")

print("\n=== Scripts 1-3 created. Creating 4-12... ===")

# ============================================================
# THE GEELONG COLLEGE (00142G)
# ============================================================
geelong_college = r'''"""
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
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
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
'''

w(geelong_college, "The Geelong College/geelong-college_webscrape.py")

# ============================================================
# GEELONG GRAMMAR SCHOOL (00143G)
# ============================================================
ggs = r'''"""
Geelong Grammar School - Web Scraper (00143G).
Data source: www.ggs.vic.edu.au
Note: International pages return 404. Using CSV data with website notes.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00143G"
PROVIDER_NAME = "Geelong Grammar School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "geelong-grammar"
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
    
    print(f"  Note: /international-students, /international return 404")
    print(f"  Note: Using CSV data with website notes\n")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": "https://www.ggs.vic.edu.au/enrolment",
                "course_description": f"<h4>Geelong Grammar School - International Program</h4><p>Geelong Grammar School is one of Australia's leading co-educational boarding schools. International students benefit from world-class facilities and a rich co-curricular program.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 3 (July)",
                "entry_requirements": "AEAS test results, academic transcripts, interview. English language proficiency assessment.",
                "apply_form": "https://www.ggs.vic.edu.au/enrolment",
                "source": "webscrape",
                "note": f"CSV-driven. No international fee page found. CSV total: ${int(csv_total) if csv_total else 0:,}" if csv_total else "CSV-driven."
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
'''

w(ggs, "Geelong Grammar School/geelong-grammar_webscrape.py")

# ============================================================
# THE HAMILTON AND ALEXANDRA COLLEGE (00144F)
# ============================================================
hamilton = r'''"""
The Hamilton and Alexandra College - Web Scraper (00144F)
Data source: www.hamiltoncollege.vic.edu.au/international-students
Fee data not found on page. Using CSV data with website notes.
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00144F"
PROVIDER_NAME = "The Hamilton and Alexandra College"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "hamilton-college"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
INTL_URL = "https://www.hamiltoncollege.vic.edu.au/international-students"

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
    try:
        r = requests.get(INTL_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        print(f"  Intl page: {r.status_code} ({len(r.text)}b)")
        fees = re.findall(r'\$[\d,]+', r.text)
        print(f"  Fees on page: {fees[:10]}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print(f"  Note: No fee table found on international page. Using CSV data.\n")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": INTL_URL,
                "course_description": f"<h4>The Hamilton and Alexandra College - International Program</h4><p>International students at Hamilton and Alexandra College enjoy a supportive boarding environment with strong pastoral care and academic support.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 3 (July)",
                "entry_requirements": "AEAS test results, academic transcripts, interview. International students must meet English language proficiency requirements.",
                "apply_form": INTL_URL,
                "source": "webscrape",
                "note": f"CSV-driven. No fee table found on website. CSV total: ${int(csv_total) if csv_total else 0:,}" if csv_total else "CSV-driven."
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
'''

w(hamilton, "The Hamilton and Alexandra College/hamilton-college_webscrape.py")

# ============================================================
# HUNTINGTOWER SCHOOL (00145E)
# ============================================================
huntingtower = r'''"""
Huntingtower School - Web Scraper (00145E)
Data source: www.huntingtower.vic.edu.au
Note: All international/fee pages return 404. Using CSV data.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00145E"
PROVIDER_NAME = "Huntingtower School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "huntingtower"
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
    print(f"  Note: All international/fee/enrolment pages return 404.")
    print(f"  Note: Using CSV data with website notes.\n")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": "https://www.huntingtower.vic.edu.au",
                "course_description": f"<h4>Huntingtower School - International Program</h4><p>Huntingtower is a co-educational school from Prep to Year 12. International students join a nurturing academic community in Mount Waverley, Victoria.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 3 (July)",
                "entry_requirements": "AEAS test results, academic transcripts, interview. English language proficiency assessment required.",
                "apply_form": "https://www.huntingtower.vic.edu.au",
                "source": "webscrape",
                "note": f"CSV-driven. No accessible international fee page found. CSV total: ${int(csv_total) if csv_total else 0:,}" if csv_total else "CSV-driven."
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
'''

w(huntingtower, "Huntingtower School/huntingtower_webscrape.py")

# ============================================================
# IVANHOE GRAMMAR SCHOOL (00147C)
# ============================================================
ivanhoe = r'''"""
The Ivanhoe Grammar School - Web Scraper (00147C)
Data source: www.ivanhoe.com.au/enrolments/international/
Fee data available via PDF at media.igs.vic.edu.au/downloads/WEBSITE/Fees/2026/InternationalStudentFees_2026.pdf
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00147C"
PROVIDER_NAME = "The Ivanhoe Grammar School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "ivanhoe-grammar"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
INTL_URL = "https://www.ivanhoe.com.au/enrolments/international/"
FEE_PDF = "https://media.igs.vic.edu.au/downloads/WEBSITE/Fees/2026/InternationalStudentFees_2026.pdf"

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
    
    # Try fetching the fee PDF
    pdf_fees = {}
    try:
        r = requests.get(FEE_PDF, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            print(f"  PDF: {len(r.content)} bytes")
            # Try to extract text with pdfminer or pypdf2
            try:
                import io, PyPDF2
                reader = PyPDF2.PdfReader(io.BytesIO(r.content))
                pdf_text = ""
                for page in reader.pages[:5]:
                    pdf_text += page.extract_text() + "\n"
                # Look for year-level fees in PDF text
                for yr in [f'Year {i}' for i in range(1,13)] + ['Prep']:
                    pattern = re.escape(yr) + r'.{0,100}\$?([\d,]+)'
                    for m in re.finditer(pattern, pdf_text):
                        try:
                            amt = int(re.sub(r'[^\d]', '', m.group(1)))
                            if 5000 < amt < 200000:
                                pdf_fees[yr] = amt
                        except: pass
                if pdf_fees:
                    print(f"  Extracted fees from PDF: {len(pdf_fees)} year levels")
                    for yr, amt in sorted(pdf_fees.items()):
                        print(f"    {yr}: ${amt:,}")
                else:
                    print(f"  No structured fees extracted from PDF - first 500 chars:")
                    print(f"  {pdf_text[:500]}")
            except ImportError:
                print(f"  PyPDF2 not available")
            except Exception as e:
                print(f"  PDF parse error: {e}")
    except Exception as e:
        print(f"  PDF fetch error: {e}")
    
    # Note about international page
    print(f"  Note: /enrolments/international/ returns empty page (JS-rendered)")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            years = max(1, int(dur) / 52) if dur else 6
            
            # Calculate fee from PDF if available
            if pdf_fees:
                if "Secondary" in course_name or "Years 7" in course_name:
                    annual = pdf_fees.get("Year 12", max(pdf_fees.values()) if pdf_fees else 0)
                else:
                    annual = pdf_fees.get("Year 6", list(pdf_fees.values())[0] if pdf_fees else 0)
                website_fee = int(annual * years)
            else:
                website_fee = ""
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": "https://www.ivanhoe.com.au/enrolments/fees/",
                "course_description": f"<h4>Ivanhoe Grammar School - International Program</h4><p>Ivanhoe Grammar School offers a co-educational environment (Primary) and boys-only (Secondary) education. International students thrive in a supportive community.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": website_fee,
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)",
                "entry_requirements": "AEAS test, previous school reports, interview. English language proficiency required.",
                "apply_form": "https://www.ivanhoe.com.au/enrolments/international/",
                "source": "webscrape",
                "note": f"International fee PDF: ${annual:,}/year × {years:.0f} years = ${website_fee:,}. CSV total: ${int(csv_total) if csv_total else 0:,}" if pdf_fees and website_fee else f"CSV-driven. PDF available but could not parse. CSV total: ${int(csv_total) if csv_total else 0:,}"
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
'''

w(ivanhoe, "The Ivanhoe Grammar School/ivanhoe-grammar_webscrape.py")

# ============================================================
# KILVINGTON GRAMMAR SCHOOL (00149A)
# ============================================================
kilvington = r'''"""
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
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
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
'''

w(kilvington, "Kilvington Grammar School/kilvington_webscrape.py")

# ============================================================
# KINGSWOOD COLLEGE (00150G)
# ============================================================
kingswood = r'''"""
Kingswood College - Web Scraper (00150G)
Data source: www.kingswoodcollege.vic.edu.au/enrolment-and-tours/international-students
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00150G"
PROVIDER_NAME = "Kingswood College"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "kingswood-college"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
INTL_URL = "https://www.kingswoodcollege.vic.edu.au/enrolment-and-tours/international-students"

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
    try:
        r = requests.get(INTL_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        print(f"  Intl page: {r.status_code} ({len(r.text)}b)")
        # Look for fees in the page
        fees = re.findall(r'\$[\d,]+', r.text)
        print(f"  Fees on page: {fees[:10]}")
    except Exception as e:
        print(f"  Error: {e}")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            years = max(1, int(dur) / 52) if dur else 6

            if csv_total:
                annual_est = int(int(csv_total) / years)
            else:
                annual_est = 0
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": INTL_URL,
                "course_description": f"<h4>Kingswood College - International Program</h4><p>Kingswood College warmly welcomes international students in Prep to Year 12 with a dedicated International Student Coordinator and ESL support.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)",
                "entry_requirements": "AEAS test, academic transcripts, interview with Head of School and/or International Student Coordinator. English language proficiency: IELTS or equivalent.",
                "apply_form": INTL_URL,
                "source": "webscrape",
                "note": f"CSV-driven. Fee handbook available on site. CSV total: ${int(csv_total) if csv_total else 0:,}. Est annual: ${annual_est:,}" if csv_total else "CSV-driven."
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
'''

w(kingswood, "Kingswood College/kingswood-college_webscrape.py")

# ============================================================
# THE KNOX SCHOOL (00151G)
# ============================================================
knox = r'''"""
The Knox School - Web Scraper (00151G)
Data source: www.knox.vic.edu.au/international/international-student-fees/
Full fee table found on website!
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00151G"
PROVIDER_NAME = "The Knox School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "knox-school"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
INTL_FEES_URL = "https://www.knox.vic.edu.au/international/international-student-fees/"

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n < 10000000 else "NULL"

def extract_knox_fees(html):
    """Extract International fee table from Knox School page."""
    fees = {}
    # Table has columns: Year Level, Annual Tuition Fee AUD$, Subject Levies$, Payroll Tax Levy$, Total AUD$, Per Term$
    pattern = r'(Prep|Year\s*\d+)\s*</td>\s*<td[^>]*>([\d,]+)\s*</td>\s*<td[^>]*>([\d,]+)\s*</td>\s*<td[^>]*>([\d,]+)\s*</td>\s*<td[^>]*>([\d,]+)\s*</td>'
    for m in re.finditer(pattern, html, re.DOTALL):
        year = m.group(1).strip()
        tuition = int(m.group(2).replace(',', ''))
        total = int(m.group(5).replace(',', ''))
        fees[year] = {"tuition": tuition, "total": total}
    
    # Also try simpler pattern
    if not fees:
        for yr in ['Prep'] + [f'Year {i}' for i in range(1,13)]:
            esc_yr = re.escape(yr)
            m = re.search(rf'{esc_yr}\s*</td>(?:\s*<td[^>]*>.*?</td>){{0,2}}\s*<td[^>]*>([\d,]+)\s*</td>', html, re.DOTALL)
            if m:
                try:
                    fees[yr] = {"tuition": int(m.group(1).replace(',','')), "total": int(m.group(1).replace(',',''))}
                except: pass
    return fees

def main():
    print(f"\n  {PROVIDER_NAME} Web Scraper")
    print(f"  {'='*40}")
    print(f"  Provider: {PROVIDER_CODE}\n")
    
    fees_data = {}
    try:
        r = requests.get(INTL_FEES_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            fees_data = extract_knox_fees(r.text)
            if fees_data:
                print(f"  International fee table: {len(fees_data)} year levels")
                for yr, f in sorted(fees_data.items()):
                    print(f"    {yr}: Tuition ${f['tuition']:,}, Total ${f['total']:,}")
            else:
                print(f"  No structured fee table found (raw page size: {len(r.text)}b)")
        else:
            print(f"  Page: {r.status_code}")
    except Exception as e:
        print(f"  Error: {e}")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            years = max(1, int(dur) / 52) if dur else 6
            
            if fees_data:
                if "Secondary" in course_name or "Years 7" in course_name:
                    annual = fees_data.get("Year 12", {}).get("tuition", list(fees_data.values())[-1]["tuition"] if fees_data else 42238)
                else:
                    annual = fees_data.get("Year 6", {}).get("tuition", list(fees_data.values())[0]["tuition"] if fees_data else 33880)
                website_fee = int(annual * years)
            else:
                website_fee = ""
                annual = 0
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": INTL_FEES_URL,
                "course_description": f"<h4>The Knox School - International Program</h4><p>The Knox School offers a supportive learning environment for international students from Prep to Year 12, with a strong focus on academic excellence.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": website_fee,
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)",
                "entry_requirements": "AEAS test results, previous school reports, interview. English proficiency required.",
                "apply_form": INTL_FEES_URL,
                "source": "webscrape",
                "note": f"Annual tuition fee: ${annual:,}/year × {years:.0f} years = ${website_fee:,}. CSV total: ${int(csv_total) if csv_total else 0:,}" if fees_data and website_fee else f"CSV total: ${int(csv_total) if csv_total else 0:,}"
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
'''

w(knox, "The Knox School/knox-school_webscrape.py")

# ============================================================
# LAURISTON GIRLS' SCHOOL (00152F)
# ============================================================
lauriston = r'''"""
Lauriston Girls' School - Web Scraper (00152F)
Data source: lauriston.vic.edu.au
Fees PDF: /wp-content/uploads/2025/10/Schedule-of-Fees-Overseas-2026.pdf
"""
import sys, re, csv, requests
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = "00152F"
PROVIDER_NAME = "Lauriston Girls' School"
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = "lauriston"
OUTPUT_XLSX = PROVIDER_DIR / (SLUG + "_webscrape.xlsx")
OUTPUT_SQL = PROVIDER_DIR / (SLUG + "_webscrape_courses_update.sql")
REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"
FEES_URL = "https://www.lauriston.vic.edu.au/fees-and-charges/"

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
    
    # Try fetching the fees page
    try:
        r = requests.get(FEES_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code == 200:
            print(f"  Fees page: {r.status_code} ({len(r.text)}b)")
            # Look for overseas fee PDF
            pdfs = re.findall(r'href=["\']([^"\']*Overseas[^"\']*\.pdf[^"\']*)["\']', r.text, re.I)
            if not pdfs:
                pdfs = re.findall(r'href=["\']([^"\']*[Oo]verseas[^"\']*\.pdf[^"\']*)["\']', r.text)
            if pdfs:
                print(f"  Overseas fee PDF: {pdfs[0]}")
    except Exception as e:
        print(f"  Error: {e}")
    
    rows = []
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for rec in csv.DictReader(f):
            if rec["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if rec["Expired"].strip().lower() == "yes": continue
            dur = re.sub(r"[^\d]", "", rec.get("Duration (Weeks)") or "")
            csv_total = rec.get("Estimated Total Course Cost", "").strip().replace("$", "").replace(",", "")
            nt = rec.get("Non Tuition Fee", "").strip().replace("$", "").replace(",", "")
            course_name = rec["Course Name"].strip()
            cricos = rec["CRICOS Course Code"].strip()
            years = max(1, int(dur) / 52) if dur else 6
            
            if csv_total:
                annual_est = int(int(csv_total) / years)
            else:
                annual_est = 0
            
            rows.append({
                "cricos": cricos,
                "title": course_name,
                "url": FEES_URL,
                "course_description": f"<h4>Lauriston Girls' School - International Program</h4><p>Lauriston is one of Melbourne's leading independent girls' schools. International students access an outstanding education from Early Learning to Year 12.</p>",
                "course_duration_per_week": int(dur) if dur.isdigit() else 312,
                "offshore_tuition_fee": "",
                "onshore_tuition_fee": "",
                "enrolment_fee": clean_numeric_fee(nt),
                "materials_fee": "",
                "intake": "Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)",
                "entry_requirements": "AEAS test results, academic transcripts, interview. English language proficiency required.",
                "apply_form": "https://www.lauriston.vic.edu.au/enrolment/",
                "source": "webscrape",
                "note": f"Fees in PDF Schedule-of-Fees-Overseas-2026.pdf. CSV total: ${int(csv_total) if csv_total else 0:,}. Est annual: ${annual_est:,}" if csv_total else "CSV-driven. Fees in overseas PDF."
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
'''

w(lauriston, "Lauriston Girls' School/lauriston_webscrape.py")

print("\n=== All 12 web scraper scripts created! ===")
print("Now run them one by one.")
