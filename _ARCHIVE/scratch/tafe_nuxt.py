"""TAFE NSW - parse Nuxt data for CRICOS + fee."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.tafensw.edu.au'

# The main nursing course
url = f'{DOMAIN}/course-areas/healthcare/courses/diploma-of-nursing--HLT54121-01'
r = curl.get(url, impersonate='chrome120', timeout=30)
print(f'Status: {r.status_code}, {len(r.text)}b')

# Parse __NUXT__
m = re.search(r'__NUXT__\s*=\s*({.*?});', r.text, re.S)
if m:
    data = json.loads(m.group(1))
    print(f'\n__NUXT__ top keys: {list(data.keys())}')
    # Show a subset
    for k, v in data.items():
        if isinstance(v, (str, int, float, bool)):
            print(f'  {k}: {v}')
        elif isinstance(v, dict):
            print(f'  {k}: dict with keys {list(v.keys())[:8]}')
        elif isinstance(v, list):
            print(f'  {k}: list of {len(v)} items')
    
    # Look for CRICOS in Nuxt data
    text = json.dumps(data).lower()
    if 'cricos' in text:
        print(f'\nCRICOS references in __NUXT__:')
        for m2 in re.finditer(r'(cricos[^"]{0,60})', json.dumps(data), re.I):
            print(f'  {m2.group()[:100]}')
    
    # Look for fee data
    for fee_key in ['fee', 'cost', 'price', 'tuition', 'aud']:
        for m2 in re.finditer(r'"[^"]{0,20}' + fee_key + '[^"]{0,60}"\s*:\s*[^,}\]]{0,60}', json.dumps(data), re.I):
            print(f'  {fee_key}: {m2.group()[:120]}')

# Also parse the HTML for CRICOS and fee
soup = BeautifulSoup(r.text, 'html.parser')
body = re.sub(r'\s+', ' ', r.text)

# CRICOS codes in page
for cr in re.finditer(r'\b\d{6,7}[A-Za-z]\b', body):
    code = cr.group()
    ctx = body[max(0,cr.start()-60):cr.end()+60]
    print(f'\nCRICOS code in HTML: {code} | ...{ctx.strip()[:120]}...')

# International fee mentions
for fee_m in re.finditer(r'AUD\s*\$?\s*[0-9,]{4,}', body):
    ctx = body[max(0,fee_m.start()-80):fee_m.end()+80]
    print(f'Fee mention: {ctx.strip()[:150]}')

# Check h1
h1 = soup.find('h1')
print(f'\nH1: {h1.get_text(strip=True)[:80] if h1 else "?"}')

# Look for CRICOS in specific sections
for el in soup.find_all(['p', 'span', 'div', 'li']):
    text = el.get_text(strip=True)
    if re.search(r'CRICOS', text, re.I):
        print(f'CRICOS text: {text[:150]}')
        break

# Also check a higher education course (degree)
print('\n=== TAFE NSW degree page ===')
deg_urls = [u for u in re.findall(r'<loc>(.*?)</loc>', curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30).text)
           if '/degrees/' in u.lower()]
for du in sorted(deg_urls)[:3]:
    r2 = curl.get(du, impersonate='chrome120', timeout=30)
    print(f'{du.split("/")[-1][:50]}: {r2.status_code}')
    if r2.status_code == 200:
        body2 = re.sub(r'\s+', ' ', r2.text)
        cr2 = bool(re.search(r'CRICOS', body2))
        fee2 = bool(re.search(r'AUD', body2))
        print(f'  CRICOS={cr2}, Fee={fee2}')
