"""
Southern Cross University (SCU) — www.scu.edu.au.

Site: CloudFront (no Cloudflare). SSR course pages with fee, duration, intake.
CRICOS course codes are JS-loaded (availability tables); fallback to CSV.

Provider: 01241G
Course URLs: 352 from sitemap (/google-sitemap/index.xml)
CSV coverage: 149 courses

Hybrid strategy:
- Page-scrape: title, description, duration, intake, fee (visible in SSR)
- CSV fallback: CRICOS course code, non-tuition fee
- Register backfill: any CRICOS in CSV not covered by page scrape
"""
import sys, re, csv, json, time
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

PROVIDER_CODE = '01241G'
PROVIDER_NAME = 'Southern Cross University (SCU)'
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = 'scu'
OUTPUT_XLSX = PROVIDER_DIR / f'{SLUG}.xlsx'
OUTPUT_SQL = PROVIDER_DIR / f'{SLUG}_courses_update.sql'
REGISTER_CSV = PROVIDER_DIR.parent / 'cricos-courses.csv'
SITEMAP = 'https://www.scu.edu.au/google-sitemap/index.xml'
DOMAIN = 'https://www.scu.edu.au'

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

def months_in_snapshot(text):
    """Detect months from snapshot boxes on SCU pages (e.g. March, July, October)."""
    months = [m for m in MONTH_ORDER if re.search(rf'\b{m}\b', text or '')]
    if months: return months
    # Map trimester/semester
    t = (text or '').lower()
    if re.search(r'trimester\s*1', t): months.append('March')
    if re.search(r'trimester\s*2', t): months.append('July')
    if re.search(r'trimester\s*3', t): months.append('November')
    if not months and re.search(r'trimester|semester', t):
        months = ['March', 'July']
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

