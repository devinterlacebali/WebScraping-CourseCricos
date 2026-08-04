"""USC - check correct sitemap."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

# Correct sitemap
r = curl.get('https://www.unisc.edu.au/XMLsitemap', impersonate='chrome120', timeout=30)
print(f'XMLsitemap: {r.status_code} ({len(r.text)} bytes)')
body = r.text

# Check if sitemap index
if '<sitemap' in body.lower():
    print('This is a sitemap INDEX')
    subs = re.findall(r'<loc>(.*?)</loc>', body)
    for s in subs[:5]:
        print(f'  {s}')
else:
    urls = re.findall(r'<loc>(.*?)</loc>', body)
    print(f'Total URLs: {len(urls)}')
    # Look for course pages
    course_urls = [u for u in urls if '/study/courses-and-programs/' in u]
    # Filter out handbook/non-course
    course_urls = [u for u in course_urls if 'handbook' not in u.lower()]
    print(f'Course URLs: {len(course_urls)}')
    if course_urls:
        print(f'Sample: {course_urls[0]}')

    # Categories
    cats = {}
    for u in urls:
        p = u.replace('https://www.unisc.edu.au', '').strip('/')
        parts = p.split('/')
        if len(parts) >= 2:
            key = parts[0] + '/' + parts[1]
        elif parts:
            key = parts[0]
        else:
            key = 'root'
        cats[key] = cats.get(key, 0) + 1
    
    for k, v in sorted(cats.items(), key=lambda x: -x[1])[:20]:
        print(f'  {k}: {v}')
