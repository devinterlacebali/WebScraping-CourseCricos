"""Deep inspection of UC course page."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re, json
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(H)

url = 'https://www.canberra.edu.au/course/ARB401/1/2026'
r = S.get(url, timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')

# All meta tags
print('=== ALL META TAGS ===')
for m in soup.find_all('meta'):
    name = m.get('name') or m.get('property') or m.get('itemprop') or '?'
    content = m.get('content', '')
    if content:
        print(f'  {name}: {content[:200]}')

# Scripts with JSON
print('\n=== SCRIPTS (JSON) ===')
for s in soup.find_all('script'):
    stype = s.get('type', '')
    if stype in ('application/ld+json', 'application/json'):
        try:
            data = json.loads(s.string)
            print(f'  {stype}: {json.dumps(data, indent=2)[:500]}')
        except:
            pass

# All headings
print('\n=== HEADINGS ===')
for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
    txt = h.get_text(strip=True)[:100]
    print(f'  {h.name}: {txt}')

# Key data extraction
body = soup.get_text()
print('\n=== KEY DATA EXTRACTION ===')
for pat in ['CRICOS', 'duration', 'fee', 'intake', 'cricos', 'semester', 'tuition', 'month']:
    for m in re.finditer(r'.{0,40}' + pat + r'.{0,40}', body, re.I):
        val = m.group().strip()
        if 10 < len(val) < 200 and 'error' not in val.lower():
            print(f'  [{pat}]: {val}')

# Page structure
print(f'\n=== PAGE ANALYSIS ===')
title = soup.title.string.strip() if soup.title else 'none'
print(f'Title: {title}')
print(f'Size: {len(r.text)}b')
print(f'Scripts: {len(soup.find_all("script"))}')
print(f'Links: {len(soup.find_all("a"))}')

# Relevant divs
print('\n=== KEY DIVS ===')
for d in soup.find_all('div', class_=True):
    cls = ' '.join(d.get('class', []))
    kw = cls.lower()
    if any(x in kw for x in ['content', 'main', 'course', 'detail', 'fee', 'duration']):
        txt = d.get_text(strip=True)[:200]
        print(f'  .{cls}: {txt}')
