"""Quick SQL format check for Deakin & JCU.""" 
import re

for name, path in [('Deakin', 'Deakin University/deakin_courses_update.sql'),
                    ('JCU', 'James Cook University/jcu_courses_update.sql')]:
    with open(path, encoding='utf-8') as f:
        sql = f.read()
    print(f'=== {name} ===')
    print(f'  Header: {"✅" if bool(re.search(r"UPDATE provider_institution\s+SET\s+intake_date\s*=", sql, re.I)) else "❌"}')
    print(f'  onshore: {"✅" if bool(re.search(r"onshore_tuition_fee\s*=", sql, re.I)) else "❌"}')
    print(f'  enrolment: {"✅" if bool(re.search(r"enrolment_fee\s*=", sql, re.I)) else "❌"}')
    print(f'  materials: {"✅" if bool(re.search(r"materials_fee\s*=", sql, re.I)) else "❌"}')
    print(f'  apply_form: {"✅" if bool(re.search(r"apply_form\s*=", sql, re.I)) else "❌"}')
    print(f'  updated_at: {"✅" if bool(re.search(r"updated_at\s*=\s*NOW\(\)", sql, re.I)) else "❌"}')
    has_cn = bool(re.search(r'(?<!provider_institution\s)SET.*course_name\s*=', sql, re.I | re.S))
    has_pc = bool(re.search(r'(?<!provider_institution\s)SET.*cricos_provider_code\s*=', sql, re.I | re.S))
    print(f'  no course_name: {"❌" if has_cn else "✅"}')
    print(f'  no cricos_prov_code: {"❌" if has_pc else "✅"}')
    descs = re.findall(r"course_description\s*=\s*'([^']*)'", sql, re.I)
    h = sum(1 for d in descs if '<' in d and '>' in d)
    print(f'  HTML descs: {h}/{len(descs)}')
    print()
