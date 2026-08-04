"""Build UC driver from sitemap, match CRICOS from CSV."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import csv, re, time
import pandas as pd
import requests
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(H)

PROVIDER_CODE = "00212K"  # UC / University of Canberra

# 1. Fetch sitemap
r = S.get('https://www.canberra.edu.au/services/wcm/site-map/course.xml', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
print(f'Total URLs in sitemap: {len(urls)}')

# Deduplicate by course code (keep latest year)
course_map = {}
for u in urls:
    parts = u.rstrip('/').split('/')
    if len(parts) >= 3:
        # URL format: .../course/CODE/version/year
        # parts[-3] = course code (e.g. ARB401), parts[-1] = year
        code = parts[-3]
        year = parts[-1]
        if code not in course_map or year > course_map[code][1]:
            course_map[code] = (u, year)

print(f'Unique courses: {len(course_map)}')

# 2. Build CSV lookup
csv_lookup = {}
try:
    with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if not row or len(row) < 4:
                continue
            if row[0].strip() == PROVIDER_CODE:
                name = row[3].strip()
                norm = re.sub(r'[^a-z0-9\s]', ' ', name.lower())
                norm = re.sub(r'\s+', ' ', norm).strip()
                csv_lookup[norm] = (row[2].strip(), name, row[18] if len(row) > 18 else '')
except FileNotFoundError:
    print('CSV not found')
    exit(1)

print(f'CSV lookup entries for {PROVIDER_CODE}: {len(csv_lookup)}')

# 3. Fetch each course page
rows = []
i = 0
for code, (url, year) in course_map.items():
    i += 1
    try:
        r = S.get(url, timeout=20)
        if r.status_code != 200 or len(r.text) < 50000:
            print(f'  ⏭️ [{i}/{len(course_map)}] {code} -> {r.status_code} ({len(r.text)}b)')
            continue
        soup = BeautifulSoup(r.text, 'html.parser')
        body = re.sub(r'\s+', ' ', soup.get_text())
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else code

        # Duration
        dur_label = soup.find('h4', string=re.compile('Course duration', re.I))
        dur = ''
        if dur_label:
            dur_block = dur_label.find_next(['p', 'div'])
            if dur_block:
                dur = dur_block.get_text(strip=True)[:100]
        if not dur:
            # Try the course-details section
            det = soup.find('div', class_=re.compile(r'course-details'))
            if det:
                m = re.search(r'(\d+\.?\d*)\s*(year|month|week)', det.get_text(), re.I)
                if m:
                    dur = m.group(0)

        # Intake / available teaching periods
        intake_text = ''
        tp = soup.find(string=re.compile(r'Available teaching periods', re.I))
        if tp:
            parent = tp.find_parent()
            if parent:
                intake_text = parent.get_text(strip=True)[:200]

        # CRICOS from CSV matching
        norm_title = re.sub(r'[^a-z0-9\s]', ' ', title.lower())
        norm_title = re.sub(r'\s+', ' ', norm_title).strip()
        cricos = csv_lookup.get(norm_title, ('', '', ''))[0]

        if not cricos:
            # Word-overlap match
            for csv_key, (cc, csv_name, _) in csv_lookup.items():
                tw = set(norm_title.split())
                cw = set(csv_key.split())
                if len(tw) >= 2 and len(cw) >= 2:
                    overlap = len(tw & cw)
                    ratio = overlap / max(len(tw), len(cw))
                    if ratio >= 0.6:
                        cricos = cc
                        break

        row = {
            'cricos': cricos,
            'title': title.split('(' + code)[0].strip(),
            'url': url,
            'course_code': code,
            'duration_text': dur,
            'intake': intake_text,
        }
        rows.append(row)
        print(f'  {"✅" if cricos else "⏭️"} [{i}/{len(course_map)}] {cricos or "---":<8} {title[:60]}')
        time.sleep(0.3)
    except Exception as e:
        print(f'  ❌ [{i}/{len(course_map)}] {code}: {e}')

# 4. Save driver
df = pd.DataFrame(rows)
df['cricos'] = df['cricos'].replace('', None)
df.to_excel(f'University of Canberra/uc.xlsx', index=False)

print(f'\n✅ Driver saved.')
print(f'  Total: {len(df)}')
print(f'  With CRICOS: {df["cricos"].notna().sum()} / {len(df)}')
print(f'  Duration found: {df["duration_text"].astype(bool).sum()}')
