"""Chisholm - extract course data."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.chisholm.edu.au'

# Get /courses and look for course data
r = curl.get(f'{DOMAIN}/courses', impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')

# Look for JSON data in scripts
for sc in soup.find_all('script'):
    if sc.string and ('course' in sc.string.lower() or 'data' in sc.string.lower()):
        if len(sc.string) > 100:
            print(f'Script ({len(sc.string)}b): {sc.string[:200]}...')
            # Check if it's JSON
            if sc.string.strip().startswith('{') or sc.string.strip().startswith('['):
                try:
                    d = json.loads(sc.string)
                    print(f'  Valid JSON: {json.dumps(d)[:300]}')
                except: pass

# Look for course links (real course pages, not categories)
links = set()
for a in soup.find_all('a', href=True):
    h = a['href']
    if '/course/' in h or '/courses/' in h:
        links.add(h)
print(f'\nCourse links: {len(links)}')
for l in sorted(links)[:10]:
    print(f'  {l}')

# Check a course detail page
print('\n=== Course detail check ===')
for slug in ['diploma-of-nursing', 'certificate-iv-in-nursing',
             'diploma-nursing', 'nursing']:
    for pat in ['/course/{s}']:
        r2 = curl.get(f'{DOMAIN}{pat.format(s=slug)}', impersonate='chrome120', timeout=15)
        if r2.status_code == 200 and len(r2.text) > 1000:
            s2 = BeautifulSoup(r2.text, 'html.parser')
            h1 = s2.find('h1')
            body = re.sub(r'\s+', ' ', s2.get_text())
            cricos = 'CRICOS' in body
            fee = 'international' in body.lower() and '$' in body
            print(f'{pat.format(s=slug)}: 200 | H1={h1.get_text(strip=True)[:40] if h1 else "?"} | CRICOS={cricos} | Intl=${fee}')
            break

# Check international page structure
print('\n=== International ===')
r3 = curl.get(f'{DOMAIN}/international', impersonate='chrome120', timeout=30)
s3 = BeautifulSoup(r3.text, 'html.parser')
body3 = re.sub(r'\s+', ' ', s3.get_text())
for m in re.finditer(r'CRICOS.{0,80}', body3):
    print(f'  CRICOS: {m.group()[:100]}')
for m in re.finditer(r'00591E|00897F|00012G|00724G', body3):
    print(f'  Provider code: {m.group()}')
