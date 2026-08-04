"""TAFE NSW - explore course API detail."""
import sys, re, json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.tafensw.edu.au'

# Get course detail
r = curl.get(f'{DOMAIN}/api/course/HLT54121-01', impersonate='chrome120', timeout=15)
data = r.json()
print(f'Course: {data.get("title")}')
print(f'Type: {data.get("type")}')

# Show all keys and nested structure
def show_keys(d, prefix='', depth=0):
    if depth > 3: return
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, (dict, list)):
                if isinstance(v, dict):
                    print(f'{prefix}  {k} -> dict with keys: {list(v.keys())[:8]}')
                else:
                    print(f'{prefix}  {k} -> list of {len(v)}')
                show_keys(v, prefix+'  ', depth+1)
            else:
                val = str(v)[:100]
                print(f'{prefix}  {k}: {val}')
    elif isinstance(d, list) and len(d) > 0:
        print(f'{prefix}  [0] = {json.dumps(d[0])[:200]}')

show_keys(data)

# Check CRICOS
text = json.dumps(data)
for m in re.finditer(r'CRICOS', text):
    ctx = text[max(0,m.start()-30):m.end()+100]
    print(f'\nCRICOS: {ctx}')

# Check fee
for m in re.finditer(r'fee|cost|price|tuition|aud', text, re.I):
    ctx = text[max(0,m.start()-40):m.end()+100]
    print(f'\nFee mention: {ctx}')

# Try the degree API
print('\n=== Try degree detail ===')
r2 = curl.get(f'{DOMAIN}/api/course/ZEN001B-01', impersonate='chrome120', timeout=15)
if r2.status_code == 200:
    d2 = r2.json()
    print(f'Course: {d2.get("title")}')
    text2 = json.dumps(d2)
    print(f'Has CRICOS: {"CRICOS" in text2}')
    for m in re.finditer(r'CRICOS|student\s*type|visa', text2, re.I):
        ctx = text2[max(0,m.start()-40):m.end()+80]
        print(f'  {ctx[:150]}')
