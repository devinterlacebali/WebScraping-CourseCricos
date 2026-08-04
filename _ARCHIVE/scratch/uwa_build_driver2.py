"""UWA - build enriched driver with CRICOS from CSV matching."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import csv, re, time, requests
import pandas as pd

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(H)

SLUG = 'uwa'
DIR = 'The University of Western Australia'
EXCEL_PATH = f'{DIR}/{SLUG}.xlsx'

# 1. Load ALL UWA entries from CRICOS CSV
def clean_for_match(s):
    """Normalize string for matching."""
    s = re.sub(r'[^a-z0-9\s]', ' ', s.lower())
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Build CSV lookup: normalized name -> CRICOS info
csv_lookup = {}
csv_names_debug = []

with open('cricos-courses.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # skip header
    
    for row in reader:
        if not row or len(row) < 4:
            continue
        provider = row[0].strip()
        cricos_code = row[2].strip()
        course_name = row[3].strip()
        
        if provider == '00126G':  # UWA
            key = clean_for_match(course_name)
            csv_lookup[key] = (cricos_code, course_name)
            csv_names_debug.append(course_name)

print(f'UWA courses in CSV: {len(csv_lookup)}')

# 2. Get course paths from sitemap
r = S.get('https://www.uwa.edu.au/study/sitemap.xml', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
course_paths = [u for u in urls if '/home/courses/' in u.lower() and 'scholarship' not in u.lower()]
print(f'Course paths from sitemap: {len(course_paths)}')

# 3. Fetch each page and match against CSV
rows = []
for i, cp in enumerate(course_paths):
    slug = cp.split('/')[-1]
    public_url = f'https://www.uwa.edu.au/study/courses/{slug}'
    
    try:
        r2 = S.get(public_url, timeout=30)
        text = r2.text
        status = r2.status_code
        
        # Skip 404
        if status == 404:
            rows.append({'cricos': '', 'title': '404', 'url': public_url, 'slug': slug, 
                         'course_duration_per_week': '', 'intake': '', 'offshore_tuition_fee': 'NULL',
                         'onshore_tuition_fee': 'NULL', 'course_description': '', 'entry_requirements': ''})
            if i % 50 == 0 and i > 0:
                print(f'  ... {i}/{len(course_paths)}')
            continue
        
        # Extract title from <title>
        title_m = re.search(r'<title>(.*?)</title>', text, re.DOTALL)
        title = ''
        if title_m:
            title = title_m.group(1).replace('| The University of Western Australia', '').strip()
        
        # Duration
        dur_m = re.search(r'(\d+(?:\.\d+)?)\s*(year|semester|month)[s]?\s*full.?time', text, re.I)
        duration_str = dur_m.group(1) if dur_m else ''
        duration_code = ''
        if duration_str:
            try:
                years = float(duration_str)
                weeks = int(round(years * 52))
                duration_code = str(weeks)
            except:
                pass
        
        # Intake
        intake = ''
        intake_m = re.search(r'INTAKE ([A-Za-z]+)', text)
        if intake_m:
            intake = intake_m.group(1)
        
        # Description from DEGREE OVERVIEW tab
        desc = ''
        overview_m = re.search(r'About the ([^"]+?)</h2>\s*(.*?)(?:<h[23]|$)', text, re.DOTALL)
        if overview_m:
            overview = re.sub(r'<[^>]+>', ' ', overview_m.group(2))
            overview = re.sub(r'\s+', ' ', overview).strip()
            desc = overview[:500] if len(overview) > 500 else overview
        
        # Entry requirements from tab
        entry = ''
        entry_m = re.search(r'ENTRY REQUIREMENTS[^<]*</tab>.*?<h2[^>]*>Entry requirements</h2>(.*?)(?:<h[23]|$)', text, re.DOTALL)
        if not entry_m:
            entry_m = re.search(r'<h2[^>]*>Entry requirements</h2>(.*?)(?:<h[23]|$)', text, re.DOTALL)
        if entry_m:
            entry_html = re.sub(r'<[^>]+>', ' ', entry_m.group(1))
            entry = re.sub(r'\s+', ' ', entry_html).strip()[:500]
        
        # 4. Match against CSV lookup
        clean_title = clean_for_match(title)
        cricos = ''
        matched_name = ''
        
        if clean_title in csv_lookup:
            cricos, matched_name = csv_lookup[clean_title]
        else:
            # Try substring matching
            for csv_key, (ccn, cname) in csv_lookup.items():
                # Check if one contains the other
                if len(clean_title) >= 10 and (csv_key.startswith(clean_title) or clean_title.startswith(csv_key)):
                    cricos, matched_name = ccn, cname
                    break
                # Also check if they share long common substring
                elif len(clean_title) >= 15 and len(csv_key) >= 15:
                    common = 0
                    words1 = set(clean_title.split())
                    words2 = set(csv_key.split())
                    intersection = words1 & words2
                    if len(intersection) >= max(len(words1), len(words2)) * 0.6:
                        cricos, matched_name = ccn, cname
                        break
        
        if not cricos:
            # Try by slug/course code in the URL
            for csv_key, (ccn, cname) in csv_lookup.items():
                csv_clean = clean_for_match(cname)
                slug_clean = slug.replace('-', ' ')
                words_csv = set(csv_clean.split())
                words_slug = set(slug_clean.split())
                if len(words_csv & words_slug) >= min(len(words_csv), len(words_slug)) * 0.5:
                    cricos, matched_name = ccn, cname
                    break
        
        rows.append({
            'cricos': cricos,
            'title': title,
            'url': public_url,
            'slug': slug,
            'course_duration_per_week': duration_code,
            'intake': intake,
            'offshore_tuition_fee': 'NULL',
            'onshore_tuition_fee': 'NULL',
            'course_description': desc,
            'entry_requirements': entry,
        })
        
        if (i+1) % 50 == 0:
            print(f'  ... {i+1}/{len(course_paths)}')
            time.sleep(1)
    except Exception as e:
        rows.append({'cricos': '', 'title': '', 'url': public_url, 'slug': slug,
                     'course_duration_per_week': '', 'intake': '',
                     'offshore_tuition_fee': 'NULL', 'onshore_tuition_fee': 'NULL',
                     'course_description': '', 'entry_requirements': ''})
        print(f'  ERROR [{i+1}]: {slug}: {e}')
    
    time.sleep(0.3)

# 5. Create enriched driver and save
df = pd.DataFrame(rows)

# Filter out 404s
valid = df[df['title'] != '404']
total_valid = len(valid)
with_cricos = valid['cricos'].astype(bool).sum()
with_duration = valid['course_duration_per_week'].astype(bool).sum()

print(f'\nTotal valid (non-404): {total_valid}')
print(f'With CRICOS: {with_cricos}')
print(f'With duration: {with_duration}')

# Check what's missing CRICOS
missing_cricos = valid[~valid['cricos'].astype(bool)]['title'].tolist()
print(f'\nMissing CRICOS ({len(missing_cricos)} courses):')
for t in missing_cricos[:20]:
    print(f'  - {t[:60]}')

df.to_excel(EXCEL_PATH, index=False)
print(f'\nSaved: {EXCEL_PATH}')
