"""Get ECU course URLs from sitemap."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.ecu.edu.au'

# Fetch course sitemap
r = curl.get(f'{DOMAIN}/sitemap.courses.xml', impersonate='chrome120', timeout=30)
print(f'courses sitemap: {len(r.text)}b, status={r.status_code}')
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Course URLs: {len(urls)}')
for u in urls[:5]:
    print(f'  {u}')
print('  ...')

# Also fetch txt sitemap for non-course URLs
r2 = curl.get(f'{DOMAIN}/sitemap.txt', impersonate='chrome120', timeout=30)
txt_urls = r2.text.strip().split('\n')
print(f'\nText sitemap: {len(txt_urls)} URLs')
course_in_txt = [u for u in txt_urls if 'course' in u.lower()]
print(f'Course-like in txt: {len(course_in_txt)}')

# Check a sample course page
print(f'\n=== Sample course page ===')
u = urls[0] if urls else f'{DOMAIN}/courses/2026/bachelor-of-nursing'
print(f'Fetching: {u}')
r3 = curl.get(u, impersonate='chrome120', timeout=20)
s3 = BeautifulSoup(r3.text, 'html.parser')
h1 = s3.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
body = re.sub(r'\s+', ' ', s3.get_text())
print(f'Body (first 300): {body[:300]}')
