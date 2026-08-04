"""Notre Dame - explore program pages."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'

# Check under /programs/school-of-nursing
r = curl.get(DOMAIN + '/programs/school-of-nursing', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')
links = []
for a in s.find_all('a', href=True):
    h = a['href']
    if re.search(r'/programs/[^/]+/[a-z]', h):
        if h.startswith('/'): h = DOMAIN + h
        links.append(h)

print(f'Nursing programs: {len(links)}')
for l in links[:10]:
    rr = curl.get(l, impersonate='chrome120', timeout=15)
    body = rr.text
    cr = bool(re.search(r'CRICOS|01032F', body))
    slug = l.split('/')[-1][:40]
    print(f'  {slug} | {rr.status_code} | CRICOS={cr} | {len(rr.text)}b')

# Check one in detail
print('\n=== Detail page ===')
if links:
    r2 = curl.get(links[0], impersonate='chrome120', timeout=15)
    s2 = BeautifulSoup(r2.text, 'html.parser')
    body = r2.text
    
    h1 = s2.find('h1')
    print(f'Title: {h1.get_text(strip=True) if h1 else "?"}')
    
    for m in re.finditer(r'CRICOS.{0,80}', body, re.I):
        txt = re.sub(r'\s+', ' ', m.group())[:100]
        print(f'  {txt}')
    
    for m in re.finditer(r'\$\s*[0-9,]{4,}', body):
        ctx = re.sub(r'\s+', ' ', body[max(0,m.start()-30):m.end()+30])[:80]
        print(f'  Fee ctx: {ctx}')
        break
    
    for m in re.finditer(r'(?:Duration|year|semester).{0,40}', body, re.I):
        txt = re.sub(r'\s+', ' ', m.group())[:60]
        if any(k in txt.lower() for k in ['year', 'semester', 'week']):
            print(f'  Duration: {txt}')
            break
