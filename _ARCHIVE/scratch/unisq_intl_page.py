"""Fetch UniSQ page with studentType=international."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

u = 'https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing?studentType=international'
r = curl.get(u, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
raw = r.text
body = soup.get_text()

print(f'Status: {r.status_code}, Size: {len(r.text)}b')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True) if h1 else "none"}')

# Check fee area
print('\n=== FEE AREA ===')
for div in soup.find_all('div', class_=lambda c: c and 'accordion' in str(c).lower()):
    txt = div.get_text(strip=True)[:500]
    if 'international' in txt.lower():
        print(f'  Accordion: {txt[:300]}')
        for m in re.finditer(r'\$([0-9,]+)', txt):
            print(f'    ${m.group(1)}')

# Check the summary fee
for div in soup.find_all('div', string=re.compile(r'Fees', re.I)):
    parent = div.find_parent(['div','section'])
    if parent:
        txt = parent.get_text(strip=True)[:200]
        if 'international' in txt.lower() or '$' in txt:
            print(f'  Fees section: {txt[:150]}')

# Find the international fee specifically
print('\n=== ALL DOLLAR AMOUNTS > 1000 ===')
for m in re.finditer(r'\$[0-9,]{4,}', body):
    ctx = body[max(0,m.start()-30):m.end()+50]
    print(f'  {m.group()} | {ctx.strip()[:100]}')

# Check duration
print('\n=== DURATION ===')
for m in re.finditer(r'Duration[^:]*:\s*(\d+\s*(?:year|month|week))', body, re.I):
    print(f'  {m.group()}')
for m in re.finditer(r'(\d+\s*years?\s*(?:full|part))', body, re.I):
    print(f'  {m.group()}')

# Check intake
print('\n=== INTAKE ===')
for m in re.finditer(r'(?:Start|Intake)[^:]*:\s*([A-Za-z, ]+)', body, re.I):
    ctx = m.group()[:80]
    if 'error' not in ctx.lower() and 'footer' not in ctx.lower():
        print(f'  {ctx}')

# Look for the summary bar at top
print('\n=== SUMMARY BAR ===')
for div in soup.find_all('div', class_=lambda c: c and ('d-flex' in str(c) or 'summary' in str(c).lower() or 'quick' in str(c).lower())):
    txt = div.get_text(strip=True)[:300]
    if any(kw in txt.lower() for kw in ['fee', 'duration', 'start', 'qtac', 'cricos']):
        print(f'  {txt[:200]}')
