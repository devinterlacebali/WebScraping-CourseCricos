"""Properly decompress and read Murdoch sitemap."""
import requests, gzip, io
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
r = requests.get('https://www.murdoch.edu.au/sitemap/sitemap.xml', headers=headers, timeout=30)

# Try decompress
try:
    buf = io.BytesIO(r.content)
    with gzip.GzipFile(fileobj=buf) as f:
        content = f.read().decode('utf-8', errors='replace')
    print("Decompressed:", len(content), "chars")
except:
    content = r.text
    print("Raw text:", len(content), "chars")

# Save to file for inspection
with open('/tmp/murdoch_sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(content)

# Extract URLs
import re
urls = re.findall(r'<loc>([^<]+)</loc>', content)
print("URLs found:", len(urls))
for u in urls[:5]:
    print(" ", u)

# Look for course URLs
course_urls = [u for u in urls if 'course' in u.lower()]
print("\nCourse URLs:", len(course_urls))
for u in course_urls[:20]:
    print(" ", u)

if not course_urls:
    # Maybe it's a sitemap index
    sitemaps = re.findall(r'<loc>([^<]+)</loc>', content)
    print("\nSitemaps in index:", len(sitemaps))
    for sm in sitemaps:
        print(" ", sm)
