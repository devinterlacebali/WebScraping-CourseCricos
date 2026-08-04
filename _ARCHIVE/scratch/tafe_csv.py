"""TAFE NSW - check CSV coverage."""
import sys, csv, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

# Find TAFE NSW provider codes in CSV
tafe_codes = set()
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if not row: continue
        name = row[3].strip().lower() if len(row) > 3 else ''
        code = row[0].strip()
        # TAFE NSW patterns in CSV
        if any(k in name for k in ['tafe nsw', 'tafensw', 'tafe ', 'north coast tafe', 
                                    'sydney institute', 'western sydney', 'illawarra',
                                    'hunter institute', 'new england', 'riverina']):
            tafe_codes.add(code)
        # Also match code patterns known for TAFE NSW
        if code in ('00591E', '00724G', '00011G', '00020G', '00092B', '00094M'):
            tafe_codes.add(code)

print(f'TAFE-related provider codes: {len(tafe_codes)}')
for c in sorted(tafe_codes):
    count = 0
    for row in csv.reader(open('cricos-courses.csv', encoding='utf-8')):
        if row and row[0].strip() == c:
            count += 1
    print(f'  {c}: {count} courses')

# Check if 00591E is the main TAFE NSW code
print(f'\n=== Provider 00591E (main TAFE NSW) ===')
courses_00591E = []
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and row[0].strip() == '00591E':
            courses_00591E.append(row)
print(f'Total: {len(courses_00591E)} courses')
nursing = [r for r in courses_00591E if 'nurs' in r[3].lower()]
print(f'Nursing: {len(nursing)}')
for r in nursing[:5]:
    print(f'  {r[2]} | {r[3][:60]} | fee={r[20][:15]} | dur={r[19]}wk')

# Check what "Technical and Further Education Commission" resolves to
print(f'\n=== "Technical and Further Education Commission" in CSV ===')
for row in csv.reader(open('cricos-courses.csv', encoding='utf-8')):
    if row and len(row) > 3 and 'technical' in row[3].lower() and 'further' in row[3].lower():
        print(f'  {row[0]} | {row[3][:80]} | {row[2]}')
        break
