"""Chisholm - try different approaches."""
import sys, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.chisholm.edu.au'

# Try more URL patterns
print('=== Try various paths ===')
for path in ['/courses', '/course', '/international', '/future-students',
             '/study', '/programs', '/find-a-course', '/search']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=15)
    print(f'{path}: {r.status_code}, {len(r.text)}b')
    if r.status_code == 200 and len(r.text) > 10000:
        s = BeautifulSoup(r.text, 'html.parser')
        h1 = s.find('h1')
        body = re.sub(r'\s+', ' ', s.get_text())
        print(f'  H1: {h1.get_text(strip=True)[:60] if h1 else "?"}')
        # Check for course links
        links = [a['href'] for a in s.find_all('a', href=True)]
        course_links = [l for l in links if 'course' in l.lower() and '#' not in l]
        if course_links:
            print(f'  Course links: {len(set(course_links))}')
            for l in sorted(set(course_links))[:5]: print(f'    {l}')

# Try sitemap index
print('\n=== Sitemaps ===')
for sp in ['/sitemap.xml', '/page-sitemap.xml', '/post-sitemap.xml',
           '/course-sitemap.xml', '/sitemap_index.xml']:
    r2 = curl.get(f'{DOMAIN}{sp}', impersonate='chrome120', timeout=15)
    if r2.status_code == 200:
        urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        print(f'{sp}: {len(urls)} URLs')
        if urls: print(f'  First: {urls[0][:100]}')

# Search CSV for anything Chisholm
print('\n=== CSV search ===')
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and len(row) > 3:
            name = row[3].lower()
            code = row[0].strip()
            if any(k in name for k in ['chisholm', 'holmesglen']):
                print(f'  {code} | {row[3][:60]} | {row[2]}')
                break
