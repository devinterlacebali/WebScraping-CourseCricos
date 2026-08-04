"""Box Hill - analyze homepage links."""
import sys, re
import json
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.boxhill.edu.au'

r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')

# Show all menu/nav links
for a in s.find_all('a', href=True):
    h = a['href']
    txt = a.get_text(strip=True)[:50]
    if not txt: continue
    if any(k in txt.lower() for k in ['course', 'study', 'program', 'international', 'future', 'student']):
        if h.startswith('/'): h = DOMAIN + h
        print(f'  [{txt[:40]}] -> {h}')

# Check JSON-LD for data
for sc in s.select('script[type="application/ld+json"]'):
    try:
        d = json.loads(sc.string or '{}')
        if isinstance(d, dict):
            print(f'\nJSON-LD type: {d.get("@type")}')
            if d.get('@type') == 'Organization':
                print(f'  Name: {d.get("name")}')
                print(f'  url: {d.get("url")}')
            # Print first 3 keys
            keys = list(d.keys())[:5]
            for k in keys:
                v = d[k]
                if isinstance(v, str):
                    print(f'  {k}: {v[:120]}')
                elif isinstance(v, list):
                    print(f'  {k}: [{len(v)} items]')
                else:
                    print(f'  {k}: {str(v)[:120]}')
    except: pass
