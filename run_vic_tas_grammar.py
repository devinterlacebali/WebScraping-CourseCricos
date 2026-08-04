"""
Master web scraper for remaining VIC/TAS grammar schools and K-12 providers.
Visits each school website for international fee/entry/intake data.
Generates {slug}_webscrape.xlsx + {slug}_webscrape_courses_update.sql per school.
"""
import sys, re, csv, os, json, subprocess
from pathlib import Path

PROJECT = Path(__file__).resolve().parent
VENV_PY = PROJECT / "venv" / "Scripts" / "python.exe"

def ensure_folder(name):
    folder = PROJECT / name
    folder.mkdir(exist_ok=True)
    return folder

# ============================================================
# PROVIDER DATA - Grammar/K-12 schools needing webscrape
# ============================================================
SCHOOLS = [
    ("00557G", "Ballarat Clarendon College", "ballarat-clarendon", "https://www.clarendon.vic.edu.au", "/enrolment/international-students"),
    ("00558F", "Loyola College", "loyola", "https://www.loyola.vic.edu.au", "/international-students"),
    ("00577C", "Strathcona Baptist Girls Grammar School", "strathcona", "https://www.strathcona.vic.edu.au", "/enrolment/international"),
    ("00578B", "Heathdale Christian College", "heathdale", "https://www.heathdale.vic.edu.au", "/international-students"),
    ("00624A", "Scotch College", "scotch-vic", "https://www.scotch.vic.edu.au", "/admissions/international"),
    ("00649C", "Haileybury College", "haileybury", "https://www.haileybury.vic.edu.au", "/enrolment/international"),
    ("00650K", "Launceston Church Grammar School", "launceston-grammar", "https://www.lcgs.tas.edu.au", "/international"),
    ("00871G", "St Aloysius College", "st-aloysius", "https://www.aloysius.vic.edu.au", "/international-students"),
    ("00974A", "Ivanhoe Girls Grammar School", "ivanhoe-girls", "https://www.ivanhoegirls.vic.edu.au", "/enrolment/international"),
    ("00977J", "Melbourne Grammar School", "melbourne-grammar", "https://www.mgs.vic.edu.au", "/enrolment/fees"),
    ("00978G", "Gilson College", "gilson", "https://www.gilsoncollege.vic.edu.au", "/international-students"),
    ("01022G", "Korowa Anglican Girls' School", "korowa", "https://www.korowa.vic.edu.au", "/enrolment/international"),
    ("01097M", "Nazareth College", "nazareth", "https://www.nazareth.vic.edu.au", "/international-students"),
    ("01100K", "Girton Grammar School", "girton", "https://www.girton.vic.edu.au", "/international"),
    ("01220B", "Mackillop Catholic Regional College", "mackillop", "https://www.mackillop.vic.edu.au", "/enrolment/international"),
    ("01376D", "Alphington Grammar School", "alphington", "https://www.alphington.vic.edu.au", "/international"),
    ("01502C", "Kardinia International College", "kardinia", "https://www.kardinia.vic.edu.au", "/international"),
    ("01894D", "Christway College", "christway", "https://christway.vic.edu.au", "/enrolment/international"),
    ("02184D", "Caroline Chisholm Catholic College", "caroline-chisholm", "https://www.cccc.vic.edu.au", "/international"),
    ("02448G", "Alia College", "alia", "https://www.alia.vic.edu.au", "/fees"),
    ("03182J", "Beaconhills College", "beaconhills", "https://www.beaconhills.vic.edu.au", "/enrolment/international"),
    ("03298G", "Genazzano FCJ College", "genazzano", "https://www.genazzano.vic.edu.au", "/admissions/international"),
    ("03423G", "Oakleigh Grammar", "oakleigh-grammar", "https://www.oakleighgrammar.vic.edu.au", "/international-students"),
    ("04313F", "Siena College", "siena", "https://www.siena.vic.edu.au", "/enrolment/international"),
    ("04366D", "Sacre Coeur", "sacre-coeur", "https://sacrecoeur.vic.edu.au", "/international"),
    ("00477G", "The Friends' School", "friends-tas", "https://www.friends.tas.edu.au", "/enrolment/international"),
    ("00478F", "The Hutchins School", "hutchins", "https://www.hutchins.tas.edu.au", "/enrolment/international"),
    ("00482K", "St Michael's Collegiate School", "collegiate-tas", "https://www.collegiate.tas.edu.au", "/enrolment/international"),
]

