"""Notre Dame - listing pages for actual course links."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'

for path in ['/study/our-programs/undergraduate', '/study/our-programs/postgraduate']:
    r = curl.get(DOMAIN + path, impersonate='chrome120', timeout=30)
    s = BeautifulSoup(r.text, 'html.parser')
    
    # Show all links
    links = []
    for a in s.find_all('a', href=True):
        h = a['href']
        txt = a.get_text(strip=True)[:50]
        if re.search(r'/programs/[^/]+/[a-z]', h):
            if h.startswith('/'): h = DOMAIN + h
            links.append((txt, h))
    
    print(f'{path}: {len(links)} course links')
    for txt, h in links[:5]:
        print(f'  [{txt}] -> {h.split("/")[-1][:30]}')
    
    # Also check any data- attributes
    cards = s.find_all(attrs={'data-program': True})[:3]
    for c in cards:
        print(f'  data-program: {c["data-program"][:100]}')
