"""Curtin University - quick exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.curtin.edu.au'

# Main site
r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
print(f'Main: {r.status_code}, {len(r.text)}b')
has_cloudflare = 'cloudflare' in r.text.lower() or 'cf-ray' in r.headers.get('cf-ray', '')
print(f'Cloudflare: {has_cloudflare}')
soup = BeautifulSoup(r.text, 'html.parser')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
has_next = '__NEXT_DATA__' in r.text
has_nuxt = '__NUXT__' in r.text
print(f'Next.js: {has_next}, Nuxt: {has_nuxt}')

# Sitemap
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
if r2.status_code == 200 and len(r2.text) > 100:
    urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
    print(f'Sitemap: {len(urls)} URLs')
    course_urls = [u for u in urls if '/course/' in u.lower() or '/study/' in u.lower()]
    print(f'Course URLs: {len(course_urls)}')
    for u in course_urls[:5]: print(f'  {u}')
else:
    print(f'Sitemap: {r2.status_code}')
    # Try other sitemap patterns
    for sp in ['/sitemap-index.xml', '/sitemap_0.xml', '/course-sitemap.xml']:
        r3 = curl.get(f'{DOMAIN}{sp}', impersonate='chrome120', timeout=15)
        if r3.status_code == 200:
            urls = re.findall(r'<loc>(.*?)</loc>', r3.text)
            print(f'  {sp}: {len(urls)} URLs')
            course_urls = [u for u in urls if 'course' in u.lower()]
            for u in course_urls[:3]: print(f'    {u}')
            break
