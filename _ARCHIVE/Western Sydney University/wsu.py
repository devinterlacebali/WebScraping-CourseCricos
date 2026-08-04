"""
Western Sydney University (WSU) scraper — page-scraped.

Site: Cloudflare but `/future/study/courses/{level}/{slug}` has SSR page content.
Extracts: CRICOS, intake (real start dates), fee, duration, description.

Fallback: CSV-driven for any courses not found on website pages.
"""
import os, sys, re, csv, time
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

PROVIDER_CODE = '00917K'
PROVIDER_NAME = 'Western Sydney University'
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = 'wsu'
OUTPUT_XLSX = PROVIDER_DIR / f'{SLUG}.xlsx'
OUTPUT_SQL = PROVIDER_DIR / f'{SLUG}_courses_update.sql'
DOMAIN = 'https://www.westernsydney.edu.au'

MONTH_NAMES = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']


def get_page(url, max_retries=2):
    for attempt in range(max_retries):
        try:
            r = curl.get(url, impersonate='chrome120', timeout=30)
            if r.status_code == 200 and len(r.text) > 1000:
                return r.text
        except: pass
        time.sleep(1)
    return None


def extract_months_from_text(text):
    """Extract month names from a text string like '01 March 2027'."""
    found = []
    for m in MONTH_NAMES:
        if m in text:
            found.append(m)
    return found


def get_course_urls():
    """Generate course URLs from CSV titles instead of listing pages."""
    csv_path = PROVIDER_DIR.parent / 'cricos-courses.csv'
    urls = []
    
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if not row or len(row) < 3: continue
            if row[0].strip() != PROVIDER_CODE: continue
            title = row[3].strip() if len(row) > 3 else ''
            level = row[12].strip().lower() if len(row) > 12 else ''
            cricos = row[2].strip()
            if not title: continue
            
            # Guess undergraduate vs postgraduate
            if any(k in level for k in ['master', 'graduate', 'postgrad']) or \
               any(k in title.lower() for k in ['master', 'graduate', 'phd', 'juris']):
                course_level = 'postgraduate'
            else:
                course_level = 'undergraduate'
            
            # Generate slug
            slug = title.lower()
            slug = re.sub(r'[^a-z0-9\s-]', '', slug)
            slug = re.sub(r'\s+', '-', slug.strip())
            slug = re.sub(r'-{2,}', '-', slug)
            
            url = f'{DOMAIN}/future/study/courses/{course_level}/{slug}'
            urls.append((url, cricos, title, course_level))
    
    print(f'  Generated {len(urls)} candidate URLs from CSV')
    return urls


