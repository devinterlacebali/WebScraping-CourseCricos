"""Find Murdoch course page structure."""
import requests, re, gzip, io
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Try sitemap
r = requests.get('https://www.murdoch.edu.au/sitemap/sitemap.xml', headers=headers, timeout=30)
if r.headers.get('Content-Type', '').startswith('application/x-gzip') or r.text[:2] == '\x1f\x8b':
    buf = io.BytesIO(r.content)
    with gzip.GzipFile(fileobj=buf) as f:
        content = f.read().decode('utf-8')
else:
    content = r.text

print("Sitemap size:", len(content), "chars")
urls = re.findall(r'<loc>([^<]+)</loc>', content)
print("Total URLs:", len(urls))

# Find course URLs
course_urls = [u for u in urls if '/course/' in u.lower()]
print("Course URLs:", len(course_urls))
for u in course_urls[:10]:
    print(" ", u)

# Try a course
if course_urls:
    test_url = course_urls[0]
    r2 = requests.get(test_url, headers=headers, timeout=30)
    print("\nTest:", test_url)
    print("Status:", r2.status_code)
    if r2.status_code == 200:
        html = r2.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title')
        print("Title:", title.get_text(strip=True) if title else '')
        
        # Meta
        for meta in soup.find_all('meta'):
            name = meta.get('name', '') or meta.get('property', '')
            content = meta.get('content', '')
            if name and content:
                print(" ", name, ":", content[:100])
        
        # CRICOS
        for m in re.finditer(r'CRICOS|cricos|00125J', html):
            start = max(0, m.start() - 50)
            ctx = html[start:m.end() + 80]
            print("  CRICOS:", re.sub(r'\s+', ' ', ctx)[:150])
        
        # Fee
        for m in re.finditer(r'\$[0-9,]+', html):
            start = max(0, m.start() - 80)
            ctx = html[start:m.end() + 80]
            clean = re.sub(r'\s+', ' ', ctx)
            if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'annual']):
                print("  FEE:", clean[:200])

if not course_urls:
    print("\nNo course URLs in sitemap. Looking for study pages...")
    study_urls = [u for u in urls if '/study/' in u.lower()]
    print("Study URLs:", len(study_urls))
    for u in study_urls[:10]:
        print(" ", u)
