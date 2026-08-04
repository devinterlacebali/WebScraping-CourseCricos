"""Deep inspect CQU page."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

r = curl.get('https://www.cqu.edu.au/courses/cu58/bachelor-of-nursing', impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
body = soup.get_text()

print(f'Size: {len(r.text)}b')
print(f'Title: {soup.title.string.strip() if soup.title else "none"}')

# Meta
print('\n=== KEY METAS ===')
for m in soup.find_all('meta'):
    n = m.get('name','') or m.get('property','') or ''
    c = m.get('content','')
    if any(kw in n.lower() for kw in ['cricos','duration','fee','desc','title','startmonth']):
        print(f'  {n}: {c[:150]}')

# CRICOS
print('\n=== CRICOS ===')
for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', body):
    print(f'  {m.group()}')

# Fee
print('\n=== FEES ===')
for m in re.finditer(r'(\$[0-9,]+)[^.]*?per\s*year', body):
    print(f'  ${m.group(1)} {m.group()[:80]}')

# Duration
print('\n=== DURATION ===')
for m in re.finditer(r'Duration[^:]*:\s*(\d+\s*(year|month|week))', body, re.I):
    print(f'  {m.group()}')

# Headings
print('\n=== HEADINGS (first 20) ===')
for h in soup.find_all(['h1','h2','h3'])[:20]:
    txt = h.get_text(strip=True)[:80]
    if txt:
        print(f'  {h.name}: {txt}')

# Now check specific course page sections
print('\n=== FIRST 5000 CHARS HTML (stripped) ===')
stripped = re.sub(r'<script[^>]*>.*?</script>', '', r.text, flags=re.DOTALL)
stripped = re.sub(r'<[^>]+>', '\n', stripped)
lines = [l.strip() for l in stripped.split('\n') if l.strip() and len(l.strip()) > 30]
for l in lines[:30]:
    print(f'  {l[:200]}')
