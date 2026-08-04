"""Murdoch - build driver xlsx from sitemap + meta tags."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re, gzip, io, time
import pandas as pd

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

SLUG = 'murdoch'
DIR = 'Murdoch University'
EXCEL_PATH = f'{DIR}/{SLUG}.xlsx'

# 1. Get all URLs from sitemap
r = S.get('https://www.murdoch.edu.au/sitemap/sitemap.xml', timeout=30)
buf = io.BytesIO(r.content)
with gzip.GzipFile(fileobj=buf) as f:
    content = f.read().decode('utf-8', errors='replace')

urls = re.findall(r'<loc>(.*?)</loc>', content)
all_course_urls = [u for u in urls if '/course/' in u]

# Filter: degree pages only (not major pages)
course_urls = []
for u in all_course_urls:
    parts = u.split('/course/')[1].split('/')
    if len(parts) >= 2:
        code = parts[1]
        if re.match(r'^[a-zA-Z]\d+', code):
            course_urls.append(u)

print(f'Degree pages to process: {len(course_urls)}')

# 2. Fetch each page for meta tags
rows = []
for i, u in enumerate(course_urls):
    try:
        r2 = S.get(u, timeout=30)
        text = r2.text

        # Extract meta tags
        def meta(name):
            m = re.search(rf'<meta[^>]*name="{name}"[^>]*content="([^"]+)"', text, re.I)
            return m.group(1) if m else ''

        cricos = meta('course_cricos')
        title = meta('course_name') or meta('title')
        code = meta('course_code')

        if cricos:
            m = re.search(r'[0-9A-Z]{5,8}', cricos)
            cricos = m.group(0) if m else cricos

        rows.append({'cricos': cricos, 'title': title, 'url': u, 'code': code})

        if (i+1) % 30 == 0:
            print(f'  {i+1}/{len(course_urls)} ...')
            time.sleep(1)
    except Exception as e:
        rows.append({'cricos': '', 'title': '', 'url': u, 'code': ''})
        print(f'  ERROR [{i+1}]: {e}')
    time.sleep(0.3)

df = pd.DataFrame(rows)
with_cricos = df['cricos'].astype(bool).sum()
print(f'\nTotal: {len(df)} courses, with CRICOS: {with_cricos}')

# Save
df.to_excel(EXCEL_PATH, index=False)
print(f'Driver saved: {EXCEL_PATH}')
