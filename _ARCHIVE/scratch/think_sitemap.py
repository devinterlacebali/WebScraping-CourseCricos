"""Explore Think sitemap & course structure."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup
import re

base = 'https://www.think.edu.au'

r = curl.get(f'{base}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)

print(f'Total URLs in sitemap: {len(urls)}')

# Look for course URLs
course_urls = [u for u in urls if '/courses/' in u.lower() or '/study/' in u.lower()]
print(f'Course/study URLs: {len(course_urls)}')
for u in course_urls[:10]:
    print(f'  {u}')
print(f'  ...')
for u in course_urls[-5:]:
    print(f'  {u}')

# Also check for any other patterns
other = [u for u in urls if 'course' in u.lower() or 'degree' in u.lower() or 'program' in u.lower()]
print(f'\nCourse/degree/program mentions: {len(other)}')
# Print unique path categories
paths = set()
for u in urls:
    parts = u.replace(base, '').strip('/').split('/')
    if len(parts) >= 2:
        paths.add(parts[0])
print(f'\nTop-level path categories:')
for p in sorted(paths):
    count = sum(1 for u in urls if u.replace(base, '').strip('/').startswith(p))
    print(f'  /{p}/: {count}')
