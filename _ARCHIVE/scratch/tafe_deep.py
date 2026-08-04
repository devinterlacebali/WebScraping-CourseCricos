"""TAFE NSW - check course detail for CRICOS/fee."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.tafensw.edu.au'

# Check a few course pages for CRICOS/intl fee
samples = [
    '/course-areas/nursing/courses/diploma-of-nursing-...',
    '/course-areas/nursing-and-health-science/courses/diploma-of-nursing--HLT54121-01',
    '/course-areas/health,-nursing-and-wellbeing/courses/diploma-of-nursing--HLT54121-01',
    '/course-areas/childcare,-aged-care-and-disability/courses/diploma-of-nursing--HLT54121-01',
]

# Find nursing courses from sitemap
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
nursing_urls = [u for u in urls if 'nurs' in u.lower() and 'course-areas' in u]
print(f'Nursing course URLs: {len(nursing_urls)}')
for u in sorted(nursing_urls)[:8]:
    print(f'  {u}')

# Check one in detail
print('\n=== Sample course detail ===')
if nursing_urls:
    url = nursing_urls[0]
    r2 = curl.get(url, impersonate='chrome120', timeout=30)
    print(f'{url.split("/")[-1][:60]}: {r2.status_code}, {len(r2.text)}b')
    if r2.status_code == 200 and len(r2.text) > 1000:
        s2 = BeautifulSoup(r2.text, 'html.parser')
        h1 = s2.find('h1')
        body = re.sub(r'\s+', ' ', s2.get_text())
        print(f'H1: {h1.get_text(strip=True)[:80] if h1 else "?"}')
        cricos = bool(re.search(r'CRICOS', body))
        fee_intl = bool(re.search(r'International|intl.*fee|AUD\s*\$', body))
        print(f'CRICOS: {cricos}')
        
        # Check Nuxt data
        has_nuxt = '__NUXT__' in r2.text
        print(f'__NUXT__: {has_nuxt}')
        if has_nuxt:
            m = re.search(r'__NUXT__\s*=\s*({.*?});', r2.text, re.S)
            if m:
                data = json.loads(m.group(1))
              #  print(json.dumps(data, indent=2)[:1000])
        
        if cricos:
            for m in re.finditer(r'CRICOS.{0,80}', body):
                print(f'  CRICOS: {m.group()[:100]}')
        
        # Show fee-related text
        for m in re.finditer(r'(?:\$[0-9,]{4,}|AUD\s*\$[0-9,]+)', body):
            ctx = body[max(0,m.start()-80):m.end()+80]
            print(f'  Fee: {ctx.strip()[:150]}')
        
        # Check all text for CRICOS-like patterns
        for m in re.finditer(r'\d{6,7}[A-Za-z]', body):
            code = m.group()[:8]
            ctx = body[max(0,m.start()-40):m.end()+40]
            if not any(ign in ctx for ign in ['freecall', 'telephone', 'phone', 'postcode']):
                print(f'  CRICOS code: {code} | ...{ctx.strip()[:80]}...')
