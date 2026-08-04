"""TAFE NSW - check course pages and CSV coverage."""
import sys, csv, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.tafensw.edu.au'

# Check what provider codes exist in CSV for "TAFE"
print('=== TAFE provider codes in CSV ===')
codes = set()
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and ('tafe' in row[3].lower() or 'tafensw' in row[3].lower() or 'technical' in row[3].lower()):
            codes.add((row[0].strip(), row[3].strip()[:60]))
for c in sorted(codes):
    print(f'  {c[0]} | {c[1]}')

# Also check just every unique provider code
all_codes = set()
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row:
            all_codes.add(row[0].strip())
print(f'\nTotal unique provider codes in CSV: {len(all_codes)}')

# Check a course page
print('\n=== Sample course pages ===')
samples = ['/course-areas/nursing', '/course-areas/nursing-and-health-science',
           '/course-areas/nursing-and-hospitability', '/international/courses']
for path in samples:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    if r.status_code == 200 and len(r.text) > 1000:
        s = BeautifulSoup(r.text, 'html.parser')
        h1 = s.find('h1')
        print(f'{path}: 200 | H1={h1.get_text(strip=True)[:60] if h1 else "none"}')
        # Look for course links
        links = s.find_all('a', href=True)
        course_links = [a['href'] for a in links if '/course-areas/' in a.get('href', '') or '/courses/' in a.get('href', '')]
        if course_links:
            print(f'  Course links: {len(course_links)}')
            for l in course_links[:5]: print(f'    {l}')
        break
    else:
        print(f'{path}: {r.status_code}')