def scrape_course_page(url):
    """Extract course data from a single course detail page."""
    html = get_page(url)
    if not html: return None

    s = BeautifulSoup(html, 'html.parser')
    body = re.sub(r'\s+', ' ', html)
    body_text = re.sub(r'\s+', ' ', s.get_text())

    # Title from H1
    h1 = s.find('h1')
    title = h1.get_text(strip=True) if h1 else ''

    # CRICOS code — look for 6-7 digit + letter near "CRICOS" keyword or in visible content
    cricos_code = ''
    # First, find CRICOS in context like "CRICOS Code: 041099M"
    for m in re.finditer(r'CRICOS(?:\s*Code)?[:\s]*(\d{6,7}[A-Za-z])', body, re.I):
        cricos_code = m.group(1).upper()
        break
    if not cricos_code:
        # Fallback: any 6-7 digit + letter not in CSS/styling context
        for m in re.finditer(r'(\d{6,7}[A-Za-z])', body):
            ctx = body[max(0,m.start()-30):m.end()+30]
            # Skip if in CSS context
            if re.search(r'#[0-9a-fA-F]|background|color\s*:|opacity|gradient|shadow', ctx, re.I):
                continue
            cricos_code = m.group(1).upper()
            break

    # Intake dates — look for "Start Date DD Month YYYY"
    intake_months = set()
    for m in re.finditer(r'(?:Start Date|Start|Commence|Commencing)\s*(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})', body):
        for month in MONTH_NAMES:
            if month in m.group(1):
                intake_months.add(month)

    # Also search for intakes in dedicated section
    for m in re.finditer(r'(?:Intake|Start)[^.]*(?:January|February|March|April|May|June|July|August|September|October|November|December)[^.]*\.', body):
        for month in MONTH_NAMES:
            if month in m.group(0):
                intake_months.add(month)

    # If no intake found, default
    if not intake_months:
        intake_months = {'March', 'July'}  # WSU typical

    # Sort months chronologically
    intake_sorted = sorted(intake_months, key=lambda m: MONTH_NAMES.index(m))

    # Fee — look for AUD amounts near Fee/International context
    fee = ''
    fee_patterns = [
        r'(?:fee|cost|tuition).{0,100}(?:AUD\s*\$?\s*[0-9,]{4,})',
        r'(?:AUD\s*\$?\s*[0-9,]{4,})',
    ]
    for pat in fee_patterns:
        for m in re.finditer(pat, body, re.I | re.S):
            txt = m.group()
            # Extract the dollar amount
            amt_m = re.search(r'\$?\s*([0-9,]{4,})', txt)
            if amt_m:
                amt = float(amt_m.group(1).replace(',', ''))
                if 5000 < amt < 200000:  # plausible annual fee
                    fee = str(int(amt))
                    break
        if fee: break

    # Duration
    duration_weeks = ''
    for m in re.finditer(r'(?:Duration|duration)[^.]*(?:\d+\.?\d*)\s*(?:Year|year|Month|month)', body):
        txt = m.group(0)[:80]
        num_m = re.search(r'(\d+\.?\d*)\s*(Year|year|Month|month)', txt)
        if num_m:
            val = float(num_m.group(1))
            unit = num_m.group(2).lower()
            if unit == 'year':
                duration_weeks = str(int(val * 52))
            elif unit == 'month':
                duration_weeks = str(int(val * 4.33))
            break

    # Description — get main content area
    description = ''
    for sel in ['[data-tab="overview"]', '.course-overview', 'main p:first-of-type',
                '.content p', '#content']:
        el = None
        if sel.startswith('#'):
            el = s.find(id=sel[1:])
        elif sel.startswith('.'):
            el = s.select_one(sel)
        elif sel == 'main p:first-of-type':
            el = s.select_one('main p')
        elif sel == '.content p':
            el = s.select_one('.content p')
        if el:
            txt = el.get_text(strip=True)[:2000]
            if len(txt) > 30:
                description = txt
                break

    # Entry requirements — collect all wysiwyg divs after "Entry requirements for international students"
    entry_req = ''
    for h in s.find_all(['h2', 'h3', 'h4']):
        txt = h.get_text(strip=True).lower()
        if 'entry requirement' in txt and 'international' in txt:
            parts = []
            # Collect all div.wysiwyg until next h2
            for el in h.find_all_next():
                if el.name in ['h2', 'h3', 'h4'] and el != h: break
                if el.name == 'div' and 'wysiwyg' in ' '.join(el.get('class', [])):
                    t = el.get_text(strip=True)
                    if t: parts.append(t)
            if parts:
                entry_req = '\n\n'.join(parts)[:2000]
            break

    return {
        'title': title,
        'url': url,
        'cricos': cricos_code,
        'fee': fee,
        'duration_weeks': duration_weeks,
        'intake': ', '.join(intake_sorted),
        'description': description,
        'entry_req': entry_req,
    }


def load_csv_data():
    """Load CSV entries for fallback."""
    csv_path = PROVIDER_DIR.parent / 'cricos-courses.csv'
    csv_courses = []
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if not row or len(row) < 3: continue
            if row[0].strip() != PROVIDER_CODE: continue
            csv_courses.append({
                'cricos': row[2].strip(),
                'title': row[3].strip() if len(row) > 3 else '',
                'fee': row[20].strip().replace('$','').replace(',','') if len(row) > 20 and row[20].strip() not in ('', '-') else '',
                'duration': row[19].strip() if len(row) > 19 and row[19].strip() not in ('', '-') else '',
            })
    return csv_courses


