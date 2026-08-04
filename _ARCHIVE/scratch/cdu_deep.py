"""CDU deeper exploration."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.cdu.edu.au'

# Get all sitemap URLs and find actual degree pages
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)

# Find actual course/degree pages
degree_keywords = ['/study/course/', '/course/', '/degrees/', '/programs/']
degree_urls = [u for u in urls if any(kw in u.lower() for kw in degree_keywords)]
print(f'Degree-like URLs: {len(degree_urls)}')
for u in degree_urls[:15]:
    print(f'  {u}')
print('...')

# Also check courses listing with study area prefix
# e.g., /study/courses/health, /study/courses/business
study_courses = [u for u in urls if '/study/courses' in u.lower() and not u.endswith('/study/courses')]
print(f'\n/study/courses/* URLs: {len(study_courses)}')
for u in study_courses[:10]:
    print(f'  {u}')

# Quick check if there's Cloudflare or not on course page
print(f'\n--- Testing course page ---')
test_url = [u for u in degree_urls if 'course/' in u][:1]
if test_url:
    try:
        r2 = curl.get(test_url[0], impersonate='chrome120', timeout=15)
        s2 = BeautifulSoup(r2.text, 'html.parser')
        h1 = s2.find('h1')
        print(f'Course page: {r2.status_code}, {len(r2.text)}b')
        print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
        body = re.sub(r'\s+', ' ', s2.get_text())
        has_cricos = bool(re.search(r'CRICOS[^\d]*\d{6,7}', body))
        has_fee = bool(re.search(r'\$\s*[0-9,]{4,}', body))
        print(f'CRICOS: {has_cricos}, Fee: {has_fee}')
        print(f'First 300 chars: {body[:300]}')
    except Exception as e:
        print(f'Course page error: {e}')
