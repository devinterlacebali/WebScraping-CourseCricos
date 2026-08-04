"""Notre Dame - check actual href values."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'
r = curl.get(DOMAIN + '/study/our-programs/undergraduate', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')

# Show all links
for a in s.find_all('a', href=True):
    h = a['href']
    txt = a.get_text(strip=True)[:60]
    if 'bachelor' in h.lower() or 'nurs' in h.lower() or 'programs/' in h:
        print(f'  [{txt[:40]}] -> {h}')
    
# Also look for program cards with data attributes
for el in s.find_all(True):
    for attr in el.attrs:
        if 'program' in attr.lower() or 'course' in attr.lower():
            print(f'  [{el.name}] {attr}={str(el[attr])[:120]}')
            break
