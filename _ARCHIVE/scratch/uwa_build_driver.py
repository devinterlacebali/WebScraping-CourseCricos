"""UWA - build driver from sitemap."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re, time
import pandas as pd

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(H)

SLUG = 'uwa'
DIR = 'The University of Western Australia'
EXCEL_PATH = f'{DIR}/{SLUG}.xlsx'

# 1. Get course paths from study sitemap
r = S.get('https://www.uwa.edu.au/study/sitemap.xml', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)

# Filter to home/courses/ paths only (not scholarships, not categories)
course_paths = [u for u in urls if '/home/courses/' in u.lower() and 'scholarship' not in u.lower()]
print(f'Course paths from sitemap: {len(course_paths)}')

# 2. Map to public URLs and fetch basic info
rows = []
for i, cp in enumerate(course_paths):
    slug = cp.split('/')[-1]
    public_url = f'https://www.uwa.edu.au/study/courses/{slug}'
    
    try:
        r2 = S.get(public_url, timeout=30)
        text = r2.text
        status = r2.status_code
        
        # Extract title from <title> tag
        title_m = re.search(r'<title>(.*?)</title>', text, re.DOTALL)
        title = ''
        if title_m:
            title = title_m.group(1).replace('| The University of Western Australia', '').strip()
        
        # Duration
        dur_m = re.search(r'(\d+(?:\.\d+)?)\s*(year|semester|month)[s]?\s*full.?time', text, re.I)
        duration = dur_m.group(0) if dur_m else ''
        
        # CRICOS - check page for individual course CRICOS
        cricos = ''
        cricos_m = re.search(r'CRICOS[^<]{0,50}([0-9]{5,7}[A-Za-z])', text)
        if cricos_m:
            code = cricos_m.group(1)
            if code != '00126G':  # Skip provider code, look for individual course CRICOS
                cricos = code
        
        rows.append({
            'cricos': cricos,
            'title': title,
            'url': public_url,
            'slug': slug,
            'duration': duration,
        })
        
        if (i+1) % 50 == 0:
            print(f'  ... {i+1}/{len(course_paths)}')
            time.sleep(1)
    except Exception as e:
        rows.append({'cricos': '', 'title': '', 'url': public_url, 'slug': slug, 'duration': ''})
        print(f'  ERROR [{i+1}]: {slug}: {e}')
    
    time.sleep(0.3)

df = pd.DataFrame(rows)
with_title = df['title'].astype(bool).sum()
with_cricos = df['cricos'].astype(bool).sum()
with_duration = df['duration'].astype(bool).sum()

print(f'\nTotal: {len(df)} courses')
print(f'With title: {with_title}')
print(f'With CRICOS: {with_cricos}')
print(f'With duration: {with_duration}')

# Save
df.to_excel(EXCEL_PATH, index=False)
print(f'Driver saved: {EXCEL_PATH}')
