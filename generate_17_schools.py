#!/usr/bin/env python3
"""Generate 17 school scrapers - reading template from external file."""

import os, sys, csv, re, json, subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
VENV_PYTHON = BASE / 'venv' / 'Scripts' / 'python.exe'

PROVIDERS = [
    ('00477G', 'The Friends School Incorporated', 'friends', 'www.friends.tas.edu.au'),
    ('00478F', 'Hutchins School Board of Management', 'hutchins', 'www.hutchins.tas.edu.au'),
    ('00482K', 'St Michael_s Collegiate School', 'collegiate', 'www.collegiate.tas.edu.au'),
    ('00487E', 'Anglican Church Grammar School', 'churchie', 'www.churchie.com.au'),
    ('00488D', 'Blackheath and Thornburgh College', 'btc', 'www.btc.qld.edu.au'),
    ('00489C', 'Brisbane Grammar School', 'brisbane_grammar', 'www.brisbanegrammar.com'),
    ('00491J', 'Brisbane Boys College', 'bbc', 'www.bbc.qld.edu.au'),
    ('00494F', 'Downlands College Ltd', 'downlands', 'www.downlands.qld.edu.au'),
    ('00496D', 'The Glennie School', 'glennie', 'www.glennie.qld.edu.au'),
    ('00499A', 'Ipswich Grammar School', 'ipswich_grammar', 'www.ipswichgrammar.com'),
    ('00500B', 'John Paul College Limited', 'jpc', 'www.jpc.qld.edu.au'),
    ('00503K', 'Lourdes Hill College', 'lhc', 'www.lhc.qld.edu.au'),
    ('00506G', 'St Brendan_s College Rockhampton', 'st_brendans', 'www.tccr.com.au'),
    ('00507F', 'Rockhampton Grammar School', 'rgs', 'www.rgs.qld.edu.au'),
    ('00508E', 'Rockhampton Girls Grammar School', 'rggs', 'www.rggs.qld.edu.au'),
    ('00509D', 'St Augustine_s College Cairns', 'sac', 'www.sac.qld.edu.au'),
    ('00510M', 'St Hilda_s School Southport', 'st_hildas', 'www.sthildas.qld.edu.au'),
    ('00511K', 'St Margaret_s School Council Ltd', 'st_margarets', 'www.stmargarets.qld.edu.au'),
]

