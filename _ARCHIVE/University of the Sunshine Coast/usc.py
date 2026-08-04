"""
University of the Sunshine Coast (USC / UniSC) — www.unisc.edu.au.

Cloudflare (bypassable). SSR course pages. CRICOS from CSV.
Sitemap: /XMLsitemap (39K URLs, ~500 course detail pages)

Provider: 01595D, CSV: 147 courses
"""
import sys, re, csv, time
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

PROVIDER_CODE = '01595D'
PROVIDER_NAME = 'University of the Sunshine Coast (UniSC)'
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = 'usc'
OUTPUT_XLSX = PROVIDER_DIR / f'{SLUG}.xlsx'
OUTPUT_SQL = PROVIDER_DIR / f'{SLUG}_courses_update.sql'
REGISTER_CSV = PROVIDER_DIR.parent / 'cricos-courses.csv'
DOMAIN = 'https://www.unisc.edu.au'

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

def months_in_trimester(text):
    months = [m for m in MONTH_ORDER if re.search(rf'\b{m}\b', text or '')]
    if months: return months
    t = (text or '').lower()
    if re.search(r'trimester\s*1', t): months.append('March')
    if re.search(r'trimester\s*2', t): months.append('July')
    if re.search(r'trimester\s*3', t): months.append('November')
    if not months and re.search(r'trimester|semester', t):
        months = ['March', 'July']
    return months

def parse_years(text):
    m = re.search(r'(\d+[.\d]*)\s*year', text or '', re.I)
    return float(m.group(1)) if m else None