def build_script(code, name, slug, website, intl_path):
    intl_url = website.rstrip("/") + intl_path
    lines = []
    lines.append('"""')
    lines.append(f'{name} - Web Scraper ({code}).')
    lines.append(f'Data sources: {intl_url}')
    lines.append('"""')
    lines.append('import sys, re, csv, requests')
    lines.append('from pathlib import Path')
    lines.append("sys.path = [p for p in sys.path if 'hermes' not in p.lower()]")
    lines.append('')
    lines.append(f'PROVIDER_CODE = \"{code}\"')
    lines.append(f'PROVIDER_NAME = \"{name}\"')
    lines.append('PROVIDER_DIR = Path(__file__).resolve().parent')
    lines.append(f'SLUG = \"{slug}\"')
    lines.append(f'OUTPUT_XLSX = PROVIDER_DIR / (SLUG + \"_webscrape.xlsx\")')
    lines.append(f'OUTPUT_SQL = PROVIDER_DIR / (SLUG + \"_webscrape_courses_update.sql\")')
    lines.append(f'REGISTER_CSV = PROVIDER_DIR.parent / \"cricos-courses.csv\"')
    lines.append(f'INTL_URL = \"{intl_url}\"')
    lines.append(f'WEBSITE = \"{website}\"')
    lines.append('')
    lines.append('''
def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan","null","n/a","","none","-",""):
        return "NULL"
    v = re.sub(r"[^\\d.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n.is_integer() else str(n)

def load_register():
    reg = {}
    with open(REGISTER_CSV, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["CRICOS Provider Code"].strip() != PROVIDER_CODE: continue
            if r["Expired"].strip().lower() == "yes": continue
            reg[r["CRICOS Course Code"].strip()] = r
    return reg

def main():
    print("  " + PROVIDER_NAME + " Web Scraper (" + PROVIDER_CODE + ")")
    print("  " + "="*50)
    
    reg = load_register()
    print("  Courses in register: " + str(len(reg)))
    
    fees = {}
    entry_req = ""
    intake = ""
    
    try:
        urls_to_try = [INTL_URL, WEBSITE.rstrip("/") + "/fees", 
                       WEBSITE.rstrip("/") + "/enrolment/fees",
                       WEBSITE.rstrip("/") + "/admissions",
                       WEBSITE.rstrip("/") + "/international-students/fees",
                       WEBSITE.rstrip("/") + "/enrolment/international-students"]
        for url in urls_to_try:
            r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            if r.status_code == 200:
                text = r.text
                # Extract fee info
                fbodies = re.findall(r'(?:Year|Prep|Primary|Secondary|Junior|Senior).{0,30}?\\$\\s*[\\d,]+', text, re.IGNORECASE)
                for fb in fbodies:
                    m = re.search(r'(Year\\s*\\d+[\\s-]*\\d*|Prep|Primary|Secondary|Junior|Senior).{0,30}?\\$\\s*([\\d,]+)', fb, re.IGNORECASE)
                    if m:
                        yr = m.group(1).strip()
                        amt = int(m.group(2).replace(",",""))
                        fees[yr] = amt
                
                er_match = re.search(r'(?:entry requirement|IELTS|AEAS|English)[^.]{10,200}\\.', text, re.IGNORECASE | re.DOTALL)
                if er_match:
                    entry_req = er_match.group(0).strip()[:300]
                
                int_match = re.search(r'(?:intake|start date|commence|term)[^.]{10,200}\\.', text, re.IGNORECASE | re.DOTALL)
                if int_match:
                    intake = int_match.group(0).strip()[:200]
                    
                print("  " + url + ": " + str(r.status_code) + " (" + str(len(text)) + "b)")
                if fees:
                    break
    except Exception as e:
        print("  Fetch error: " + str(e))
    
    rows = []
    for cricos_code, reg_rec in reg.items():
        name_raw = reg_rec.get("Course Name", "").strip()
        duration_weeks = re.sub(r"[^\\d]", "", reg_rec.get("Duration (Weeks)","") or "")
        csv_fee = reg_rec.get("Estimated Total Course Cost","") or ""
        csv_fee = clean_numeric_fee(csv_fee.replace("$","")) if csv_fee else "NULL"
        
        total_fee = "NULL"
        years = 0
        if duration_weeks and duration_weeks.isdigit():
            years = max(1, round(int(duration_weeks) / 52))
        if fees:
            annual_fees = list(fees.values())
            if annual_fees:
                avg_annual = max(annual_fees)
                if years:
                    total_fee = str(int(avg_annual) * years)
                else:
                    total_fee = str(int(avg_annual))
        else:
            total_fee = csv_fee
        
        enr_fee = clean_numeric_fee(reg_rec.get("Non Tuition Fee",""))
        
        rows.append({
            "cricos": cricos_code,
            "title": name_raw,
            "url": INTL_URL,
            "course_duration_per_week": duration_weeks if duration_weeks else "NULL",
            "offshore_tuition_fee": total_fee,
            "onshore_tuition_fee": "NULL",
            "enrolment_fee": enr_fee,
            "materials_fee": "NULL",
            "intake": intake,
            "course_description": "<h4>Course overview</h4><p>" + name_raw + "</p>" if name_raw else "",
            "entry_requirements": "<h4>Entry Requirements</h4><p>" + entry_req + "</p>" if entry_req else "",
            "source": "website" if fees else "register",
            "note": "Fees from website fee table" if fees else "CSV fallback - no fee table found"
        })
    
    # Write XLSX
    import openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Courses"
    headers = ["cricos","title","url","course_duration_per_week","offshore_tuition_fee",
               "onshore_tuition_fee","enrolment_fee","materials_fee","intake",
               "course_description","entry_requirements","source","note"]
    ws.append(headers)
    for row in rows:
        ws.append([row[h] for h in headers])
    wb.save(str(OUTPUT_XLSX))
    print("  XLSX: " + str(len(rows)) + " rows -> " + str(OUTPUT_XLSX))
    
    # Write SQL
    sql_lines = []
    sql_lines.append("-- Update provider institution details")
    sql_lines.append("UPDATE provider_institution SET")
    sql_lines.append("    intake_date = '" + intake.replace("'", "''") + "',")
    sql_lines.append("    updated_at = NOW()")
    sql_lines.append("WHERE cricos_provider_code = '" + PROVIDER_CODE + "';")
    
    for row in rows:
        desc_esc = row["course_description"].replace("'", "''") if row["course_description"] else ""
        entry_esc = row["entry_requirements"].replace("'", "''") if row["entry_requirements"] else ""
        sql_lines.append("")
        sql_lines.append("-- " + row['title'])
        sql_lines.append("UPDATE courses SET")
        sql_lines.append("    course_description = '" + desc_esc + "',")
        
        dw = row["course_duration_per_week"]
        if dw != "NULL":
            sql_lines.append("    course_duration_per_week = " + dw + ",")
        else:
            sql_lines.append("    course_duration_per_week = NULL,")
        
        sql_lines.append("    offshore_tuition_fee = " + row['offshore_tuition_fee'] + ",")
        sql_lines.append("    onshore_tuition_fee = " + row['onshore_tuition_fee'] + ",")
        sql_lines.append("    enrolment_fee = " + row['enrolment_fee'] + ",")
        sql_lines.append("    materials_fee = " + row['materials_fee'] + ",")
        sql_lines.append("    entry_requirements = '" + entry_esc + "',")
        sql_lines.append("    updated_at = NOW()")
        sql_lines.append("WHERE cricos_course_code = '" + row['cricos'] + "';")
    
    sql_content = "\\n".join(sql_lines)
    OUTPUT_SQL.write_text(sql_content, encoding="utf-8")
    print("  SQL: " + str(len(rows)) + " statements -> " + str(OUTPUT_SQL))
    print("  Done!")

if __name__ == "__main__":
    main()
''')
    return '\n'.join(lines)

