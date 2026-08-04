"""
Menzies Institute of Technology — CSV-driven (provider 02815M, 18 courses).
No Cloudflare. No course sitemap (WordPress). Strategy: CSV-driven.
"""
import sys, re, csv
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = '02815M'
PROVIDER_NAME = 'Menzies Institute of Technology'
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = 'menzies'
OUTPUT_XLSX = PROVIDER_DIR / f'{SLUG}.xlsx'
OUTPUT_SQL = PROVIDER_DIR / f'{SLUG}_courses_update.sql'
REGISTER_CSV = PROVIDER_DIR.parent / 'cricos-courses.csv'

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n >= 100 else "NULL"

def main():
    print(f'\n  {PROVIDER_NAME} Scraper\n  {"="*40}\n  Provider: {PROVIDER_CODE}')
    rows = []
    with open(REGISTER_CSV, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if r['CRICOS Provider Code'].strip() != PROVIDER_CODE: continue
            if r['Expired'].strip().lower() == 'yes': continue
            dur = re.sub(r'[^\d]', '', r.get('Duration (Weeks)') or '')
            fee = r.get('Tuition Fee', '').strip().replace('$', '').replace(',', '')
            nt = r.get('Non Tuition Fee', '').strip().replace('$', '').replace(',', '')
            rows.append({
                'cricos': r['CRICOS Course Code'].strip(),
                'title': r['Course Name'].strip(),
                'duration': int(dur) if dur.isdigit() else '',
                'fee': clean_numeric_fee(fee),
                'enrol_fee': clean_numeric_fee(nt),
            })
    print(f'  CSV courses: {len(rows)}')
    intake_date = 'February, July'
    out = [{
        'cricos': r['cricos'], 'title': r['title'], 'url': '',
        'course_duration_per_week': r['duration'],
        'offshore_tuition_fee': '' if r['fee'] == 'NULL' else r['fee'],
        'onshore_tuition_fee': '', 'enrolment_fee': '' if r['enrol_fee'] == 'NULL' else r['enrol_fee'],
        'materials_fee': '', 'intake': intake_date,
        'course_description': '', 'entry_requirements': '',
        'source': 'register', 'note': 'CSV-driven (no SSR data)',
    } for r in rows]
    pd.DataFrame(out).to_excel(OUTPUT_XLSX, index=False)
    emitted = set()
    with open(OUTPUT_SQL, 'w', encoding='utf-8') as f:
        f.write('-- Update provider institution details\n'
                'UPDATE provider_institution SET\n'
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for r in rows:
            if r['cricos'] in emitted: continue
            emitted.add(r['cricos'])
            dur = str(r['duration']) if r['duration'] else 'NULL'
            fee = r['fee']; enr = r['enrol_fee']
            f.write(f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur},\n"
                    f"    offshore_tuition_fee = {fee},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = {enr},\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '',\n"
                    f"    apply_form = '',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{r['cricos']}';\n\n")
    print(f'     xlsx -> {OUTPUT_XLSX.name}')
    print(f'     sql  -> {OUTPUT_SQL.name}')
    print(f'\n  ✅ {len(emitted)} courses. Intake: {intake_date}')
    print(f'  {PROVIDER_NAME} scraper complete.\n')

if __name__ == '__main__':
    main()
