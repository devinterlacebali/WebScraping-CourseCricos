"""Explore Griffith sitemap properly."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re, json

# Check sitemap structure
r = curl.get('https://www.griffith.edu.au/sitemap.xml', impersonate='chrome120', timeout=30)
print(f'Status: {r.status_code}, Size: {len(r.text)}b')

# Check if it's a sitemap index
if 'sitemapindex' in r.text.lower() or 'sitemapindex' in r.text.lower():
    soup = BeautifulSoup(r.text, 'xml')
    for loc in soup.find_all('loc'):
        print(f'  {loc.text}')
    # Get all sitemaps
    sitemap_urls = re.findall(r'<loc>(.*?)</loc>', r.text)
    for su in sitemap_urls:
        print(f'\nFetching {su[:80]}...')
        r2 = curl.get(su, impersonate='chrome120', timeout=30)
        urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        courses = [u for u in urls if 'degree' in u.lower() or 'course' in u.lower() or 'study' in u.lower()]
        print(f'  {len(urls)} URLs, {len(courses)} courses')
        if courses:
            for c in courses[:3]: print(f'    {c}')
else:
    print('Direct sitemap')
    urls = re.findall(r'<loc>(.*?)</loc>', r.text)
    print(f'Total: {len(urls)}')
    for u in urls[:20]:
        print(f'  {u}')
    
    # Also check search/api for course data
    print('\n=== Looking for course pages ===')
    # Try common patterns
    for path in ['/study/degrees', '/study/courses', '/courses', '/future-students/courses']:
        r2 = curl.get(f'https://www.griffith.edu.au{path}', impersonate='chrome120', timeout=15)
        nxt = '<script id="__NEXT_DATA__"' in r2.text
        print(f'  {path}: {r2.status_code}, {len(r2.text)}b, Next={nxt}')
        if len(r2.text) < 500:
            print(f'    Body: {r2.text[:200]}')
