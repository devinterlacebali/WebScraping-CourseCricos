"""UTas - check if course pages exist at different domain."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.utas.edu.au'

# Try the international page which lists courses for intl students
r = curl.get(f'{DOMAIN}/international', impersonate='chrome120', timeout=30)
if r.status_code == 200:
    s = BeautifulSoup(r.text, 'html.parser')
    body = re.sub(r'\s+', ' ', s.get_text())
    links = set(a['href'] for a in s.find_all('a', href=True))
    course_links = [l for l in links if any(k in l for k in ['course', 'degree'])]
    print(f'/international: {len(course_links)} course links')
    for l in course_links[:10]: print(f'  {l}')

# Check /international/courses
r2 = curl.get(f'{DOMAIN}/international/courses', impersonate='chrome120', timeout=30)
print(f'\n/international/courses: {r2.status_code}')
if r2.status_code == 200:
    s2 = BeautifulSoup(r2.text, 'html.parser')
    body2 = re.sub(r'\s+', ' ', s2.get_text())
    links2 = set(a['href'] for a in s2.find_all('a', href=True))
    course_links2 = [l for l in links2 if '/course/' in l]
    print(f'  Course links: {len(course_links2)}')
    for l in course_links2[:5]: print(f'    {l}')

# Check /study/courses
r3 = curl.get(f'{DOMAIN}/study/courses', impersonate='chrome120', timeout=30)
print(f'\n/study/courses: {r3.status_code}')

# Try the search functionality
r4 = curl.get(f'{DOMAIN}/courses/search?query=nursing&type=all', impersonate='chrome120', timeout=30)
print(f'\n/courses/search: {r4.status_code}')

# Try the course detail at different pattern
# UTas Squiz Matrix often has course at /courses/course/{slug}
r5 = curl.get(f'{DOMAIN}/courses/course/bachelor-of-nursing', impersonate='chrome120', timeout=30)
print(f'\n/courses/course/bachelor-of-nursing: {r5.status_code}')
