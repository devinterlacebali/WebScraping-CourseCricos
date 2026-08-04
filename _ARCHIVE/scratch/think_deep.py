"""Check Think page structure and provider info."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

base = 'https://www.think.edu.au'

# Check footer for CRICOS provider code
r = curl.get(base, impersonate='chrome120', timeout=30)
soup = BeautifulSoup(r.text, 'html.parser')
footer = soup.find('footer')
if footer:
    ft = footer.get_text()
    for m in re.finditer(r'CRICOS|Provider|PRISMS', ft, re.I):
        print(f'Footer CRICOS context: {ft[max(0,m.start()-20):m.end()+50]}')
    codes = re.findall(r'\b\d{5,7}[A-Za-z]?\b', ft)
    print(f'Codes in footer: {codes}')

# Deep inspect nursing page
r2 = curl.get(f'{base}/courses/diploma-of-nursing', impersonate='chrome120', timeout=30)
soup2 = BeautifulSoup(r2.text, 'html.parser')

# Find CRICOS
body = re.sub(r'\s+', ' ', soup2.get_text())
for m in re.finditer(r'CRICOS[^\d]*(\d{6,7}[A-Za-z]?)', body):
    print(f'\nNursing CRICOS: {m.group(1)}')

# Find fee
for m in re.finditer(r'\$[0-9,]{4,}', body):
    ctx = body[max(0,m.start()-30):m.end()+50]
    print(f'Fee: {m.group()} ctx: {ctx.strip()[:80]}')

# Find duration
for m in re.finditer(r'(\d+\.?\d*)\s*(year|month|week)\s', body):
    ctx = body[max(0,m.start()-30):m.end()+30]
    print(f'Duration: {m.group()} ctx: {ctx.strip()[:80]}')

# Check for JSON-LD
for sc in soup2.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(sc.string)
        if isinstance(data, dict):
            print(f'\nJSON-LD type: {data.get("@type")}')
            if data.get('@type') == 'Course':
                print(f'  name: {data.get("name")}')
                print(f'  provider: {data.get("provider")}')
                print(f'  offers: {data.get("offers")}')
            elif data.get('@graph'):
                for g in data['@graph']:
                    if g.get('@type') == 'Course':
                        print(f'  Course: {g.get("name")}')
                        print(f'  CRICOS: {g.get("cricos")}')
                        print(f'  fees: {g.get("offers")}')
    except: pass