def run_script(script_path, folder):
    result = subprocess.run(
        [str(VENV_PY), str(script_path)],
        capture_output=True, text=True, timeout=60,
        cwd=str(folder)
    )
    return result

def main():
    results = []
    for code, name, slug, website, intl_path in SCHOOLS:
        folder_name = re.sub(r'[<>:"/\\|?*]', '', name).strip()
        folder = ensure_folder(folder_name)
        script_path = folder / f"{slug}_webscrape.py"
        
        if not script_path.exists():
            print(f"\n--- Creating {name} ({code}) ---")
            script_content = build_script(code, name, slug, website, intl_path)
            script_path.write_text(script_content, encoding='utf-8')
            print(f"  Script: {script_path}")
        
        print(f"\n--- Running {name} ({code}) ---")
        result = run_script(script_path, folder)
        print(f"  STDOUT: {result.stdout[:1000] if result.stdout else '(empty)'}")
        if result.stderr:
            print(f"  STDERR: {result.stderr[:500]}")
        
        xlsx = folder / f"{slug}_webscrape.xlsx"
        sql = folder / f"{slug}_webscrape_courses_update.sql"
        has_xlsx = xlsx.exists()
        has_sql = sql.exists()
        results.append((code, name, slug, has_xlsx, has_sql))
        print(f"  Status: {'X' if has_xlsx else ' '} XLSX {'X' if has_sql else ' '} SQL")
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    ok = sum(1 for r in results if r[3] and r[4])
    for r in results:
        mark = "OK" if r[3] and r[4] else "FAIL"
        print(f"  [{mark}] {r[0]} | {r[1][:45]}")
    print(f"Total: {len(results)} | Successful: {ok} | Failed: {len(results)-ok}")

if __name__ == "__main__":
    main()
