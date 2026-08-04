"""Notre Dame - check nursing page links."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'
r = curl.get(DOMAIN + '/programs/school-of-nursing', impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')

# Show all links
for a in s.find_all('a', href=True):
    h = a['href']
    txt = a.get_text(strip=True)[:60]
    if 'program' in h or 'course' in h or 'degree' in h or 'nurs' in h:
        print(f'  [{txt[:40]}] -> {h}')
