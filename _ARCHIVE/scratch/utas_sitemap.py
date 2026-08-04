"""UTas - find course pages in sitemap."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.utas.edu.au'

r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Total URLs: {len(urls)}')

# Categories
cats = {}
for u in urls:
    p = u.replace(DOMAIN, '').strip('/').split('/')
    cat = p[0] if p else 'root'
    cats[cat] = cats.get(cat, 0) + 1

print('\nCategories:')
for cat, cnt in sorted(cats.items(), key=lambda x: -x[1])[:20]:
    print(f'  /{cat}/: {cnt} URLs')
    # Show samples
    samples = [u for u in urls if u.replace(DOMAIN, '').strip('/').startswith(cat)]
    for s in samples[:2]:
        print(f'    {s[:100]}')

# Look for course/study URLs
course_terms = ['course', 'degree', 'program', 'study', 'bachelor', 'master', 'diploma']
course_urls = [u for u in urls if any(t in u.lower().split('/') for t in course_terms)]
print(f'\nCourse-related: {len(course_urls)}')
for u in course_urls[:10]:
    print(f'  {u[:120]}')

# Also check the sub-sitemap if exists
r2 = curl.get(f'{DOMAIN}/sitemap/courses.xml', impersonate='chrome120', timeout=30)
if r2.status_code == 200:
    cu = re.findall(r'<loc>(.*?)</loc>', r2.text)
    print(f'\nCourses sitemap: {len(cu)} URLs')
    for u in cu[:5]: print(f'  {u}')

# Try courses subdirectory
r3 = curl.get(f'{DOMAIN}/courses/', impersonate='chrome120', timeout=30)
print(f'\n/courses/: {r3.status_code}')
if r3.status_code == 200:
    s3 = BeautifulSoup(r3.text, 'html.parser')
    h1_3 = s3.find('h1')
    print(f'H1: {h1_3.get_text(strip=True)[:60] if h1_3 else "none"}')
    links = set()
    for a in s3.find_all('a', href=True):
        h = a['href']
        if '/course/' in h:
            links.add(h)
    print(f'Course links: {len(links)}')
    for l in sorted(list(links))[:5]: print(f'  {l}')
