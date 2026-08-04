"""Explore ECU sitemap and site structure."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.ecu.edu.au'

# Check common sitemap paths
sitemap_paths = [
    '/sitemap.xml', '/sitemap_index.xml', '/sitemap/', '/sitemap',
    '/course-sitemap.xml', '/courses-sitemap.xml', '/study-sitemap.xml',
    '/robots.txt',
    '/future-students/courses/',
]
for path in sitemap_paths:
    try:
        r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=20)
        print(f'{path}: status={r.status_code}, size={len(r.text)}b')
        if 'xml' in r.text[:100]:
            urls = re.findall(r'<loc>(.*?)</loc>', r.text)
            print(f'  URLs: {len(urls)}')
            for u in urls[:3]: print(f'    {u}')
        elif r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            sp_text = re.sub(r"\s+", " ", soup.get_text())
            print(f'  Text: {sp_text[:200]}')
    except Exception as e:
        print(f'{path}: ERROR {e}')
    print()
