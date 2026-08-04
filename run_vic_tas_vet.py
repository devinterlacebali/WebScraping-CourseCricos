"""
Master web scraper for remaining VIC/TAS VET/English/training colleges.
Visits college websites for international fee/entry/intake data.
Generates {slug}_webscrape.xlsx + {slug}_webscrape_courses_update.sql per provider.
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
# PROVIDER DATA - VET/English colleges needing webscrape
# ============================================================
COLLEGES = [
    # Large providers first
    ("00122A", "RMIT University (RMIT)", "rmit", "https://www.rmit.edu.au", "/courses"),
    ("00724G", "Melbourne Polytechnic", "melbourne-polytechnic", "http://www.melbournepolytechnic.edu.au", "/international"),
    ("01331F", "Australian Pacific College", "apc", "https://www.apc.edu.au", "/courses"),
    ("02886G", "Melbourne College of Hair and Beauty", "mcohb", "https://www.mcohb.com.au", "/courses"),
    ("02044E", "VIT (Victorian Institute of Technology)", "vit", "https://www.vit.edu.au", "/courses"),
    ("02506B", "Australian National Institute of Business & Technology", "anibt", "https://www.anibt.vic.edu.au", "/courses"),
    ("03024A", "Melbourne City Institute of Education", "mcie", "https://www.mcie.edu.au", "/courses"),
    ("01218G", "Bendigo TAFE / Kangan Institute", "kangan", "https://www.kangan.edu.au", "/international"),
    ("03312D", "La Trobe College Australia", "la-trobe-college", "https://www.latrobemelbourne.edu.au", "/courses"),
    ("01545C", "MIT - Melbourne Institute of Technology", "mit", "https://www.mit.edu.au", "/courses"),
    ("02992E", "Rhodes College", "rhodes", "https://www.rhodescollege.vic.edu.au", "/courses"),
    ("03831C", "iLearn OZ / MELBOURNE METRO COLLEGE", "ilearn-oz", "https://www.ilearnoz.com.au", "/courses"),
    ("03874C", "West Melbourne Institute of Technology", "wmit", "https://www.wmit.edu.au", "/courses"),
    ("03737A", "Niashi School of Management and Technology", "niashi", "https://www.nsmt.vic.edu.au", "/courses"),
    ("01590J", "Deakin College", "deakin-college", "https://www.deakincollege.edu.au", "/courses"),
    ("03529J", "Mechanical Institute of Training and Technology", "mitt", "https://www.mitt.vic.edu.au", "/courses"),
    ("03723G", "Ruby Institute", "ruby", "https://www.ruby.vic.edu.au", "/courses"),
    ("03642G", "Dolph Business School", "dolph", "https://www.dolphbusinessschool.com.au", "/courses"),
    ("03976H", "MELBOURNE INSTITUTE OF TRAINING AND EDUCATION", "mite", "https://www.mite.edu.au", "/courses"),
    ("03611D", "Zoi Education Pty Ltd", "zoi", "https://www.zoi.vic.edu.au", "/courses"),
    ("04354H", "Victorian Skillls College", "victorian-skills", "https://www.victorianskills.vic.edu.au", "/courses"),
    ("04305F", "Vocational Augment Training", "vat", "https://www.vat.vic.edu.au", "/courses"),
    ("02868J", "Australian Institute of Technical Training", "aitt", "https://www.aitt.vic.edu.au", "/courses"),
    ("03401C", "Max Therapy Institute / MAX English", "max-therapy", "https://www.mti.vic.edu.au", "/courses"),
    ("03592B", "Melbourne City College Australia", "mcca", "https://www.melbournecitycollege.edu.au", "/courses"),
    ("03916J", "Kingsway College Pty Ltd", "kingsway", "https://www.kingswaycollege.vic.edu.au", "/courses"),
    ("02790D", "Hays International College", "hays", "https://www.hic.vic.edu.au", "/courses"),
    ("02961A", "Melbourne College of Further Education", "mcfe", "https://www.mcfe.com.au", "/courses"),
    ("03961D", "Brilliant Institute of Business and Education", "bibe", "https://www.bibe.tas.edu.au", "/courses"),
    ("00898G", "Holmes Institute (Melbourne School of Fashion)", "holmes-institute", "https://www.holmesinstitute.edu.au", "/courses"),
    ("04289A", "Australis Business School", "australis", "https://www.australis.vic.edu.au", "/courses"),
    ("02137M", "ILSC - Australia", "ilsc", "https://www.ilsc.com.au", "/courses"),
    ("02892J", "Institute of Tertiary and Higher Education Australia", "ithea", "https://www.ithea.vic.edu.au", "/courses"),
    ("03560K", "Windsor College Australia", "windsor", "https://www.windsorcollege.edu.au", "/courses"),
    ("03803G", "Lindisfarne Anglican Grammar School", "lindisfarne", "https://www.lindisfarne.nsw.edu.au", "/international"),
    ("03980A", "Federation Academy", "federation-academy", "https://www.federationacademy.edu.au", "/courses"),
    ("03330B", "Macquarie Grammar School", "macquarie-grammar", "https://www.macquariegrammarschool.edu.au", "/international"),
]

def build_vet_script(code, name, slug, website, courses_path):
    intl_url = website.rstrip("/") + courses_path
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
    
    # Try to get website data - course pages, fee info
    entry_req = ""
    intake = ""
    has_website_data = False
    
    try:
        r = requests.get(WEBSITE, timeout=15, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
        if r.status_code == 200:
            text = r.text
            er_match = re.search(r'(?:entry requirement|IELTS|English)[^.]{10,200}\\.', text, re.IGNORECASE | re.DOTALL)
            if er_match:
                entry_req = er_match.group(0).strip()[:300]
            int_match = re.search(r'(?:intake|start date|commence|term)[^.]{10,200}\\.', text, re.IGNORECASE | re.DOTALL)
            if int_match:
                intake = int_match.group(0).strip()[:200]
            if er_match or int_match:
                has_website_data = True
            print("  Homepage: " + str(r.status_code) + " (" + str(len(text)) + "b)")
    except Exception as e:
        print("  Homepage error: " + str(e))
    
    # Also try the courses page
    try:
        r2 = requests.get(INTL_URL, timeout=15, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
        if r2.status_code == 200:
            text2 = r2.text
            if not entry_req:
                er_match = re.search(r'(?:entry requirement|IELTS|English)[^.]{10,200}\\.', text2, re.IGNORECASE | re.DOTALL)
                if er_match:
                    entry_req = er_match.group(0).strip()[:300]
            if not intake:
                int_match = re.search(r'(?:intake|start date|commence|term)[^.]{10,200}\\.', text2, re.IGNORECASE | re.DOTALL)
                if int_match:
                    intake = int_match.group(0).strip()[:200]
            print("  Courses page: " + str(r2.status_code) + " (" + str(len(text2)) + "b)")
    except Exception as e:
        print("  Courses page error: " + str(e))
    
    rows = []
    for cricos_code, reg_rec in reg.items():
        name_raw = reg_rec.get("Course Name", "").strip()
        duration_weeks = re.sub(r"[^\\d]", "", reg_rec.get("Duration (Weeks)","") or "")
        csv_fee = reg_rec.get("Estimated Total Course Cost","") or ""
        csv_fee = clean_numeric_fee(csv_fee.replace("$","")) if csv_fee else "NULL"
        enr_fee = clean_numeric_fee(reg_rec.get("Non Tuition Fee",""))
        
        rows.append({
            "cricos": cricos_code,
            "title": name_raw,
            "url": INTL_URL,
            "course_duration_per_week": duration_weeks if duration_weeks else "NULL",
            "offshore_tuition_fee": csv_fee,
            "onshore_tuition_fee": "NULL",
            "enrolment_fee": enr_fee,
            "materials_fee": "NULL",
            "intake": intake,
            "course_description": "<h4>Course overview</h4><p>" + name_raw + "</p>" if name_raw else "",
            "entry_requirements": "<h4>Entry Requirements</h4><p>" + entry_req + "</p>" if entry_req else "",
            "source": "website" if has_website_data else "register",
            "note": "Data from CSV+website homepage" if has_website_data else "CSV-driven - website limited"
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
    for code, name, slug, website, courses_path in COLLEGES:
        folder_name = re.sub(r'[<>:"/\\|?*]', '', name).strip()
        folder = ensure_folder(folder_name)
        script_path = folder / f"{slug}_webscrape.py"
        
        if not script_path.exists():
            print(f"\n--- Creating {name} ({code}) ---")
            script_content = build_vet_script(code, name, slug, website, courses_path)
            script_path.write_text(script_content, encoding='utf-8')
            print(f"  Script: {script_path}")
        
        print(f"\n--- Running {name} ({code}) ---")
        result = run_script(script_path, folder)
        print(f"  STDOUT: {result.stdout[:500] if result.stdout else '(empty)'}")
        if result.stderr:
            print(f"  STDERR: {result.stderr[:300]}")
        
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
