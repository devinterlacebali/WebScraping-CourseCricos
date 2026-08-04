"""Explore University of Canberra website structure."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Test a course page
url = 'https://www.canberra.edu.au/courses/bachelor-of-nursing'
r = requests.get(url, headers=headers, timeout=60)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

print("Status:", r.status_code)
if r.status_code == 200:
    print("Title:", soup.find('title').get_text(strip=True) if soup.find('title') else '')
else:
    print("Status:", r.status_code)

# Try different URL patterns
urls_to_try = [
    'https://www.canberra.edu.au/course/bachelor-of-nursing',
    'https://www.canberra.edu.au/courses/bachelor-of-nursing',
    'https://www.canberra.edu.au/study/courses/bachelor-of-nursing',
    'https://www.canberra.edu.au/future-students/courses/bachelor-of-nursing',
    'https://www.canberra.edu.au/about-uc/courses/bachelor-of-nursing',
]
for u in urls_to_try:
    try:
        r2 = requests.get(u, headers=headers, timeout=30, allow_redirects=True)
        if r2.status_code == 200 and '404' not in r2.text[:500]:
            title = re.search(r'<title>(.*?)</title>', r2.text)
            t = title.group(1) if title else ''
            if '404' not in t:
                print(f"\n✅ {r2.status_code} {u}")
                print(f"   Title: {t[:80]}")
                print(f"   Final URL: {r2.url}")
                break
    except:
        pass

# Check sitemap
r3 = requests.get('https://www.canberra.edu.au/sitemap.xml', headers=headers, timeout=30)
if r3.status_code == 200:
    urls = re.findall(r'<loc>([^<]+)</loc>', r3.text)
    course_urls = [u for u in urls if 'course' in u.lower()]
    print(f"\nCourse URLs in sitemap: {len(course_urls)}")
    for u in course_urls[:5]:
        print(f"  {u}")
else:
    print(f"\nSitemap: {r3.status_code}")
    r3 = requests.get('https://www.canberra.edu.au/sitemap_index.xml', headers=headers, timeout=30)
    print(f"Sitemap index: {r3.status_code}")
