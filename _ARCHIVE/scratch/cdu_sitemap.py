"""CDU - sitemap analysis + international check."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.cdu.edu.au'

# Get all sitemap URLs
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)

# Check for /study/course/ URLs patterns
course_urls = [u for u in urls if '/study/course/' in u.lower()]
print(f'Course URLs: {len(course_urls)}')

# Check how many have international in path separately
intl_courses = [u for u in urls if '/international' in u.lower() and 'course' in u.lower()]
print(f'International + course URLs: {len(intl_courses)}')
for u in intl_courses[:5]:
    print(f'  {u}')

# Check the course-specific pattern at /study/course/X
# Check a sample international course page at /international/study/course/X
sample_slug = course_urls[0].split('/')[-1] if course_urls else ''
print(f'\nSample slug: {sample_slug}')

# Also check if there's a cookie-based view — try setting cookie
import http.cookies
cookies = {'CDU_STUDENT_TYPE': 'international'}
r2 = curl.get(f'{DOMAIN}/study/course/{sample_slug}', impersonate='chrome120', 
              cookies=cookies, timeout=15)
s2 = BeautifulSoup(r2.text, 'html.parser')
body = re.sub(r'\s+', ' ', s2.get_text())
has_intl_fee = 'International' in body
has_cricos = bool(re.search(r'CRICOS', body))
print(f'\nWith CDU_STUDENT_TYPE cookie: intl_fee={has_intl_fee}, cricos={has_cricos}')
if has_cricos:
    for m in re.finditer(r'CRICOS.{0,60}\d{6,7}[A-Za-z]?', body):
        print(f'  CRICOS: {m.group()[:60]}')
if has_intl_fee:
    for m in re.finditer(r'International.{0,80}\$[0-9,]{4,}', body):
        print(f'  Fee: {m.group()[:100]}')