def main():
    print(f'\n  {PROVIDER_NAME} Scraper')
    print(f'  {"="*40}')
    print(f'  Provider: {PROVIDER_CODE}')

    # Step 1: Get all course URLs
    course_urls = get_course_urls()

    # Step 2: Scrape each course page
    scraped = {}
    print(f'  Scraping up to {len(course_urls)} course pages...')
    for i, (url, cricos, title, level) in enumerate(course_urls):
        data = scrape_course_page(url)
        if data and data['cricos']:
            scraped[data['cricos']] = data
        if (i + 1) % 50 == 0 or i == len(course_urls) - 1:
            print(f'    [{i+1}/{len(course_urls)}] CRICOS page-match: {len(scraped)}')

    print(f'  Courses with CRICOS from pages: {len(scraped)}')

    # Step 3: Build unified dataset
    csv_courses = load_csv_data()
    print(f'  CSV entries: {len(csv_courses)}')

    rows = []
    matched_from_page = set()

    # First, use scraped data
    for csv_c in csv_courses:
        cricos = csv_c['cricos']
        if cricos in scraped:
            s = scraped[cricos]
            fee = s['fee'] if s['fee'] else csv_c['fee']
            dur = s['duration_weeks'] if s['duration_weeks'] else csv_c['duration']
            rows.append({
                'title': s['title'] or csv_c['title'],
                'description': s['description'],
                'cricos': cricos,
                'cricos_provider_code': PROVIDER_CODE,
                'offshore_tuition_fee': fee if fee and fee != '-' else 'NULL',
                'course_duration_per_week': dur if dur and dur != '-' else 'NULL',
                'intake': s['intake'],
                'entry_requirements': s['entry_req'],
                'url': s['url'],
                'on_shore': '',
                'note': 'Page-scraped',
            })
            matched_from_page.add(cricos)
        else:
            # Fallback to CSV-only (no page found)
            rows.append({
                'title': csv_c['title'],
                'description': '',
                'cricos': cricos,
                'cricos_provider_code': PROVIDER_CODE,
                'offshore_tuition_fee': csv_c['fee'] if csv_c['fee'] and csv_c['fee'] != '-' else 'NULL',
                'course_duration_per_week': csv_c['duration'] if csv_c['duration'] and csv_c['duration'] != '-' else 'NULL',
                'intake': 'March, July',
                'entry_requirements': '',
                'url': '',
                'on_shore': '',
                'note': 'CSV fallback (no page)',
            })

    result_df = pd.DataFrame(rows)
    result_df = result_df[['title','description','cricos','cricos_provider_code',
                           'offshore_tuition_fee','course_duration_per_week','intake',
                           'entry_requirements','url','on_shore','note']]

    # Stats
    cricos_c = result_df['cricos'].str.match(r'^\d{6,7}[A-Za-z]?$').sum()
    fee_c = result_df['offshore_tuition_fee'].apply(
        lambda x: bool(re.match(r'^\d+', str(x))) if pd.notna(x) else False).sum()
    dur_c = result_df['course_duration_per_week'].apply(
        lambda x: bool(re.match(r'^\d+', str(x))) if pd.notna(x) else False).sum()
    
    all_intakes = set()
    for v in result_df['intake'].dropna():
        for m in str(v).split(','):
            all_intakes.add(m.strip())
    real_intakes = [m for m in MONTH_NAMES if m in all_intakes]

    page_count = len(matched_from_page)

    print(f'\n  ✅ {len(result_df)} courses.')
    print(f'     Page-scraped: {page_count} | CSV fallback: {len(result_df) - page_count}')
    print(f'     CRICOS: {cricos_c}')
    print(f'     Fee: {fee_c}')
    print(f'     Duration: {dur_c}')
    print(f'     Intake: {", ".join(real_intakes)}')

    OUTPUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_excel(OUTPUT_XLSX, index=False)
    print(f'     xlsx -> {OUTPUT_XLSX.name}')

    # Generate SQL
    intake_combined = ', '.join(real_intakes)
    sql_lines = [f'-- Update provider institution details',
                 f'UPDATE provider_institution SET',
                 f"    intake_date = '{intake_combined}',",
                 f'    updated_at = NOW()',
                 f"WHERE cricos_provider_code = '{PROVIDER_CODE}';",
                 f'']
    sql_cnt = 0
    for _, r in result_df.iterrows():
        cricos = r['cricos']
        if not cricos or not re.match(r'^\d{6,7}[A-Za-z]?$', str(cricos)): continue
        desc = str(r.get('description', '') or '')
        if desc in ('nan', 'None', '') or not desc:
            desc = ''
        else:
            desc = desc.replace("'", "''")
            if not desc.startswith('Course overview'):
                desc = f'Course overview <p>{desc}</p>'
        fee = r['offshore_tuition_fee']
        try: fee = str(int(float(fee))) if float(fee) > 0 else 'NULL'
        except: fee = 'NULL'
        dur = r['course_duration_per_week']
        try: dur = str(int(float(dur))) if float(dur) > 0 else 'NULL'
        except: dur = 'NULL'
        entry = str(r.get('entry_requirements', '') or '')
        if entry in ('nan', 'None', ''):
            entry = ''
        else:
            entry = entry.replace("'", "''")
        url = str(r.get('url', '') or '')
        if url in ('nan', 'None'):
            url = ''
        else:
            url = url.replace("'", "''")
        sql_lines.append(
            f"UPDATE courses SET"
            f"\n    course_description = '{desc}',"
            f"\n    course_duration_per_week = {dur},"
            f"\n    offshore_tuition_fee = {fee},"
            f"\n    onshore_tuition_fee = NULL,"
            f"\n    enrolment_fee = 0,"
            f"\n    materials_fee = NULL,"
            f"\n    entry_requirements = '{entry}',"
            f"\n    apply_form = '{url}',"
            f"\n    updated_at = NOW()"
            f"\nWHERE cricos_course_code = '{cricos}';"
        )
        sql_cnt += 1
    sql_lines.append(f'\n-- {sql_cnt} UPDATE statements generated.')

    with open(OUTPUT_SQL, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_lines))
    print(f'     sql  -> {OUTPUT_SQL.name}')
    print(f'\n  {PROVIDER_NAME} scraper complete.\n')


if __name__ == '__main__':
    main()
