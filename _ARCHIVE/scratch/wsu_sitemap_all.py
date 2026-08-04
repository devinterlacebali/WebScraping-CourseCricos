"""WSU - check all sitemaps for course URLs."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.westernsydney.edu.au'

# Get sitemap index
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
text = r.text
subs = re.findall(r'<loc>(.*?)</loc>', text)
print(f'Sub-sitemaps: {len(subs)}')

# Try common sitemap names
common = ['/course-sitemap.xml', '/page-sitemap.xml', '/sitemap-index.xml',
          '/wp-sitemap.xml', '/sitemap-courses.xml', '/study-sitemap.xml',
          '/future-sitemap.xml', '/sitemap1.xml']
for sp in common:
    r2 = curl.get(f'{DOMAIN}{sp}', impersonate='chrome120', timeout=15)
    if r2.status_code == 200 and len(r2.text) > 100:
        urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        course_urls = [u for u in urls if '/future/study/' in u.lower()]
        print(f'{sp}: {len(urls)} URLs, {len(course_urls)} course')
        if course_urls: print(f'  e.g. {course_urls[0]}')

# Check sub-sitemaps for course
for s in subs[:5]:
    r3 = curl.get(s, impersonate='chrome120', timeout=15)
    urls3 = re.findall(r'<loc>(.*?)</loc>', r3.text)
    course_urls3 = [u for u in urls3 if '/future/study/courses/' in u.lower()]
    print(f'{s.split("/")[-1][:30]}: {len(urls3)} URLs, {len(course_urls3)} course')
    if course_urls3: print(f'  e.g. {course_urls3[0]}')
