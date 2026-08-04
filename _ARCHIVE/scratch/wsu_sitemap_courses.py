"""WSU - find all course URLs from sitemap."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.westernsydney.edu.au'

r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Total URLs: {len(urls)}')

# Find all future/study/courses/ URLs
course_urls = [u for u in urls if '/future/study/courses/' in u.lower()]
print(f'Course URLs: {len(course_urls)}')
for u in sorted(course_urls)[:10]:
    print(f'  {u}')

# Categorize by type
undergrad = [u for u in course_urls if '/undergraduate/' in u]
postgrad = [u for u in course_urls if '/postgraduate/' in u]
research = [u for u in course_urls if '/research/' in u]
other = [u for u in course_urls if not any(x in u for x in ['/undergraduate/', '/postgraduate/', '/research/'])]
print(f'\nUndergraduate: {len(undergrad)}')
print(f'Postgraduate: {len(postgrad)}')
print(f'Research: {len(research)}')
print(f'Other: {len(other)}')

# Check a few samples
print('\n--- Samples ---')
for slug in sorted(undergrad)[:3]:
    print(f'  {slug}')
for slug in sorted(postgrad)[:3]:
    print(f'  {slug}')
