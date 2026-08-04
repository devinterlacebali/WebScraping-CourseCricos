"""
The University of Notre Dame Australia — www.notredame.edu.au.

Site: No Cloudflare, SSR course pages with rich meta tags.
Meta tags provide: program CRICOS, duration, commencement, description.
Fee amounts are JS-loaded; fallback to CSV.

Provider: 01032F
Course URLs: 208 from sitemap (/programs/{school}/{level}/{slug})
CSV coverage: 133 courses
"""
import sys, re, csv, json, time
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

PROVIDER_CODE = '01032F'
PROVIDER_NAME = 'The University of Notre Dame Australia'
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = 'notredame'
OUTPUT_XLSX = PROVIDER_DIR / f'{SLUG}.xlsx'
OUTPUT_SQL = PROVIDER_DIR / f'{SLUG}_courses_update.sql'
REGISTER_CSV = PROVIDER_DIR.parent / 'cricos-courses.csv'
SITEMAP = 'https://www.notredame.edu.au/sitemap.xml'
DOMAIN = 'https://www.notredame.edu.au'

MONTH_ORDER = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

def clean_numeric_fee(val):
    if val is None or str(val).strip().lower() in ("nan", "null", "n/a", "", "none", "-"):
        return "NULL"
    v = re.sub(r"[^\d\.]", "", str(val))
    if not v: return "NULL"
    n = float(v)
    return str(int(n)) if n >= 100 else "NULL"

def clean_html(html):
    if not html: return ''
    return re.sub(r'\s+', ' ', html).replace("'", "''").strip()

def get_page(url, tries=3):
    for i in range(tries):
        try:
            return curl.get(url, impersonate='chrome120', timeout=30)
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(1.5 * (i+1))

def months_in(text):
    months = [m for m in MONTH_ORDER if re.search(rf'\b{m}\b', text or '')]
    if not months:
        # Map semester patterns to months
        t = (text or '').lower()
        if re.search(r'semester\s*1|semester\s*one|february|feb\b', t):
            months.append('February')
            if re.search(r'semester\s*2|semester\s*two|july|jul\b', t):
                months.append('July')
            elif re.search(r'june|jun\b', t):
                months.append('June')
        elif re.search(r'trimester|trimester\s*1|march|mar\b', t):
            months.append('March')
            if re.search(r'trimester\s*2|july|jul\b', t):
                months.append('July')
        if not months:
            # Generic semester detection
            if re.search(r'semester', t):
                months = ['February', 'July']
    return months

def parse_years(text):
    m = re.search(r'(\d+[.\d]*)\s*year', text or '', re.I)
    if m: return float(m.group(1))
    m = re.search(r'(\d+[.\d]*)\s*month', text or '', re.I)
    return float(m.group(1)) / 12 if m else None