def match_cricos_from_csv(title, register):
    """Try to match a course title from the page to a CRICOS course code in the register."""
    if not title: return ''
    title_norm = re.sub(r'[^a-z0-9]+', ' ', title.lower()).strip()
    title_words = set(title_norm.split())
    
    best_score = 0.0
    best_code = ''
    
    for code, reg in register.items():
        cname = reg.get('Course Name', '')
        cname_norm = re.sub(r'[^a-z0-9]+', ' ', cname.lower()).strip()
        cname_words = set(cname_norm.split())
        if not cname_words: continue
        inter = title_words & cname_words
        union = title_words | cname_words
        score = len(inter) / len(union) if union else 0
        if score > best_score:
            best_score = score
            best_code = code
    
    return best_code if best_score >= 0.45 else ''

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
        # Remove " - 2026 - SCU" suffix
        result['title'] = re.sub(r'\s*-\s*\d{4}\s*-\s*(?:SCU|Southern Cross University).*', '', result['title']).strip()

        # Description from meta description
        meta_desc = s.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            desc = meta_desc['content'].strip()
            if desc and len(desc) > 20:
                result['course_description'] = clean_html(f'<h4>Course overview</h4><p>{desc}</p>')

        # Duration from snapshot
        for div in s.find_all(['div', 'dd']):
            txt = div.get_text(strip=True)
            if 'year' in txt and ('full-time' in txt or 'duration' in txt.lower()):
                years = parse_years(txt)
                if years:
                    result['course_duration_per_week'] = str(int(round(years * 52)))
                break

        # Intake from snapshot
        for div in s.find_all('div', class_=lambda c: c and 'snapshot' in c.lower()):
            txt = div.get_text(' ', strip=True)
            result['intake_months'] = months_in_snapshot(txt)
            if result['intake_months']:
                break
        if not result['intake_months']:
            # Also check dt/dd pairs
            for dt in s.find_all('dt'):
                if 'start' in dt.get_text(strip=True).lower() or 'intake' in dt.get_text(strip=True).lower():
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        result['intake_months'] = months_in_snapshot(dd.get_text(strip=True))
                        break
        
        # Fee from snapshot data
        fee_text = ''
        for tag in s.find_all(['div', 'span', 'p', 'dd']):
            txt = tag.get_text(strip=True)
            if re.search(r'\$\s*[\d,]+', txt) and ('fee' in txt.lower() or 'tuition' in txt.lower() or 'per unit' in txt.lower()):
                fee_text = txt
                break
        
        # Extract international fee from page text
        intl_fee = None
        for m in re.finditer(r'(\$[\s\d,]+(?:\.\d{2})?)', fee_text or body):
            ctx = body[max(0,m.start()-60):m.end()+60]
            if 'international' in ctx.lower() or 'intl' in ctx.lower() or 'per unit' in ctx.lower():
                val = clean_numeric_fee(m.group(1))
                if val != 'NULL' and int(val) >= 100:
                    intl_fee = val
                    break
        
        if intl_fee:
            result['offshore_tuition_fee'] = intl_fee
        
        # Try to match CRICOS from CSV register using page title
        matched_code = match_cricos_from_csv(result['title'], register)
        if matched_code:
            result['cricos'] = matched_code
            reg = register[matched_code]
            # Fee from CSV if not found on page
            if result['offshore_tuition_fee'] == 'NULL':
                fee = reg.get('Tuition Fee', '').replace('$', '').replace(',', '')
                if fee:
                    result['offshore_tuition_fee'] = clean_numeric_fee(fee)
            # Duration from CSV if not found on page
            if not result['course_duration_per_week']:
                dur = re.sub(r'[^\d]', '', reg.get('Duration (Weeks)') or '')
                if dur and dur.isdigit():
                    result['course_duration_per_week'] = dur
            # Non-tuition fee
            nt = reg.get('Non Tuition Fee', '').replace('$', '').replace(',', '')
            if nt and re.match(r'^\d', nt):
                result['enrolment_fee'] = clean_numeric_fee(nt)
            result['source'] = 'page_csv'
        else:
            result['note'] = 'no CRICOS match from CSV'
            result['source'] = 'page_no_cricos'

        status = '✅' if result['cricos'] else '⚠️'
        print(f'{status} {result["title"][:44]:44} → {result["cricos"] or "—"} | '
              f'fee {result["offshore_tuition_fee"]} | {result["course_duration_per_week"] or "?"}w | '
              f'intake {", ".join(result["intake_months"])}')
    except Exception as e:
        result['note'] = f'error: {e}'
        print(f'❌ {url}: {e}')
    return result

def main():
    print(f'\n  {PROVIDER_NAME} Scraper')
    print(f'  {"="*40}')
    print(f'  Provider: {PROVIDER_CODE}')

    # Load register
    register = load_register()
    print(f'  CSV courses for {PROVIDER_CODE}: {len(register)}')

    # Get course URLs from sitemap
    resp = get_page(SITEMAP)
    all_urls = re.findall(r'<loc>(.*?)</loc>', resp.text)
    course_urls = [u for u in all_urls if '/study/courses/' in u]
    print(f'  Course URLs from sitemap: {len(course_urls)}')

    # Scrape
    results = []
    for url in course_urls:
        r = scrape_course(url, register)
        results.append(r)

    # Aggregate intake
    months = set()
    for d in results:
        months.update(d['intake_months'])
    intake_date = ', '.join(m for m in MONTH_ORDER if m in months)

    # Register backfill
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
                        f"    materials_fee = NULL,\n"
                        f"    entry_requirements = '{entry}',\n"
                        f"    apply_form = '{url}',\n"
                        f"    updated_at = NOW()\n"
                        f"WHERE cricos_course_code = '{d['cricos']}';\n\n")

    print(f'     sql  -> {OUTPUT_SQL.name}')
    page_count = sum(1 for d in results if d['source'].startswith('page'))
    reg_count = sum(1 for d in results if d['source'] == 'register')
    no_cricos_count = sum(1 for d in results if not d['cricos'])
    total = len(emitted)
    print(f'\n  ✅ {total} courses ({page_count} page, {reg_count} register, {no_cricos_count} no CRICOS). '
          f'Intake: {intake_date}')
    print(f'  {PROVIDER_NAME} scraper complete.\n')

if __name__ == '__main__':
    main()
