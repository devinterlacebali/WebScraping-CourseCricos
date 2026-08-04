"""CDU international course check."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.cdu.edu.au'

# Check international landing pages
paths = [
    '/international',
    '/international/courses',
    '/international/study/courses',
    '/international/future-students/courses',
    '/courses/international',
    '/study/courses/international',
    '/international/study',
]

for path in paths:
    try:
        r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=15)
        s = BeautifulSoup(r.text, 'html.parser')
        h1 = s.find('h1')
        title = h1.get_text(strip=True)[:50] if h1 else 'none'
        links = len(s.find_all('a', href=re.compile(r'/course/')))
        print(f'{path}: {r.status_code} | {title} | course_links={links}')
    except Exception as e:
        print(f'{path}: ERROR {e}')
