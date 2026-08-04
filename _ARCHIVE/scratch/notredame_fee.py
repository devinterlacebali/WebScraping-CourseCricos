"""Notre Dame - find CRICOS and fee."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

url = 'https://www.notredame.edu.au/programs/school-of-nursing/undergraduate/bachelor-of-nursing'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text
s = BeautifulSoup(body, 'html.parser')

# CRICOS in body
for m in re.finditer(r'CRICOS[^.]*\d{6}[A-Z]', body, re.I):
    txt = re.sub(r'\s+', ' ', m.group())[:100]
    print(f'CRICOS ctx: {txt}')

# Specific CRICOS number known from earlier exploration
target = '015324A'
if target in body:
    idx = body.index(target)
    ctx = re.sub(r'\s+', ' ', body[max(0,idx-50):idx+50])[:100]
    print(f'015324A ctx: {ctx}')

# Fee - search for dollar amounts
for m in re.finditer(r'\$[\s,0-9]+', body):
    if not re.search(r'\d{4,}', m.group()): continue
    ctx = re.sub(r'\s+', ' ', body[max(0,m.start()-60):m.end()+60])[:120]
    if re.search(r'#[0-9a-fA-F]', ctx): continue
    if re.search(r'background|margin|padding|font-size', ctx, re.I): continue
    print(f'  Fee: {ctx}')

# Look for fee-related content divs
for el in s.find_all('div'):
    cls = ' '.join(el.get('class', [])) if el.get('class') else ''
    if not cls: continue
    if any(k in cls.lower() for k in ['fee','cost','tuition','price']):
        print(f'Div [{cls}]: {el.get_text(strip=True)[:120]}')