def load_register():
    reg = {}
    with open(REGISTER_CSV, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if r['CRICOS Provider Code'].strip() != PROVIDER_CODE: continue
            if r['Expired'].strip().lower() == 'yes': continue
            reg[r['CRICOS Course Code'].strip()] = r
    return reg

def scrape_course(url, register):
    result = {'cricos': '', 'title': '', 'url': url, 'course_description': '',
              'course_duration_per_week': '', 'offshore_tuition_fee': 'NULL',
              'onshore_tuition_fee': 'NULL', 'enrolment_fee': 'NULL',
              'materials_fee': 'NULL', 'entry_requirements': '',
              'apply_form': url, 'intake_months': [], 'source': 'page', 'note': ''}
    try:
        resp = get_page(url)
        s = BeautifulSoup(resp.text, 'html.parser')
        body = resp.text

        # Title
        h1 = s.find('h1')
        result['title'] = h1.get_text(strip=True) if h1 else url.split('/')[-1].replace('-', ' ').title()

        # CRICOS from meta tag
        meta_cricos = s.find('meta', attrs={'name': lambda x: x and 'CRICOS' in x.upper()})
        if meta_cricos and meta_cricos.get('content'):
            result['cricos'] = meta_cricos['content'].strip()

        # Duration from meta
        meta_dur = s.find('meta', attrs={'name': lambda x: x and 'duration' in (x or '').lower()})
        if meta_dur and meta_dur.get('content'):
            years = parse_years(meta_dur['content'])
            if years:
                result['course_duration_per_week'] = str(int(round(years * 52)))

        # Intake from meta
        meta_com = s.find('meta', attrs={'name': lambda x: x and 'commencement' in (x or '').lower()})
        if meta_com and meta_com.get('content'):
            result['intake_months'] = months_in(meta_com['content'])

        # Description from meta description
        meta_desc = s.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            result['course_description'] = clean_html(
                f'<h4>Course overview</h4><p>{meta_desc["content"]}</p>')

        # Fee from CSV register match
        if result['cricos'] and result['cricos'] in register:
            reg = register[result['cricos']]
            fee = reg.get('Tuition Fee', '').replace('$', '').replace(',', '')
            dur_reg = re.sub(r'[^\d]', '', reg.get('Duration (Weeks)', '') or '')
            if dur_reg and not result['course_duration_per_week']:
                result['course_duration_per_week'] = dur_reg
            if fee:
                result['offshore_tuition_fee'] = clean_numeric_fee(fee)
            non_tuition = reg.get('Non Tuition Fee', '').replace('$', '').replace(',', '')
            if non_tuition and re.match(r'^\d', non_tuition):
                result['enrolment_fee'] = clean_numeric_fee(non_tuition)

        # Entry requirements from page (look for admission/entry sections)
        for h in s.find_all(['h2', 'h3', 'h4']):
            txt = h.get_text(strip=True).lower()
            if 'admission requirement' in txt or 'entry requirement' in txt or 'academic entry' in txt:
                els = []
                for sibling in h.find_next_siblings():
                    if sibling.name and sibling.name.startswith('h'): break
                    if sibling.name in ['p', 'ul', 'ol', 'div']:
                        txt_s = sibling.get_text(strip=True)
                        if len(txt_s) > 20:
                            els.append(str(sibling))
                if els:
                    result['entry_requirements'] = clean_html('<h4>Entry Requirements</h4>' + ''.join(els))
                break

        # Note
        if not result['cricos']:
            result['note'] = 'no CRICOS in meta tag'
            result['source'] = 'page_no_cricos'

        status = '✅' if result['cricos'] else '⚠️'
        print(f'{status} {result["title"][:44]:44} → {result["cricos"] or "—"} | '
              f'fee {result["offshore_tuition_fee"]} | {result["course_duration_per_week"] or "?"}w')
    except Exception as e:
        result['note'] = f'error: {e}'
        print(f'❌ {url}: {e}')
    return result

def main():
    print(f'\n  {PROVIDER_NAME} Scraper')
    print(f'  {"="*40}')
    print(f'  Provider: {PROVIDER_CODE}')

    # Load register for fee backfill
    register = load_register()
    print(f'  CSV courses for {PROVIDER_CODE}: {len(register)}')

    # Get course URLs from sitemap
    resp = get_page(SITEMAP)
    all_urls = re.findall(r'<loc>(.*?)</loc>', resp.text)
    pat = r'/programs/[^/]+/(undergraduate|postgraduate|vet|research|microcredential|online)/[a-z]'
    course_urls = [u for u in all_urls if re.search(pat, u)]
    print(f'  Course URLs from sitemap: {len(course_urls)}')

    # Scrape each course page
    results = []
    for url in course_urls:
        r = scrape_course(url, register)
        results.append(r)

    # Aggregate intake months
    months = set()
    for d in results:
        months.update(d['intake_months'])
    intake_date = ', '.join(m for m in MONTH_ORDER if m in months)

    # Register backfill for courses not on site scraper
    scraped_codes = {d['cricos'] for d in results if d['cricos']}
    for code, reg in register.items():
        if code in scraped_codes: continue
        weeks = re.sub(r'[^\d]', '', reg.get('Duration (Weeks)') or '')
        fee = reg.get('Tuition Fee', '').strip().replace('$', '').replace(',', '')
        results.append({
            'cricos': code, 'title': reg['Course Name'].strip(),
            'url': '', 'course_description': '',
            'course_duration_per_week': weeks if weeks.isdigit() else '',
            'offshore_tuition_fee': clean_numeric_fee(fee),
            'onshore_tuition_fee': 'NULL',
            'enrolment_fee': clean_numeric_fee(reg.get('Non Tuition Fee', '')),
            'materials_fee': 'NULL',
            'entry_requirements': '', 'apply_form': '',
            'intake_months': [], 'source': 'register',
            'note': 'not on site; from CRICOS register',
        })
        print(f'  📋 Register-only: {reg["Course Name"][:44]} → {code}')

    # Write XLSX
    def cell(v):
        v = '' if v in (None, 'NULL') else str(v).replace("''", "'")
        return v[:32000]
    
    xlsx_data = [{
        'cricos': d['cricos'], 'title': d['title'], 'url': d['url'],
        'course_duration_per_week': int(d['course_duration_per_week']) if str(d['course_duration_per_week']).isdigit() else '',
        'offshore_tuition_fee': cell(d['offshore_tuition_fee']),
        'onshore_tuition_fee': cell(d['onshore_tuition_fee']),
        'enrolment_fee': cell(d['enrolment_fee']),
        'materials_fee': cell(d['materials_fee']),
        'intake': ', '.join(d['intake_months']),
        'course_description': cell(d['course_description']),
        'entry_requirements': cell(d['entry_requirements']),
        'source': d['source'], 'note': d['note'],
    } for d in results]
    pd.DataFrame(xlsx_data).to_excel(OUTPUT_XLSX, index=False)
    print(f'     xlsx -> {OUTPUT_XLSX.name}')

    # Write SQL
    emitted = set()
    with open(OUTPUT_SQL, 'w', encoding='utf-8') as f:
        f.write('-- Update provider institution details\n'
                'UPDATE provider_institution SET\n'
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")

        for d in results:
            if not d['cricos']:
                f.write(f"-- ⚠️ Skipped ({d['note'] or 'no CRICOS'}): {d['title']} | {d['url']}\n\n")
                continue
            if d['cricos'] in emitted:
                f.write(f"-- ⚠️ Skipped (CRICOS {d['cricos']} already emitted): {d['title']}\n\n")
                continue
            emitted.add(d['cricos'])

            dur = d['course_duration_per_week'] if str(d['course_duration_per_week']).isdigit() else 'NULL'
            fee = d['offshore_tuition_fee'] if d['offshore_tuition_fee'] not in (None, 'NULL', '') else 'NULL'
            desc = d['course_description'].replace("'", "''")
            entry = d['entry_requirements'].replace("'", "''")
            url = d['url'].replace("'", "''")
            enr = d['enrolment_fee'] if d['enrolment_fee'] not in (None, 'NULL', '') else 'NULL'
            mat = d['materials_fee'] if d['materials_fee'] not in (None, 'NULL', '') else 'NULL'

            if d['source'] == 'register':
                f.write(f"-- Register-only (not on site scrape): {d['title']}\n"
                        f"UPDATE courses SET\n"
                        f"    course_duration_per_week = {dur},\n"
                        f"    offshore_tuition_fee = {fee},\n"
                        f"    enrolment_fee = {enr},\n"
                        f"    updated_at = NOW()\n"
                        f"WHERE cricos_course_code = '{d['cricos']}';\n\n")
            else:
                f.write(f"UPDATE courses SET\n"
                        f"    course_description = '{desc}',\n"
                        f"    course_duration_per_week = {dur},\n"
                        f"    offshore_tuition_fee = {fee},\n"
                        f"    onshore_tuition_fee = NULL,\n"
                        f"    enrolment_fee = {enr},\n"
                        f"    materials_fee = {mat},\n"
                        f"    entry_requirements = '{entry}',\n"
                        f"    apply_form = '{url}',\n"
                        f"    updated_at = NOW()\n"
                        f"WHERE cricos_course_code = '{d['cricos']}';\n\n")

    print(f'     sql  -> {OUTPUT_SQL.name}')
    page_count = sum(1 for d in results if d['source'] == 'page' and d['cricos'])
    reg_count = sum(1 for d in results if d['source'] == 'register')
    total = len(emitted)
    print(f'\n  ✅ {total} courses ({page_count} page, {reg_count} register). Intake: {intake_date}')
    print(f'  {PROVIDER_NAME} scraper complete.\n')

if __name__ == '__main__':
    main()
