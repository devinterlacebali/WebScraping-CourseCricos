"""Explore Murdoch University correct URL structure."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
base = 'https://www.murdoch.edu.au'

# Try different URL patterns
patterns = [
    '/study/courses/bachelor-of-nursing/',
    '/study/courses/course/bachelor-of-nursing/',
    '/course/bachelor-of-nursing/',
    '/courses/bachelor-of-nursing/',
    '/study/course/bachelor-of-nursing/',
    '/future-students/courses/bachelor-of-nursing/',
    '/study/find-a-course/bachelor-of-nursing/',
]

for p in patterns:
    url = base + p
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200:
            title = re.search(r'<title>(.*?)</title>', r.text)
            t = title.group(1) if title else ''
            if '404' not in t and 'Page not found' not in t:
                print(f"✅ {url}")
                print(f"   Title: {t[:80]}")
        else:
            print(f"❌ {r.status_code} {url}")
    except:
        print(f"⚠️ Error {url}")

# Check sitemap index
print("\n=== SITEMAP INDEX ===")
r = requests.get('https://www.murdoch.edu.au/sitemap.xml', headers=headers, timeout=30)
if r.status_code == 200:
    for sm in re.findall(r'<loc>([^<]+)</loc>', r.text):
        if 'course' in sm.lower():
            print(f"  {sm}")
else:
    # Try other sitemap paths
    for path in ['/sitemap', '/sitemapindex.xml', '/sitemap/sitemap.xml']:
        r2 = requests.get(base + path, headers=headers, timeout=30)
        print(f"  {path}: {r2.status_code}")
