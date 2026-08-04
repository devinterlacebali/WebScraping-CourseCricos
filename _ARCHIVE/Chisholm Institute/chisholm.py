"""
Chisholm Institute scraper — www.chisholm.edu.au.

CSV-driven (31 courses, provider 00881F). SQL standard Deakin/JCU.
"""
import os, sys, re
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
import csv

PROVIDER_CODE = '00881F'
PROVIDER_NAME = 'Chisholm Institute'
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = 'chisholm'
OUTPUT_XLSX = PROVIDER_DIR / f'{SLUG}.xlsx'
OUTPUT_SQL = PROVIDER_DIR / f'{SLUG}_courses_update.sql'

MONTH_ORDER = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n >= 100 else "NULL"

def main():
    print(f'\n  {PROVIDER_NAME} Scraper')
    print(f'  {"="*40}')
    print(f'  Provider: {PROVIDER_CODE}')

    # Load CSV
    csv_path = PROVIDER_DIR.parent / 'cricos-courses.csv'
    rows = []
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if not row or len(row) < 3: continue
            if row[0].strip() != PROVIDER_CODE: continue
            title = row[3].strip() if len(row) > 3 else ''
            cricos = row[2].strip()
            fee = row[20].strip().replace('$','').replace(',','') if len(row) > 20 and row[20].strip() not in ('','-') else ''
            dur = row[19].strip() if len(row) > 19 and row[19].strip() not in ('','-') else ''
            rows.append({
                'cricos': cricos, 'title': title,
                'offshore_tuition_fee': fee,
                'course_duration_per_week': dur,
            })

    print(f'  CSV courses: {len(rows)}')

    # Build intake
    intake_date = 'February, July'

    # Write XLSX
    out = []
    for r in rows:
        fee = clean_numeric_fee(r['offshore_tuition_fee'])
        dur = r['course_duration_per_week'] if r['course_duration_per_week'] and re.match(r'^\d+', r['course_duration_per_week']) else ''
        out.append({
            'cricos': r['cricos'], 'title': r['title'], 'url': '',
            'course_duration_per_week': int(dur) if dur and dur.isdigit() else '',
            'offshore_tuition_fee': '' if fee == 'NULL' else fee,
            'onshore_tuition_fee': '', 'enrolment_fee': '', 'materials_fee': '',
            'intake': intake_date,
            'course_description': '', 'entry_requirements': '',
            'source': 'register', 'note': 'from CRICOS register (CSV-driven, no SSR pages)',
        })
    df = pd.DataFrame(out)
    df.to_excel(OUTPUT_XLSX, index=False)
    print(f'     xlsx -> {OUTPUT_XLSX.name}')

    # Write SQL
    emitted = set()
    with open(OUTPUT_SQL, 'w', encoding='utf-8') as f:
        f.write('-- Update provider institution details\n'
                'UPDATE provider_institution SET\n'
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")

        for r in rows:
            cricos = r['cricos']
            if not cricos or not re.match(r'^\d{6,7}[A-Za-z]?$', cricos): continue
            if cricos in emitted: continue
            emitted.add(cricos)
            dur = r['course_duration_per_week'] if r['course_duration_per_week'] and r['course_duration_per_week'].isdigit() else 'NULL'
            fee = clean_numeric_fee(r['offshore_tuition_fee'])
            f.write(f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = NULL,\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '',\n"
                    f"    apply_form = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{cricos}';\n\n")

    print(f'     sql  -> {OUTPUT_SQL.name}')
    print(f'     Courses with CRICOS: {len(emitted)}')
    print(f'  {PROVIDER_NAME} scraper complete.\n')

if __name__ == '__main__':
    main()