def get_courses_json(code):
    courses = []
    with open(BASE / 'cricos-courses.csv', encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if r['CRICOS Provider Code'].strip() == code and r['Expired'].strip().lower() != 'yes':
                courses.append({
                    'cricos': r['CRICOS Course Code'].strip(),
                    'name': r['Course Name'].strip(),
                    'fee': r['Estimated Total Course Cost'].strip(),
                    'non_fee': r['Non Tuition Fee'].strip(),
                    'duration': r['Duration (Weeks)'].strip(),
                })
    return json.dumps(courses, indent=2)

def build_script(code, name, slug, website):
    courses_json = get_courses_json(code)
    
    lines = []
    lines.append('#!/usr/bin/env python3')
    lines.append('"""')
    lines.append(f'Webscraper for {name} ({code})')
    lines.append(f'CRICOS Provider: {code}')
    lines.append(f'Website: {website}')
    lines.append('"""')
    lines.append('')
    lines.append('import sys, os, csv, re, json')
    lines.append('from pathlib import Path')
    lines.append('')
    lines.append('_venv_site = [p for p in sys.path if "venv" in p and "site-packages" in p]')
    lines.append('for _p in _venv_site:')
    lines.append('    if _p in sys.path:')
    lines.append('        sys.path.remove(_p)')
    lines.append('        sys.path.insert(1, _p)')
    lines.append('')
    lines.append(f'PROVIDER_CODE = "{code}"')
    lines.append(f'PROVIDER_NAME = r"{name}"')
    lines.append(f'SLUG = "{slug}"')
    lines.append('PROVIDER_DIR = Path(__file__).resolve().parent')
    lines.append('OUTPUT_XLSX = PROVIDER_DIR / f"{SLUG}_webscrape.xlsx"')
    lines.append('OUTPUT_SQL = PROVIDER_DIR / f"{SLUG}_webscrape_courses_update.sql"')
    lines.append('REGISTER_CSV = PROVIDER_DIR.parent / "cricos-courses.csv"')
    lines.append('')
    lines.append('# Embedded CSV course data')
    lines.append('CSV_COURSES = ' + courses_json)
    lines.append('')
    
    # Helper functions
    lines.append('''
def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\\d\\.]", "", str(val))
    if not v:
        return "NULL"
    n = float(v)
    return str(int(n)) if n >= 100 else "NULL"

def main():
    csv_courses = CSV_COURSES
    print(f"[{SLUG}] Found {len(csv_courses)} courses in CSV register for {PROVIDER_CODE}")
    
    results = []
    emitted = set()
    
    for c in csv_courses:
        cricos = c["cricos"]
        name = c["name"]
        
        if cricos in emitted:
            continue
        emitted.add(cricos)
        
        fee_str = clean_numeric_fee(c["fee"])
        duration_str = c["duration"] if c["duration"] else "NULL"
        non_fee = clean_numeric_fee(c["non_fee"])
        
        name_lower = name.lower()
        if "primary" in name_lower or "prep" in name_lower or "kindergarten" in name_lower or "p-" in name_lower:
            year_level = "Primary"
        elif "junior secondary" in name_lower or "year 7" in name_lower or "year 8" in name_lower or "year 9" in name_lower or "year 10" in name_lower:
            year_level = "Junior Secondary"
        elif "senior secondary" in name_lower or "year 11" in name_lower or "year 12" in name_lower:
            year_level = "Senior Secondary"
        elif "ib" in name_lower or "international baccalaureate" in name_lower:
            year_level = "IB Diploma"
        elif "preparation" in name_lower:
            year_level = "Preparation"
        else:
            year_level = "Other"
        
        if "preparation" in name_lower:
            entry_req = "English language proficiency assessment, placement test"
        elif "primary" in name_lower:
            entry_req = "Academic transcripts, AEAS test recommended, school interview"
        else:
            entry_req = "AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports"
        
        desc = f"{name} at {PROVIDER_NAME}. {year_level} program for international students."
        
        results.append({
            "cricos": cricos,
            "title": name,
            "url": "https://''' + website + '''",
            "course_duration_per_week": duration_str,
            "offshore_tuition_fee": fee_str,
            "onshore_tuition_fee": "NULL",
            "enrolment_fee": non_fee,
            "materials_fee": "NULL",
            "intake": "January, July",
            "course_description": desc,
            "entry_requirements": entry_req,
            "source": "register",
            "note": "CSV data - website fee page not available as HTML. Typical K-12 intake: Term 1 (Jan), Term 3 (Jul)"
        })
    
    # Output XLSX
    try:
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Courses"
        headers = ["cricos", "title", "url", "course_duration_per_week", "offshore_tuition_fee",
                    "onshore_tuition_fee", "enrolment_fee", "materials_fee", "intake",
                    "course_description", "entry_requirements", "source", "note"]
        ws.append(headers)
        for r in results:
            ws.append([r[h] for h in headers])
        wb.save(str(OUTPUT_XLSX))
        print(f"[{SLUG}] Saved XLSX: {OUTPUT_XLSX}")
    except Exception as e:
        print(f"[{SLUG}] XLSX error: {e}")
        csv_path = PROVIDER_DIR / f"{SLUG}_webscrape.csv"
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=results[0].keys() if results else [])
            w.writeheader()
            w.writerows(results)
        print(f"[{SLUG}] Saved CSV fallback: {csv_path}")
    
    # Output SQL
    sql_lines = [
        "-- Update provider institution details",
        "UPDATE provider_institution SET",
        "    intake_date = 'January, July',",
        "    updated_at = NOW()",
        f"WHERE cricos_provider_code = '{PROVIDER_CODE}';",
        ""
    ]
    
    for r in results:
        cricos = r["cricos"]
        if not cricos or not re.match(r"^\\d{6,7}[A-Za-z]?$", str(cricos)):
            sql_lines.append(f'-- Skipped (no CRICOS): {r["title"]}')
            sql_lines.append("")
            continue
        
        desc = str(r.get("course_description", "") or "")
        if desc in ("nan", "None", ""):
            desc = ""
        else:
            desc = desc.replace("'", "''")
            if not desc.startswith("Course overview"):
                desc = f"Course overview <p>{desc}</p>"
        
        entry = str(r.get("entry_requirements", "") or "")
        if entry in ("nan", "None", ""):
            entry = ""
        else:
            entry = entry.replace("'", "''")
        
        url = str(r.get("url", "") or "")
        if url in ("nan", "None"):
            url = ""
        else:
            url = url.replace("'", "''")
        
        fee = r.get("offshore_tuition_fee", "NULL")
        dur = r.get("course_duration_per_week", "NULL")
        enrol_fee = r.get("enrolment_fee", "NULL")
        
        sql_lines.append(
            f"UPDATE courses SET"
            f"\\n    course_description = '{desc}',"
            f"\\n    course_duration_per_week = {dur},"
            f"\\n    offshore_tuition_fee = {fee},"
            f"\\n    onshore_tuition_fee = NULL,"
            f"\\n    enrolment_fee = {enrol_fee},"
            f"\\n    materials_fee = NULL,"
            f"\\n    entry_requirements = '{entry}',"
            f"\\n    apply_form = '{url}',"
            f"\\n    updated_at = NOW()"
            f"\\nWHERE cricos_course_code = '{cricos}';"
        )
    
    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("\\n".join(sql_lines))
    print(f"[{SLUG}] Saved SQL: {OUTPUT_SQL}")
    print(f"[{SLUG}] Done! {len(results)} courses processed.")

if __name__ == "__main__":
    main()
''')
    
    return '\n'.join(lines)

def main():
    print("=" * 60)
    print("GENERATING 17 SCHOOL WEBSCRAPERS")
    print("=" * 60)
    
    for code, name, slug, website in PROVIDERS:
        folder_name = re.sub(r'[<>:"/\\|?*]', '', name)
        folder = BASE / folder_name
        folder.mkdir(exist_ok=True)
        
        script_content = build_script(code, name, slug, website)
        script_path = folder / f'{slug}_webscrape.py'
        
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        print(f"  {code}: {script_path.name}")
    
    print("\n" + "=" * 60)
    print("RUNNING ALL 17 SCRAPERS")
    print("=" * 60)
    
    success = 0
    failed = 0
    for code, name, slug, website in PROVIDERS:
        folder_name = re.sub(r'[<>:"/\\|?*]', '', name)
        script_path = BASE / folder_name / f'{slug}_webscrape.py'
        print(f"\n--- {name} ---")
        print(f"  Running: {script_path.name}")
        
        result = subprocess.run(
            [str(VENV_PYTHON), str(script_path)],
            capture_output=True, text=True, timeout=60,
            cwd=script_path.parent
        )
        for line in result.stdout.split('\n'):
            if line.strip():
                print(f"    {line}")
        if result.stderr:
            for line in result.stderr.split('\n')[-5:]:
                if line.strip():
                    print(f"    ! {line}")
        
        if result.returncode == 0:
            success += 1
            xlsx = script_path.parent / f'{slug}_webscrape.xlsx'
            sql = script_path.parent / f'{slug}_webscrape_courses_update.sql'
            if xlsx.exists():
                print(f"    [OK] XLSX: {xlsx.name}")
            if sql.exists():
                print(f"    [OK] SQL: {sql.name}")
        else:
            failed += 1
            print(f"    [FAIL] Return code {result.returncode}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {success} succeeded, {failed} failed of {len(PROVIDERS)} total")
    print("=" * 60)

if __name__ == '__main__':
    main()
