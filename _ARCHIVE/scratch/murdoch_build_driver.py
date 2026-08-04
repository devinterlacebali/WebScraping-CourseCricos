"""Murdoch - build driver xlsx from sitemap course URLs."""
import requests, re, json, sys, gzip, io, time
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

import pandas as pd
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

# 1. Get all URLs from sitemap
r = S.get('https://www.murdoch.edu.au/sitemap/sitemap.xml', timeout=30)
buf = io.BytesIO(r.content)
with gzip.GzipFile(fileobj=buf) as f:
    content = f.read().decode('utf-8', errors='replace')

urls = re.findall(r'<loc>(.*?)</loc>', content)
print(f'Total sitemap URLs: {len(urls)}')

all_course_urls = [u for u in urls if '/course/' in u]
print(f'All course URLs: {len(all_course_urls)}')

# 2. Filter: keep only degree COURSE pages (not major pages)
# Course pages: /course/{level}/{shortcode} where code starts with letter+digits
# Major pages: /course/{level}/mj-xxx or bh-xxx (multi-char prefix)
course_pages = []
major_pages = []

for u in all_course_urls:
    # Extract the code part after /course/{level}/
    parts = u.split('/course/')[1].split('/')
    if len(parts) >= 2:
        level = parts[0]
        code = parts[1]
        # Course pages have codes like: b1417, c1108, m1260, g1102, n1080
        # Major pages have codes like: mj-fbio, bh-cons, mj-iaidd
        if re.match(r'^[a-z]\d+', code, re.I):
            course_pages.append(u)
        else:
            major_pages.append(u)

print(f'Course pages (degree): {len(course_pages)}')
print(f'Major pages: {len(major_pages)}')
print()

# 3. Sample course pages to see titles
print("=== Sample course pages ===")
sample = course_pages[:5]
for u in sample:
    try:
        r2 = S.get(u, timeout=30)
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', r2.text, re.DOTALL)
        title = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else 'N/A'
        print(f'  {title[:50]:50s} | {u}')
    except Exception as e:
        print(f'  ERROR: {e} | {u}')
    time.sleep(0.3)

# 4. Check what levels exist
print("\n=== Course levels ===")
levels = {}
for u in course_pages:
    level = u.split('/course/')[1].split('/')[0]
    levels[level] = levels.get(level, 0) + 1
for l, c in sorted(levels.items()):
    print(f'  {l}: {c}')

# 5. Build driver xlsx
print("\n=== Building driver xlsx ===")
rows = []
for i, u in enumerate(course_pages):
    try:
        r2 = S.get(u, timeout=30)
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', r2.text, re.DOTALL)
        title = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else 'N/A'
        
        # CRICOS: check page
        cricos = ''
        # Look in the CRICOS footer link
        cricos_match = re.search(r'CRICOS\s*(\d{6,7}[A-Za-z]?)', r2.text)
        if cricos_match:
            cricos = cricos_match.group(1)
        
        # Murdoch provider code is 00125J - course codes are elsewhere
        rows.append({
            'cricos': cricos,
            'title': title,
            'url': u,
        })
        if (i+1) % 30 == 0:
            print(f'  ... {i+1}/{len(course_pages)} courses fetched')
            time.sleep(1)
    except Exception as e:
        rows.append({'cricos': '', 'title': '', 'url': u})
        print(f'  ERROR [{i+1}]: {u[:60]}')
    
    time.sleep(0.2)

df = pd.DataFrame(rows)
print(f'\nTotal: {len(df)} courses')
print(f'With CRICOS: {df["cricos"].astype(bool).sum()}')
print(f'Sample rows:')
print(df.head(10).to_string())
