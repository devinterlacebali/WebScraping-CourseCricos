"""CDU (Charles Darwin University) - quick exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.cdu.edu.au'

# Check main site
r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
print(f'Main: {r.status_code}, {len(r.text)}b')
soup = BeautifulSoup(r.text, 'html.parser')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')

# Check for Next.js/Nuxt signals
has_next = '__NEXT_DATA__' in r.text
has_nuxt = '__NUXT__' in r.text
print(f'Next.js: {has_next}, Nuxt: {has_nuxt}')

# Sitemap
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
if r2.status_code == 200:
    urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
    print(f'Sitemap: {len(urls)} URLs')
    course_urls = [u for u in urls if 'course' in u.lower()]
    print(f'Course URLs: {len(course_urls)}')
    for u in course_urls[:5]: print(f'  {u}')
else:
    print(f'Sitemap: {r2.status_code}')

# Try /courses
r3 = curl.get(f'{DOMAIN}/courses', impersonate='chrome120', timeout=30)
if r3.status_code == 200:
    s3 = BeautifulSoup(r3.text, 'html.parser')
    h1_3 = s3.find('h1')
    print(f'/courses H1: {h1_3.get_text(strip=True)[:60] if h1_3 else "none"}')
    # Check for course links
    links = []
    for a in s3.find_all('a', href=True):
        h = a['href']
        if '/course/' in h.lower() or '/study/' in h.lower():
            links.append(h)
    print(f'Course links: {len(links)}')
    for l in links[:5]: print(f'  {l}')

# Check sitemap index / main sitemap for course data  
r4 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=20)
print(f'\nSitemap index check:')
if 'sitemapindex' in r4.text.lower() or 'sitemap' in r4.text.lower():
    # Could be sitemap index
    sitemaps = re.findall(r'<loc>(.*?)</loc>', r4.text)
    print(f'Linked sitemaps: {len(sitemaps)}')
    for s in sitemaps[:10]: print(f'  {s}')
