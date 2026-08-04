"""Notre Dame - find actual course pages."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'

for path in ['/study/our-programs', '/programs']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    s = BeautifulSoup(r.text, 'html.parser')
    
    links = []
    for a in s.find_all('a', href=True):
        h = a['href']
        if re.search(r'/programs?/[a-z]', h) and h not in (path, path + '/'):
            if h.startswith('/'): h = DOMAIN + h
            if 'entry-req' not in h:
                links.append(h)
    
    print(f'{path}: {len(links)} program links')
    if links:
        for l in links[:5]: print(f'  {l}')
        
        # Check one program page for CRICOS
        r2 = curl.get(links[0], impersonate='chrome120', timeout=30)
        if r2.status_code == 200:
            for m in re.finditer(r'CRICOS.{0,60}', r2.text, re.I):
                txt = re.sub(r'\s+', ' ', m.group())[:80]
                print(f'  CRICOS: {txt}')
                break
            print(f'  Page: {len(r2.text)} bytes')
