"""
uowc_02_sitemap.py — Analisa sitemap UOW College
"""

import sys
sys.path.insert(0, r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\venv\Lib\site-packages')

from curl_cffi import requests
import re

r = requests.get("https://www.uowcollege.edu.au/sitemap.xml", impersonate="chrome", timeout=30)
print(f"Status: {r.status_code}")

urls = re.findall(r'<loc>([^<]+)</loc>', r.text)
print(f"\nTotal URLs in sitemap: {len(urls)}")

# Kategorisasi
categories = {
    'course': [],
    'story': [],
    'support': [],
    'about': [],
    'student': [],
    'other': [],
}

for u in urls:
    if '/courses-pathways/' in u:
        categories['course'].append(u)
    elif '/our-stories/' in u or '/college-insider/' in u:
        categories['story'].append(u)
    elif '/support-resources/' in u:
        categories['support'].append(u)
    elif '/about/' in u:
        categories['about'].append(u)
    elif '/students/' in u or '/student-life/' in u:
        categories['student'].append(u)
    else:
        categories['other'].append(u)

for cat, items in categories.items():
    print(f"\n{cat.upper()}: {len(items)} URLs")
    if items and len(items) <= 10:
        for u in items:
            print(f"  - {u}")
    elif items:
        print(f"  Sample:")
        for u in items[:5]:
            print(f"  - {u}")

# Course URLs breakdown
course_urls = categories['course']
print(f"\n\n--- COURSE URL DETAIL ---")
print(f"Total course-related URLs: {len(course_urls)}")

# Sub-categorize course URLs
course_pages = [u for u in course_urls if not any(u.endswith(p) for p in ['/', '#/'])]
print(f"Unique course detail/listing pages: {len(course_pages)}")
