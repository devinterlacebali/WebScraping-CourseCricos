"""Continue ECU exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.ecu.edu.au'

# Check robots.txt for sitemaps
r = curl.get(f'{DOMAIN}/robots.txt', impersonate='chrome120', timeout=20)
for l in r.text.split('\n'):
    if 'sitemap' in l.lower():
        print(f'robots.txt sitemap: {l.strip()}')

# Also check common sitemap config
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=20)
print(f'/sitemap.xml: status={r2.status_code}')

# Try fetching known course URL pattern
test_urls = [
    '/future-students/courses',
    '/future-students/courses/',
    '/degrees/',
    '/study/courses',
    '/courses',
    '/courses/',
    '/study-areas',
    '/future-students/course-finder',
]

for path in test_urls:
    try:
        r3 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=15)
        s3 = BeautifulSoup(r3.text, 'html.parser')
        h1 = s3.find('h1')
        title = h1.get_text(strip=True) if h1 else 'none'
        # Check for JS data
        has_next = '__NEXT_DATA__' in r3.text
        has_nuxt = '__NUXT__' in r3.text
        body = re.sub(r'\s+', ' ', s3.get_text())[:100]
        print(f'{path}: status={r3.status_code}, h1={title[:40]}, next={has_next}, nuxt={has_nuxt}')
    except Exception as e:
        print(f'{path}: ERROR {e}')
