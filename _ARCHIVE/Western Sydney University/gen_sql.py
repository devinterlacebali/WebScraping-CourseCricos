"""Generate correct SQL for WSU from existing XLSX."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd

PROVIDER_CODE = '00917K'
PROVIDER_NAME = 'Western Sydney University'
xlsx = 'Western Sydney University/wsu.xlsx'

df = pd.read_excel(xlsx)

# Intake from data
all_intakes = set()
for v in df['intake'].dropna():
    for m in str(v).split(','):
        m = m.strip()
        if m: all_intakes.add(m)
intake_combined = ', '.join(sorted(all_intakes, key=lambda x: [
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
].index(x) if x in [
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
] else 99))

sql_lines = [f'-- Update provider institution details',
             f'UPDATE provider_institution SET',
             f"    intake_date = '{intake_combined}',",
             f'    updated_at = NOW()',
             f"WHERE cricos_provider_code = '{PROVIDER_CODE}';",
             f'']

sql_cnt = 0
for _, r in df.iterrows():
    cricos = r['cricos']
    if not cricos or not re.match(r'^\d{6,7}[A-Za-z]?$', str(cricos)): continue
    
    desc = str(r.get('description', '') or '')
    if desc in ('nan', 'None', '') or not desc:
        desc = ''
    else:
        desc = desc.replace("'", "''")
        if not desc.startswith('Course overview'):
            desc = f'Course overview <p>{desc}</p>'
    
    fee = r.get('offshore_tuition_fee', 'NULL')
    try: fee = str(int(float(fee))) if float(fee) > 0 else 'NULL'
    except: fee = 'NULL'
    
    dur = r.get('course_duration_per_week', 'NULL')
    try: dur = str(int(float(dur))) if float(dur) > 0 else 'NULL'
    except: dur = 'NULL'
    
    entry = str(r.get('entry_requirements', '') or '')
    if entry in ('nan', 'None', ''):
        entry = ''
    else:
        entry = entry.replace("'", "''")
    
    url = str(r.get('url', '') or '')
    if url in ('nan', 'None'):
        url = ''
    else:
        url = url.replace("'", "''")
    
    sql_lines.append(
        f"UPDATE courses SET"
        f"\n    course_description = '{desc}',"
        f"\n    course_duration_per_week = {dur},"
        f"\n    offshore_tuition_fee = {fee},"
        f"\n    onshore_tuition_fee = NULL,"
        f"\n    enrolment_fee = 0,"
        f"\n    materials_fee = NULL,"
        f"\n    entry_requirements = '{entry}',"
        f"\n    apply_form = '{url}',"
        f"\n    updated_at = NOW()"
        f"\nWHERE cricos_course_code = '{cricos}';"
    )
    sql_cnt += 1

sql_lines.append(f'\n-- {sql_cnt} UPDATE statements generated.')

with open('Western Sydney University/wsu_courses_update.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sql_lines))

print(f'Output: wsu_courses_update.sql ({sql_cnt} statements)')
print(f'Intake: {intake_combined}')
