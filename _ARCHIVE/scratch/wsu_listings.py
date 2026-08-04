"""WSU - check course listing pages for intake."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

for path in ['/future/study/courses', '/future/study/courses/undergraduate', 
             '/future/study/courses/postgraduate', '/future/study/courses/international']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    print(f'{path}: {r.status_code}, {len(r.text)}b')
    if r.status_code == 200 and len(r.text) > 1000:
        s = BeautifulSoup(r.text, 'html.parser')
        body = re.sub(r'\s+', ' ', s.get_text())
        # Find actual course links
        links = [a['href'] for a in s.find_all('a', href=True)]
        course_links = [l for l in links if l not in [path, f'{path}/'] and ('/courses/' in l.lower() or ('/future/study/' in l.lower() and l.count('/') > 4))]
        print(f'  Links: {len(set(links))}, Course links: {len(set(course_links))}')
        for l in sorted(set(course_links))[:5]:
            print(f'    {l}')
        # Find intake mentions
        for m in re.finditer(r'(?:intake|session|semester|start|commence|study\s*period).{0,100}', body, re.I):
            txt = m.group()[:120]
            if any(month in txt for month in ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'March', 'July']):
                print(f'  Intake: {txt}')
                break
        else:
            print(f'  No intake mention found')
