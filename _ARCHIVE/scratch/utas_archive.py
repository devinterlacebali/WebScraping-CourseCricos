"""UTas - find course system."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.utas.edu.au'

# Check course archive for actual course pages
r = curl.get(f'{DOMAIN}/courses/course-and-unit-archive', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')
body = re.sub(r'\s+', ' ', s.get_text())

# Get all links
links = set()
for a in s.find_all('a', href=True):
    h = a['href']
    if 'course' in h.lower() or 'unit' in h.lower():
        links.add(h)
print(f'Archive links: {len(links)}')
for l in sorted(list(links))[:15]:
    print(f'  {l}')

# Check for course search API (Squiz Matrix course search pattern)
for ep in ['/api/course-search', '/api/courses', '/courses/search', '/courses/list']:
    try:
        r2 = curl.get(f'{DOMAIN}{ep}', impersonate='chrome120', timeout=15)
        ct = r2.headers.get('content-type', '')
        print(f'{ep}: {r2.status_code} {ct[:30]}')
        if 'json' in ct: print(f'  {r2.text[:200]}')
    except: pass

# Check subdomain: courses.utas.edu.au
print('\n--- courses.utas.edu.au ---')
try:
    r3 = curl.get('https://courses.utas.edu.au', impersonate='chrome120', timeout=15)
    print(f'Status: {r3.status_code}, {len(r3.text)}b')
except Exception as e:
    print(f'Error: {e}')

# Try UTas API pattern with course codes from CSV
print('\n--- CSV courses for UTas ---')
import csv
csv_courses = []
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and row[0].strip() == '00586B':
            csv_courses.append({'cricos': row[2].strip(), 'name': row[3].strip(), 
                               'fee': row[20].strip(), 'duration': row[19].strip()})
print(f'CSV courses: {len(csv_courses)}')

# Try a course detail API with specific course from CSV
sample = csv_courses[0] if csv_courses else None
if sample:
    print(f'Sample: {sample["name"][:60]} | CRICOS={sample["cricos"]}')

# Also check the https://study.utas.edu.au/ domain for course system
print('\n--- utas.edu.au/study/courses ---')
r4 = curl.get(f'{DOMAIN}/study/courses', impersonate='chrome120', timeout=30)
print(f'Status: {r4.status_code}, {len(r4.text)}b')
if r4.status_code == 200 and len(r4.text) > 1000:
    s4 = BeautifulSoup(r4.text, 'html.parser')
    h1 = s4.find('h1')
    print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
    # Look for course API in JS
    for m in re.finditer(r'/api/([^"\'<>]+)', r4.text):
        api = m.group(0)
        if 'course' in api or 'search' in api or 'degree' in api:
            print(f'API: {api}')
