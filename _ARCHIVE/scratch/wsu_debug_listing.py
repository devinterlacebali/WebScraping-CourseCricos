"""WSU debug listing page."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

for path in ['/future/study/courses/undergraduate', '/future/study/courses/postgraduate']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    s = BeautifulSoup(r.text, 'html.parser')
    links = []
    for a in s.find_all('a', href=True):
        h = a['href']
        parts = h.strip('/').split('/')
        if len(parts) >= 5 and parts[0] == 'future' and parts[1] == 'study' and parts[2] == 'courses':
            links.append(h)
    
    print(f'{path}: {len(links)} links')
    for l in links[:10]:
        print(f'  {l}')
    
    # Also show all links with "future/study/courses" in them
    all_future = [a['href'] for a in s.find_all('a', href=True) if 'future/study/courses' in a.get('href', '')]
    print(f'All future/study/courses links: {len(all_future)}')
    for l in all_future[:5]: print(f'  {l}')
