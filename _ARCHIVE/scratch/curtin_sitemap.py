"""Curtin - find course sitemaps."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.curtin.edu.au'

# Common sitemap patterns for Curtin
sitemaps = [
    '/sitemap.xml',
    '/sitemap_index.xml',
    '/sitemap-index.xml',
    '/sitemap_0.xml',
    '/sitemap_1.xml',
    '/sitemap_courses.xml',
    '/course-sitemap.xml',
    '/courses-sitemap.xml',
    '/study-sitemap.xml',
    '/page-sitemap.xml',
    '/post-sitemap.xml',
]

for sp in sitemaps:
    try:
        r = curl.get(f'{DOMAIN}{sp}', impersonate='chrome120', timeout=15)
        text = r.text[:2000].lower()
        if r.status_code == 200 and len(r.text) > 50:
            urls = re.findall(r'<loc>(.*?)</loc>', r.text)
            print(f'{sp}: {r.status_code}, {len(urls)} URLs')
            if urls: 
                for u in urls[:3]: print(f'  {u}')
        else:
            print(f'{sp}: {r.status_code}')
    except Exception as e:
        print(f'{sp}: error')

# Check robots.txt
print('\n--- robots.txt ---')
r2 = curl.get(f'{DOMAIN}/robots.txt', impersonate='chrome120', timeout=15)
print(r2.text[:500])

# Check if there's an API or course search
print('\n--- API check ---')
endpoints = [
    '/api/courses',
    '/api/v1/courses',
    '/study/courses',
    '/courses',
]
for ep in endpoints:
    r3 = curl.get(f'{DOMAIN}{ep}', impersonate='chrome120', timeout=15)
    print(f'{ep}: {r3.status_code}, {len(r3.text)}b')
    if 'api' in ep and 'json' in r3.headers.get('content-type', ''):
        print(f'  JSON: {r3.text[:200]}')
