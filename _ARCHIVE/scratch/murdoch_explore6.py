"""Murdoch - find degree pages with CRICOS codes and full data."""
import requests, re, json, sys, gzip, io
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

# 1. Get all course URLs from sitemap
r = S.get('https://www.murdoch.edu.au/sitemap/sitemap.xml', timeout=30)
buf = io.BytesIO(r.content)
with gzip.GzipFile(fileobj=buf) as f:
    content = f.read().decode('utf-8', errors='replace')

urls = re.findall(r'<loc>(.*?)</loc>', content)
course_urls = [u for u in urls if '/course/' in u]
print(f'Total course URLs: {len(course_urls)}')

# Sample some different types
types = set()
for u in course_urls:
    parts = u.split('/course/')[1].split('/')
    if len(parts) >= 2:
        types.add(parts[0])

print(f'Course types found: {types}')

# Check each type
for t in sorted(types):
    sample_urls = [u for u in course_urls if f'/course/{t}/' in u][:3]
    print(f'\n--- Type: {t} ({len([u for u in course_urls if f"/course/{t}/" in u])} total) ---')
    for u in sample_urls:
        try:
            r2 = S.get(u, timeout=30)
            h1 = re.search(r'<h1[^>]*>(.*?)</h1>', r2.text, re.DOTALL)
            title = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else 'N/A'
            
            # Check for CRICOS
            has_cricos = 'cricos' in r2.text.lower()
            has_fee = bool(re.search(r'\$[0-9,]+', r2.text))
            has_duration = bool(re.search(r'\d+\s*(year|semester)', r2.text, re.I))
            
            print(f'  {title[:40]:40s} | CRICOS mention: {has_cricos} | Fee: {has_fee} | Duration: {has_duration} | {u}')
            
            if has_cricos:
                for m in re.finditer(r'[0-9]{6,7}[A-Za-z]', r2.text):
                    start = max(0, m.start()-30)
                    ctx = r2.text[start:m.end()+30]
                    clean = re.sub(r'\s+', ' ', ctx)
                    print(f'    CRICOS candidate: {m.group(0)} ctx: ...{clean[:120]}')
        except Exception as e:
            print(f'  ERROR: {e}')
