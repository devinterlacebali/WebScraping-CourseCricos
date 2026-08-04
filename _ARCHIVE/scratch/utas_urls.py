"""UTas - try all course URL patterns."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.utas.edu.au'
COURSE_SLUGS = ['bachelor-of-nursing', 'bachelor-of-science-nursing', 
                'master-of-nursing', 'bachelor-of-business', 'bachelor-of-arts']

# Try different URL patterns
patterns = [
    '/courses/{slug}',
    '/courses/degree/{slug}',
    '/study/courses/{slug}',
    '/study/degree/{slug}',
    '/course/{slug}',
    '/degrees/{slug}',
    '/study/{slug}',
    '/courses/{slug}/home',
]

for slug in COURSE_SLUGS:
    for pat in patterns:
        url = f'{DOMAIN}{pat.format(slug=slug)}'
        try:
            r = curl.get(url, impersonate='chrome120', timeout=10)
            if r.status_code == 200 and len(r.text) > 5000:
                s = BeautifulSoup(r.text, 'html.parser')
                h1 = s.find('h1')
                body = re.sub(r'\s+', ' ', s.get_text())
                cricos = bool(re.search(r'CRICOS', body))
                print(f'200 | {url} | H1={h1.get_text(strip=True)[:40] if h1 else "?"} | CRICOS={cricos}')
                if cricos:
                    for m in re.finditer(r'CRICOS.{0,80}', body):
                        print(f'  CRICOS: {m.group()[:100]}')
                    break
        except:
            pass

# Also check for Squiz Matrix asset pattern
print('\n=== Squiz Matrix asset URLs ===')
for aid in range(1500000, 1500020):
    url = f'{DOMAIN}/?a={aid}'
    try:
        r = curl.get(url, impersonate='chrome120', timeout=5)
        if r.status_code == 200 and len(r.text) > 5000:
            print(f'  ?a={aid}: {r.status_code}, {len(r.text)}b')
    except: pass

# Check __data/assets patterns (Squiz Matrix)
print('\n=== __data/assets course page ===')
r2 = curl.get(f'{DOMAIN}/courses', impersonate='chrome120', timeout=30)
s2 = BeautifulSoup(r2.text, 'html.parser')

# Squiz Matrix uses asset IDs - look for them in the page
asset_ids = set(re.findall(r'\?a=(\d+)', r2.text))
print(f'Asset IDs found: {len(asset_ids)}')
for aid in sorted(asset_ids)[:10]:
    print(f'  ?a={aid}')

# Look for course search AJAX endpoints
for m in re.finditer(r'/__data/([^"\'<>]+)', r2.text):
    ep = m.group(0)
    if any(kw in ep for kw in ['course', 'search', 'list', 'degree']):
        print(f'Data endpoint: {ep}')
