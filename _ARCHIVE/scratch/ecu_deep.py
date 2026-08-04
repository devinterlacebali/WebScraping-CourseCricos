"""Deep check ECU course pages for data."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

DOMAIN = 'https://www.ecu.edu.au'

r = curl.get(f'{DOMAIN}/sitemap.courses.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Total course URLs: {len(urls)}')

# Check a few sample courses
samples = [
    'https://www.ecu.edu.au/degrees/courses/bachelor-of-nursing',
    'https://www.ecu.edu.au/degrees/courses/master-of-nursing',
    'https://www.ecu.edu.au/degrees/courses/bachelor-of-science-nursing',
]

for url in samples:
    try:
        rp = curl.get(url, impersonate='chrome120', timeout=20)
        sp = BeautifulSoup(rp.text, 'html.parser')
        body = re.sub(r'\s+', ' ', sp.get_text())
        
        print(f'\n{"="*60}')
        print(f'URL: {url}')
        h1 = sp.find('h1')
        print(f'Title: {h1.get_text(strip=True)[:60] if h1 else "none"}')
        
        # CRICOS
        for m in re.finditer(r'CRICOS.{0,30}\d{6,7}[A-Za-z]?', body):
            print(f'  CRICOS: {m.group()[:50]}')
        
        # Fee
        for m in re.finditer(r'(?:international|tuition|fee).{0,30}\$\s*([0-9,]+)', body, re.I):
            val = int(m.group(1).replace(',',''))
            if val > 1000:
                print(f'  Fee: ${val:,} ({m.group()[:60]})')
        
        # Duration
        for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)', body, re.I):
            print(f'  Duration: {m.group()}')
            break
        
        # Intake
        for m_name in ['January','February','March','April','May','June','July','August','September','October','November','December']:
            if m_name in body:
                print(f'  Intake: {m_name} (found)')
                break
        
        # Check if there's JSON-LD
        for sc in sp.find_all('script', type='application/ld+json'):
            print(f'  JSON-LD: {sc.string[:200] if sc.string else "empty"}')
            
        # Check for structured data sections
        for h in sp.find_all(['h2','h3','h4']):
            txt = h.get_text(strip=True)
            if any(kw in txt.lower() for kw in ['about', 'overview', 'entry', 'admission', 'fees', 'duration', 'cricos']):
                ctx = ''
                for sib in h.find_all_next(['p'], limit=2):
                    ctx += ' ' + sib.get_text(strip=True)[:80]
                print(f'  [{h.name}] {txt[:50]}: {ctx[:100]}')
        
    except Exception as e:
        print(f'  ERROR: {e}')
