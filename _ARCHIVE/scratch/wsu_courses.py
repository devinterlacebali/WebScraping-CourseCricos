"""WSU - find course pages."""
import sys, re, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Get sitemap
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Total URLs: {len(urls)}')

# Categories
cats = {}
for u in urls:
    p = u.replace(DOMAIN, '').strip('/').split('/')
    cat = p[0] if p else 'root'
    cats[cat] = cats.get(cat, 0) + 1

# Find course/study related categories
for c, n in sorted(cats.items(), key=lambda x: -x[1])[:25]:
    sample = [u for u in urls if u.replace(DOMAIN, '').strip('/').startswith(c)]
    print(f'  /{c}/: {n} — e.g. {sample[0][:80] if sample else ""}')

# Search for course-related paths
course_related = [u for u in urls if any(k in u.lower() for k in ['/course/', '/degree/', '/study/', '/program/'])]
print(f'\nCourse-related URLs: {len(course_related)}')
for u in sorted(course_related)[:8]:
    print(f'  {u}')

# Check what WSU provider code is
codes = {}
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and len(row) > 3:
            name = row[3].lower()
            if 'western sydney' in name or 'wsd' in name or 'uws' in name:
                codes[row[0].strip()] = codes.get(row[0].strip(), 0) + 1
print(f'\nCSV provider codes for WSU: {codes}')

# Also check by name
print('\n--- Search By Provider Name ---')
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and len(row) > 1:
            name = row[1].strip().lower() if len(row) > 1 else ''
            code = row[0].strip()
            if 'western sydney' in name:
                print(f'  {code} | {row[1][:60]}')
