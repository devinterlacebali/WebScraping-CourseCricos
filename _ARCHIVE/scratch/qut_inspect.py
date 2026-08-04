"""Deep inspection of QUT course page."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

r = curl.get('https://www.qut.edu.au/courses/bachelor-of-nursing', impersonate='chrome120')
soup = BeautifulSoup(r.text, 'html.parser')

print(f'Status: {r.status_code}, size: {len(r.text)}b')
print(f'Title: {soup.title.string.strip() if soup.title else "none"}')
print()

# 1. JSON-LD
print('=== JSON-LD ===')
for s in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(s.string)
        if isinstance(data, list):
            for d in data:
                if isinstance(d, dict) and d.get('@type') in ('Course', 'Product', 'WebPage'):
                    print(json.dumps(d, indent=2)[:800])
        elif isinstance(data, dict):
            if data.get('@type') == 'Course':
                print(json.dumps(data, indent=2)[:800])
            elif data.get('@type') == 'WebPage':
                # Check for courseCode in mainEntity
                me = data.get('mainEntity', {})
                if isinstance(me, dict) and me.get('@type') == 'Course':
                    print(json.dumps(me, indent=2)[:800])
    except:
        pass

# 2. All meta tags
print('\n=== META TAGS ===')
for m in soup.find_all('meta'):
    name = m.get('name', m.get('property', m.get('itemprop', '?')))
    content = m.get('content', '')
    if content and len(content) > 10:
        print(f'  {name}: {content[:150]}')

# 3. Headings structure
print('\n=== HEADINGS ===')
for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
    txt = h.get_text(strip=True)[:100]
    if txt:
        print(f'  {h.name}: {txt}')

# 4. CRICOS mentions
print('\n=== CRICOS ===')
for el in soup.find_all(string=re.compile(r'CRICOS', re.I)):
    print(f'  {el.parent.name}: {el.strip()[:150]}')

# 5. Fee data
print('\n=== FEE ===')
for el in soup.find_all(string=re.compile(r'\$[0-9,]', re.I)):
    ctx = el.strip()[:200]
    if any(w in ctx.lower() for w in ['fee', 'tuition', 'cost', 'annual', 'year']):
        print(f'  {ctx}')

# 6. Duration
print('\n=== DURATION ===')
for el in soup.find_all(string=re.compile(r'(year|month|week)s? (full|part)', re.I)):
    print(f'  {el.strip()[:200]}')
for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)s?\s*(full|part)', r.text, re.I):
    print(f'  {m.group()[:80]}')

# 7. Page size / structure
print(f'\n=== STRUCTURE ===')
print(f'Scripts: {len(soup.find_all("script"))}')
print(f'Links: {len(soup.find_all("a"))}')
print(f'Has ld+json: {len(soup.find_all("script", type="application/ld+json"))}')
