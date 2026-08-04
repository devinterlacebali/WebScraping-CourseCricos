"""Match UWA courses from CRICOS CSV database."""
import sys, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
import re

# Read UWA driver
df = pd.read_excel('The University of Western Australia/uwa.xlsx')
uwa_titles = df['title'].tolist()

# Read CRICOS CSV and filter for UWA (00126G)
rows = []
line_count = 0
uwa_rows = []

with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)  # skip header
    print(f'Header: {header[:5]}')
    
    for row in reader:
        if not row or len(row) < 4:
            continue
        line_count += 1
        provider_code = row[0].strip()
        if provider_code == '00126G':  # UWA
            uwa_rows.append(row)

print(f'Total CSV lines: {line_count}')
print(f'UWA courses in CSV: {len(uwa_rows)}')

# Show sample UWA courses
print('\n=== UWA courses from CSV ===')
for r in uwa_rows[:10]:
    print(f'  {r[2]:10s} | {r[3][:60]}')

# Now try to match with our driver
print('\n=== Matching ===')
# Clean titles for matching
def clean(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()

# Build lookup by normalized course name
uwa_lookup = {}
for r in uwa_rows:
    name = clean(r[3])
    uwa_lookup[name] = r  # CRICOS course code is at index 2

matched = 0
unmatched = 0
matches = []

for title in uwa_titles:
    cricos = ''
    # Clean the title
    t = clean(title.split(':')[0].strip())  # Remove " : The University of Western Australia" suffix
    
    # Direct match
    if t in uwa_lookup:
        matched += 1
        cricos = uwa_lookup[t][2]
        matches.append((title, cricos, 'direct'))
        continue
    
    # Try partial match - check if our title is a prefix of CSV name or vice versa
    found = False
    for csv_name, r in uwa_lookup.items():
        if t == csv_name or csv_name.startswith(t) or t.startswith(csv_name):
            matched += 1
            cricos = r[2]
            matches.append((title, cricos, 'partial'))
            found = True
            break
    
    if not found:
        unmatched += 1
        matches.append((title, '', 'none'))

print(f'Direct matches: {sum(1 for m in matches if m[2]=="direct")}')
print(f'Partial matches: {sum(1 for m in matches if m[2]=="partial")}')
print(f'Unmatched: {unmatched}')

# Show unmatched
print('\n=== Unmatched titles (first 30) ===')
for t, c, typ in matches:
    if typ == 'none':
        print(f'  {t[:60]}')

# Show matched samples
print('\n=== Matched samples ===')
matched_list = [m for m in matches if m[1]]
for t, c, typ in matched_list[:20]:
    print(f'  {c:10s} | {t[:60]}')
