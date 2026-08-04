"""Notre Dame - sitemap pattern analysis."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.notredame.edu.au'
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)

# Categorize by path depth
cats = {}
for u in urls:
    p = u.replace(DOMAIN, '').strip('/')
    parts = p.split('/')
    if len(parts) >= 2:
        key = parts[0] + '/' + parts[1]
    else:
        key = parts[0] if parts else 'root'
    cats.setdefault(key, []).append(u)

for k, v in sorted(cats.items(), key=lambda x: -len(x[1]))[:20]:
    print(f'{k}: {len(v)}')
    if len(v) <= 3:
        for u in v: print(f'  {u}')

# Look specifically for course/degree/program patterns
print('\n=== Course-like URLs ===')
course_pats = [u for u in urls if re.search(r'/(course|degree|program)/[a-z]', u)]
print(f'Total: {len(course_pats)}')
for u in course_pats[:10]:
    print(f'  {u}')
