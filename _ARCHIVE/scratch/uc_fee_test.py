"""UC fee extraction test."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = 'https://www.canberra.edu.au/course/364JA/2/2027'
r = requests.get(url, headers=H, timeout=20)
soup = BeautifulSoup(r.text, 'html.parser')

print(f'URL: {url}')
print(f'Size: {len(r.text)}b')

# Fee sections
print('\n=== FEE CLASS DIVS ===')
for d in soup.find_all('div', class_=True):
    cls = ' '.join(d.get('class', []))
    if 'fee' in cls.lower():
        print(f'.{cls}: {d.get_text(strip=True)[:200]}')

# Data attributes for fee
print('\n=== DATA ATTRIBUTES ===')
for attr in ['data-annual-fee', 'data-per-unit-fee', 'data-total-fee', 
             'data-domestic-fee', 'data-international-fee']:
    els = soup.find_all(attrs={attr: True})
    for el in els:
        print(f'{attr}: {el.get(attr)}')

# Look through scripts for fee data
print('\n=== SCRIPT FEE REFERENCES ===')
for s in soup.find_all('script'):
    if s.string and ('fee' in s.string.lower() or 'Fee' in s.string or 'tuition' in s.string.lower()):
        for m in re.finditer(r'(?:domestic|international|offshore|onshore|annual|total|per\s*unit)\s*[Ff]ee[^:]*:\s*\$?([0-9,]+)', s.string):
            ctx = s.string[max(0,m.start()-30):m.end()+30]
            print(f'  {ctx}')

# Look for JSON structure in scripts
print('\n=== JSON DATA SCRIPTS ===')
for s in soup.find_all('script', type=re.compile(r'json|data', re.I)):
    if s.string:
        for m in re.finditer(r'[Ff]ee[^:]*:\s*\$?([0-9,]+)', s.string):
            print(f'  fee: ${m.group(1)}')
