"""TAFE NSW - find course detail pages."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.tafensw.edu.au'

# Check intl sub-pages for actual course listings
print('=== International sub-pages ===')
for path in ['/international/courses/certificate-to-advanced-diploma',
             '/international/courses/degrees',
             '/international/courses/english-courses',
             '/international/courses/midsemester-intakes']:
    r = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    s = BeautifulSoup(r.text, 'html.parser')
    h1 = s.find('h1')
    links = s.find_all('a', href=True)
    course_links = set()
    for a in links:
        h = a['href']
        if '/international/courses/' in h and h not in [path, f'{path}/']:
            course_links.add(h)
    print(f'{path.split("/")[-1]}: {r.status_code} | H1={h1.get_text(strip=True)[:40] if h1 else "?"} | course-links={len(course_links)}')
    if course_links:
        for l in sorted(list(course_links))[:3]: print(f'  {l}')

# Check sitemap for course detail pages
print('\n=== Course detail URLs from sitemap ===')
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r2.text)

# Find individual course pages (not category pages)
course_detail = []
for u in urls:
    path = u.replace(DOMAIN, '')
    segments = path.strip('/').split('/')
    # Individual courses have deeper paths
    if len(segments) >= 3 and ('course' in segments[0] or 'international' in segments[0]):
        if any(k in u.lower() for k in ['certificate', 'diploma', 'bachelor', 'degree',
                                          'advanced-diploma', 'english-', 'pathway']):
            if len(segments) > 2:  # deeper than category
                course_detail.append(u)

print(f'Course detail URLs: {len(course_detail)}')
for u in sorted(course_detail)[:8]:
    print(f'  {u}')

# Try a nursing-specific course
print('\n=== Try course page ===')
for path in ['/international/courses/nursing', '/course/nursing',
             '/international/courses/diploma-of-nursing',
             '/courses/diploma-of-nursing']:
    r3 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=30)
    if r3.status_code == 200 and len(r3.text) > 5000:
        s3 = BeautifulSoup(r3.text, 'html.parser')
        h1_3 = s3.find('h1')
        body = re.sub(r'\s+', ' ', s3.get_text())
        fee = bool(re.search(r'AUD', body))
        cricos = bool(re.search(r'CRICOS', body))
        print(f'{path}: 200 | H1={h1_3.get_text(strip=True)[:60] if h1_3 else "?"} | Fee={fee} | CRICOS={cricos}')
        if cricos:
            for m in re.finditer(r'CRICOS.{0,80}', body):
                print(f'  {m.group()[:100]}')
        if fee:
            for m in re.finditer(r'AUD\s*\$?\s*[0-9,]{4,}', body):
                ctx = body[max(0,m.start()-40):m.end()+40]
                print(f'  {ctx.strip()[:120]}')
    else:
        print(f'{path}: {r3.status_code}')