def load_register():
    reg = {}
    with open(REGISTER_CSV, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if r['CRICOS Provider Code'].strip() != PROVIDER_CODE: continue
            if r['Expired'].strip().lower() == 'yes': continue
            reg[r['CRICOS Course Code'].strip()] = r
    return reg

def match_cricos(title, register):
    if not title: return ''
    tn = re.sub(r'[^a-z0-9]+', ' ', title.lower()).strip()
    tw = set(tn.split())
    best_score = 0.0
    best_code = ''
    for code, reg in register.items():
        cn = re.sub(r'[^a-z0-9]+', ' ', reg['Course Name'].lower()).strip()
        cw = set(cn.split())
        if not cw: continue
        score = len(tw & cw) / len(tw | cw)
        if score > best_score:
            best_score = score
            best_code = code
    return best_code if best_score >= 0.4 else ''

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

        h1 = s.find('h1')
        result['title'] = h1.get_text(strip=True) if h1 else url.split('/')[-1].replace('-', ' ').title()
        result['title'] = re.sub(r'\s*[–\-]\s*(?:UniSC|University of the Sunshine Coast).*', '', result['title']).strip()

        meta_desc = s.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            d = meta_desc['content'].strip()
            if len(d) > 20:
                result['course_description'] = clean_html(f'<h4>Course overview</h4><p>{d}</p>')

        # Duration
        for dt in s.find_all(['dt', 'th']):
            if 'duration' in dt.get_text(strip=True).lower():
                dd = dt.find_next_sibling(['dd', 'td'])
                if dd:
                    years = parse_years(dd.get_text(strip=True))
                    if years:
                        result['course_duration_per_week'] = str(int(round(years * 52)))
                    break
        if not result['course_duration_per_week']:
            for m in re.finditer(r'(\d+[.\d]*)\s*year', body, re.I):
                ctx = body[max(0,m.start()-40):m.end()+40]
                if 'full-time' in ctx.lower() or 'program' in ctx.lower() or 'course' in ctx.lower():
                    years = parse_years(m.group())
                    if years:
                        result['course_duration_per_week'] = str(int(round(years * 52)))
                    break

        # Intake
        for dt in s.find_all(['dt', 'th']):
            txt = dt.get_text(strip=True).lower()
            if any(k in txt for k in ['intake', 'start', 'commence', 'session', 'trimester']):
                dd = dt.find_next_sibling(['dd', 'td'])
                if dd:
                    result['intake_months'] = months_in_trimester(dd.get_text(strip=True))
                    break
        if not result['intake_months']:
            tt = ''
            for m in re.finditer(r'Trimester\s*[12]', body):
                tt += ' ' + m.group()
            if tt:
                result['intake_months'] = months_in_trimester(tt)

        # Match CRICOS from CSV
        matched = match_cricos(result['title'], register)
        if matched:
            result['cricos'] = matched
            reg = register[matched]
            fee = reg.get('Tuition Fee', '').replace('$', '').replace(',', '')
            if fee:
                result['offshore_tuition_fee'] = clean_numeric_fee(fee)
            dur = re.sub(r'[^\d]', '', reg.get('Duration (Weeks)') or '')
            if dur and dur.isdigit() and not result['course_duration_per_week']:
                result['course_duration_per_week'] = dur
            nt = reg.get('Non Tuition Fee', '').replace('$', '').replace(',', '')
            if nt and re.match(r'^\d', nt):
                result['enrolment_fee'] = clean_numeric_fee(nt)
            result['source'] = 'page_csv'
        else:
            result['note'] = 'no CRICOS match from CSV'

        status = '✅' if result['cricos'] else '⚠️'
        print(f'{status} {result["title"][:44]:44} → {result["cricos"] or "—"} | '
              f'fee {result["offshore_tuition_fee"]} | {result["course_duration_per_week"] or "?"}w')
    except Exception as e:
        result['note'] = f'error: {e}'
        print(f'❌ {url}: {e}')
    return result

def main():
    print(f'\n  {PROVIDER_NAME} Scraper\n  {"="*40}\n  Provider: {PROVIDER_CODE}')

    register = load_register()
    print(f'  CSV courses for {PROVIDER_CODE}: {len(register)}')

    # Get course detail URLs from sitemap (depth-4 = course pages)
    resp = get_page('https://www.unisc.edu.au/XMLsitemap')
    all_urls = re.findall(r'<loc>(.*?)</loc>', resp.text)
    course_urls = [u for u in all_urls 
                   if '/study/courses-and-programs/' in u 
                   and len(u.replace(DOMAIN, '').strip('/').split('/')) == 4]
    print(f'  Course detail URLs: {len(course_urls)}')

    # Scrape (limit to avoid rate limit)
    MAX_PAGES = 300
    results = []
    for url in course_urls[:MAX_PAGES]:
        r = scrape_course(url, register)
        results.append(r)
    if len(course_urls) > MAX_PAGES:
        print(f'  (limited to {MAX_PAGES} pages)')

    # Intake
    months = set()
    for d in results:
        months.update(d['intake_months'])
    intake_date = ', '.join(m for m in MONTH_ORDER if m in months)

    # Register backfill
    scraped = {d['cricos'] for d in results if d['cricos']}
    for code, reg in register.items():
        if code in scraped: continue
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

    # XLSX (dedup by CRICOS)
    seen = set()
    def cell(v):
        v = '' if v in (None, 'NULL') else str(v).replace("''", "'")
        return v[:32000]
    xd = []
    for d in results:
        if d['cricos']:
            if d['cricos'] in seen: continue
            seen.add(d['cricos'])
        xd.append(d)
    pdf = [{'cricos': d['cricos'], 'title': d['title'], 'url': d['url'],
            'course_duration_per_week': int(d['course_duration_per_week']) if str(d['course_duration_per_week']).isdigit() else '',
            'offshore_tuition_fee': cell(d['offshore_tuition_fee']),
            'onshore_tuition_fee': cell(d['onshore_tuition_fee']),
            'enrolment_fee': cell(d['enrolment_fee']),
            'materials_fee': cell(d['materials_fee']),
            'intake': ', '.join(d['intake_months']),
            'course_description': cell(d['course_description']),
            'entry_requirements': cell(d['entry_requirements']),
            'source': d['source'], 'note': d['note'],
        } for d in xd]
    pd.DataFrame(pdf).to_excel(OUTPUT_XLSX, index=False)

    # SQL
    emitted = set()
    with open(OUTPUT_SQL, 'w', encoding='utf-8') as f:
        f.write('-- Update provider institution details\n'
                'UPDATE provider_institution SET\n'
                f"    intake_date = '{intake_date}',\n    updated_at = NOW()\n"
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")
        for d in results:
            if not d['cricos'] or d['cricos'] in emitted: continue
            emitted.add(d['cricos'])
            dur = d['course_duration_per_week'] if str(d['course_duration_per_week']).isdigit() else 'NULL'
            fee = d['offshore_tuition_fee'] if d['offshore_tuition_fee'] not in (None, 'NULL', '') else 'NULL'
            desc = d['course_description'].replace("'", "''")
            entry = d['entry_requirements'].replace("'", "''")
            url = d['url'].replace("'", "''")
            enr = d['enrolment_fee'] if d['enrolment_fee'] not in (None, 'NULL', '') else 'NULL'
            if d['source'] == 'register':
                f.write(f"-- Register-only: {d['title']}\n"
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

    print(f'     xlsx -> {OUTPUT_XLSX.name}')
    print(f'     sql  -> {OUTPUT_SQL.name}')
    pc = sum(1 for d in results if d['source'].startswith('page') and d['cricos'])
    rc = sum(1 for d in results if d['source'] == 'register')
    nc = sum(1 for d in results if not d['cricos'])
    print(f'\n  ✅ {len(emitted)} courses ({pc} page, {rc} register, {nc} no CRICOS). Intake: {intake_date}')
    print(f'  {PROVIDER_NAME} scraper complete.\n')

if __name__ == '__main__':
    main()
