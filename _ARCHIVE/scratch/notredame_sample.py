"""Notre Dame - scrape a sample course page for structure."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'

# Sample nursing page
url = 'https://www.notredame.edu.au/programs/school-of-nursing/undergraduate/bachelor-of-nursing'
r = curl.get(url, impersonate='chrome120', timeout=30)
body = r.text
s = BeautifulSoup(body, 'html.parser')

h1 = s.find('h1')
print(f'Title: {h1.get_text(strip=True) if h1 else "?"}')

# Schema.org JSON-LD
for sc in s.select('script[type="application/ld+json"]'):
    try:
        d = json.loads(sc.string or '{}')
        if isinstance(d, dict):
            print(f'JSON-LD @type: {d.get("@type")}')
            if d.get('@type') == 'Course':
                print(f'  name: {d.get("name")}')
                print(f'  identifier: {d.get("identifier")}')
                print(f'  description: {(d.get("description") or "")[:200]}')
                for o in (d.get('offers') or []):
                    print(f'  offer: {o.get("category")} = {o.get("priceSpecification",{}).get("price")}')
            else:
                print(f'  keys: {list(d.keys())[:8]}')
    except: pass

# Meta CRICOS
for m in s.find_all('meta'):
    if 'cricos' in str(m.get('name','') + m.get('content','')).lower():
        print(f'Meta CRICOS: {m.get("content")}')

# Fee patterns
for m in re.finditer(r'\$[\s,0-9]+', body):
    ctx = re.sub(r'\s+', ' ', body[max(0,m.start()-50):m.end()+50])[:120]
    if re.search(r'\d{4,}', m.group()) and not re.search(r'background|margin|padding|font', ctx, re.I):
        print(f'Fee candidate: {ctx}')

# Duration patterns
for m in re.finditer(r'(\d+[.\d]*)\s*(year|semester|month|week|session)s?', body, re.I):
    ctx = re.sub(r'\s+', ' ', body[max(0,m.start()-40):m.end()+40])[:100]
    if not re.search(r'background|margin|padding|font|color', ctx, re.I):
        print(f'Duration: {ctx}')

# Intake/Start date
for m in re.finditer(r'(start|intake|commence|session).{0,40}', body, re.I):
    txt = re.sub(r'\s+', ' ', m.group())[:60]
    if any(k in txt.lower() for k in ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec', 'semester', 'session', 'trimester']):
        print(f'Intake: {txt}')

# Entry requirements
for m in re.finditer(r'(entry requirement|admission requirement|academic entry).{0,60}', body, re.I):
    txt = re.sub(r'\s+', ' ', m.group())[:80]
    print(f'Entry: {txt}')

print(f'\nPage size: {len(body)} bytes')
print(f'Status: {r.status_code}')
