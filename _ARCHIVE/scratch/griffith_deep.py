"""Deep inspect Griffith page for hidden data."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

url = 'https://www.griffith.edu.au/study/degrees/bachelor-of-nursing-2036'
r = curl.get(url, impersonate='chrome120', timeout=30)
print(f'Status: {r.status_code}, Size: {len(r.text)}b')

# Check for CSR framework
has_react = 'react' in r.text.lower()
has_angular = 'angular' in r.text.lower()
has_next = '<script id="__NEXT_DATA__"' in r.text
has_vue = 'vue' in r.text.lower()
has_jsonld = 'application/ld+json' in r.text
has_cricos_body = 'CRICOS' in r.text

print(f'React: {has_react}, Next: {has_next}, Vue: {has_vue}, Angular: {has_angular}')
print(f'JSON-LD: {has_jsonld}, CRICOS in text: {has_cricos_body}')

# Check what's in <main> or #content
soup = BeautifulSoup(r.text, 'html.parser')

# Find all divs with content
for d in soup.find_all('div'):
    cls = d.get('class', [])
    txt = d.get_text(strip=True)[:80]
    if any(c for c in cls if 'content' in c.lower() or 'main' in c.lower() or 'degree' in c.lower()):
        if len(txt) > 20:
            print(f'  Div.{cls}: {txt[:100]}')

# Check for <noscript> with SSR content
for noscript in soup.find_all('noscript'):
    t = noscript.get_text(strip=True)[:200]
    if t:
        print(f'  noscript: {t[:100]}')

# Look for degree name anywhere
for kw in ['Bachelor of Nursing', 'bachelor-of-nursing', 'degree name', 'program name']:
    for el in soup.find_all(string=re.compile(kw, re.I)):
        ctx = el.strip()[:150]
        if len(ctx) > 10:
            print(f'  Found "{kw}": {ctx[:100]}')

# Script tags content
print('\n=== Script tags analysis ===')
for s in soup.find_all('script'):
    if s.get('id') == '__NEXT_DATA__':
        continue
    if s.string and len(s.string) > 200:
        txt = s.string[:200]
        if 'nursing' in txt.lower() or 'degree' in txt.lower() or 'program' in txt.lower():
            print(f'  Script (len={len(s.string)}): {txt[:150]}...')
            # Search for CRICOS
            for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', s.string, re.I):
                print(f'    CRICOS in script: {m.group()}')

# Check if it redirects via JS/refresh
for m in soup.find_all('meta', content=re.compile(r'url=|URL=', re.I)):
    print(f'  Refresh/redirect meta: {m.get("content")}')

# The real URL
print(f'\nFinal URL after redirect: {r.url}')
print(f'Title tag: {soup.title.string.strip() if soup.title else "none"}')

# Check for data attributes
patterns = ['cricos', 'course-code', 'program-code', 'data-course']
for p in patterns:
    els = soup.find_all(attrs={p: True})
    if els:
        for e in els[:3]:
            print(f'  [{p}] = {e.get(p)}')

# Check for JSON data in script
print('\n=== scripts with large data ===')
for s in soup.find_all('script'):
    if s.string and len(s.string) > 5000:
        # Check if it looks like course data
        for kw in ['"name"', '"description"', '"cricos"', '"duration"']:
            if kw in s.string:
                print(f'  Large script ({len(s.string)}b) contains {kw}')
                # Try to extract cricos
                for m in re.finditer(r'cricos["\']\s*:\s*["\'](\d{6,7}[A-Za-z]?)["\']', s.string, re.I):
                    print(f'    CRICOS: {m.group(1)}')
                break
