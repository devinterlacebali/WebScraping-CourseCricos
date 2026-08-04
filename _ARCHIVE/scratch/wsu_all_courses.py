"""WSU - full course system discovery."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Get all links from undergrad and postgrad course listing pages
all_course_links = set()

for path in ['/future/study/courses/undergraduate', '/future/study/courses/postgraduate',
             '/future/study/courses/research', '/future/study/courses']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    if r.status_code != 200: continue
    s = BeautifulSoup(r.text, 'html.parser')
    for a in s.find_all('a', href=True):
        h = a['href']
        if '/future/study/courses/' in h and h != path and h != f'{path}/':
            if h.startswith('/'): h = f'{DOMAIN}{h}'
            if DOMAIN in h:
                all_course_links.add(h)

print(f'Total unique course links: {len(all_course_links)}')
for u in sorted(all_course_links):
    print(f'  {u}')
