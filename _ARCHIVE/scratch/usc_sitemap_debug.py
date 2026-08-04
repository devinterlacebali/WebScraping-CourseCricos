"""USC - find all sitemap pages with course URLs."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

# Check sitemap structure
r = curl.get('https://www.unisc.edu.au/sitemap.xml', impersonate='chrome120', timeout=30)
body = r.text
print(f'Sitemap page 1: {len(body)} bytes')

# Check if it's a sitemap index
if 'sitemapindex' in body.lower() or '<sitemap>' in body.lower():
    print('This is a sitemap INDEX!')
    subs = re.findall(r'<loc>(.*?)</loc>', body)
    print(f'Sub-sitemaps: {len(subs)}')
    for s in subs[:10]:
        print(f'  {s}')
else:
    # Direct URL set
    urls = re.findall(r'<loc>(.*?)</loc>', body)
    print(f'Total URLs: {len(urls)}')
    course_urls = [u for u in urls if '/study/courses-and-programs/' in u and 'handbook' not in u]
    print(f'Course URLs: {len(course_urls)}')
    if course_urls: print(f'Sample: {course_urls[0]}')
    
    # Show URL categories
    from collections import Counter
    cats = Counter()
    for u in urls:
        parts = u.replace('https://www.unisc.edu.au', '').strip('/').split('/')
        if parts:
            cats[parts[0]] += 1
    for k, v in cats.most_common(15):
        print(f'  /{k}/: {v}')

# Try pages 2-5
for i in range(2, 6):
    r2 = curl.get(f'https://www.unisc.edu.au/sitemap.xml?page={i}', impersonate='chrome120', timeout=15)
    body2 = r2.text
    urls2 = re.findall(r'<loc>(.*?)</loc>', body2)
    course2 = [u for u in urls2 if '/study/courses-and-programs/' in u and 'handbook' not in u]
    print(f'Page {i}: {len(urls2)} URLs, {len(course2)} course URLs')
    if course2:
        print(f'  e.g. {course2[0]}')
