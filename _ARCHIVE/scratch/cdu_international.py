"""CDU - find the international data loading mechanism."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

url = 'https://www.cdu.edu.au/study/course/bachelor-nursing-wnurs1'

# Default domestic view
r = curl.get(url, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
raw = r.text

# 1. Check for JSON-LD
print('=== JSON-LD ===')
for sc in soup.find_all('script', type='application/ld+json'):
    print(f'  {sc.string[:200]}')

# 2. Check for GTM dataLayer
print('\n=== dataLayer ===')
for l in re.finditer(r'dataLayer.*?\[.*?\]', raw):
    print(f'  {l.group()[:200]}')

# 3. Check for data attributes that contain CRICOS/fee
print('\n=== Elements with data-* attrs containing course info ===')
for el in soup.find_all(attrs={'data-course-code': True}):
    print(f'  data-course-code: {el.get("data-course-code")}')
for el in soup.find_all(attrs={'data-cricos': True}):
    print(f'  data-cricos: {el.get("data-cricos")}')

# 4. Check if there's a REST API hidden in JavaScript configs
print('\n=== Scripts containing "api" or "endpoint" ===')
for sc in soup.find_all('script'):
    if sc.string and ('api/' in sc.string or 'endpoint' in sc.string or 'fetch' in sc.string):
        print(f'  Found API reference: {sc.string[:200]}')
        break

# 5. Check what the toggle actually does - any AJAX calls?
print('\n=== Toggle buttons analysis ===')
toggle_links = []
for a in soup.find_all('a', href=True):
    txt = a.get_text(strip=True)
    if 'international' in txt.lower() or 'domestic' in txt.lower():
        toggle_links.append((a['href'], txt))
for href, txt in toggle_links[:5]:
    print(f'  {txt}: {href}')

# 6. Check if international page exists at /international/course/...
print('\n=== Try international path pattern ===')
for path in ['/international/courses/bachelor-nursing-wnurs1',
             '/international/study/course/bachelor-nursing-wnurs1',
             '/study/course/bachelor-nursing-wnurs1?international']:
    try:
        r2 = curl.get(f'https://www.cdu.edu.au{path}', impersonate='chrome120', timeout=10)
        print(f'  {path}: {r2.status_code}')
    except:
        print(f'  {path}: error')

# 7. Check for hidden div with international content
print('\n=== Hidden international content ===')
for div in soup.find_all('div', hidden=True):
    txt = div.get_text(strip=True)[:200]
    if any(kw in txt.lower() for kw in ['cricos', 'international', 'fee', 'tuition']):
        print(f'  Hidden div (class={div.get("class")}): {txt[:200]}')

# 8. Check all heading structure for course outline
print('\n=== Course headings ===')
for h in soup.find_all(['h1','h2','h3','h4']):
    txt = h.get_text(strip=True)
    if len(txt) > 4:
        print(f'  [{h.name}] {txt[:60]}')
