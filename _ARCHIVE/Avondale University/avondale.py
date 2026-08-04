"""
Avondale University — www.avondale.edu.au.

Cloudflare (bypass with curl_cffi). SSR course pages with CRICOS in spans.
Fee on separate page only. Course sitemap: /course-sitemap.xml (34 URLs).

Provider: 02731D, CSV: 21 courses.

Hybrid: page-scrape for CRICOS, duration, intake; CSV fallback for fee.
"""
import sys, re, csv, time
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

PROVIDER_CODE = '02731D'
PROVIDER_NAME = 'Avondale University'
PROVIDER_DIR = Path(__file__).resolve().parent
SLUG = 'avondale'
OUTPUT_XLSX = PROVIDER_DIR / f'{SLUG}.xlsx'
OUTPUT_SQL = PROVIDER_DIR / f'{SLUG}_courses_update.sql'
REGISTER_CSV = PROVIDER_DIR.parent / 'cricos-courses.csv'
DOMAIN = 'https://www.avondale.edu.au'
COURSE_SITEMAP = 'https://www.avondale.edu.au/course-sitemap.xml'

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

def months_in_text(text):
    months = [m for m in MONTH_ORDER if re.search(rf'\b{m}\b', text or '')]
    if months: return months
    t = (text or '').lower()
    if re.search(r'semester\s*1', t): months.append('February')
    if re.search(r'semester\s*2', t): months.append('July')
    if not months:
        if re.search(r'semester|trimester', t):
            months = ['February', 'July']
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

def cricos_in_span(soup):
    """Extract CRICOS code from visible span on course page."""
    for span in soup.find_all('span'):
        txt = span.get_text(strip=True)
        for m in re.finditer(r'(0?\d{5}[A-Z])', txt):
            code = m.group(1)
            if len(code) == 7:
                if code[0] == '0':
                    code = code[1:]  # Some have leading 0
                else:
                    code = '0' + code  # Some lack leading 0
            # Check context - avoid footer provider code
            parent = span.find_parent(['div', 'section'])
            txt_lower = txt.lower()
            if 'provider' not in txt_lower and 'cricos' not in txt_lower:
                return code
    return ''

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

        # CRICOS from title matching (CSV is authoritative)
        matched = match_cricos(result['title'], register)
        if matched:
            result['cricos'] = matched
            result['source'] = 'page_title_match'
        else:
            # Fallback: try span extraction
            code = cricos_in_span(s)
            if code and len(code) == 6 and code[0].isdigit():
                result['cricos'] = code
                result['source'] = 'page_scrape'
                # Verify it's in register
                if code not in register:
                    result['note'] = f'CRICOS {code} not in CSV register'
            else:
                result['note'] = 'no CRICOS match from CSV or page'

        # Duration from page
        years = None
        # Check common patterns
        for dt in s.find_all(['dt', 'th', 'strong']):
            dtxt = dt.get_text(strip=True).lower()
            if 'duration' in dtxt or 'length' in dtxt:
                dd = dt.find_next_sibling(['dd', 'td'])
                if dd: years = parse_years(dd.get_text(strip=True))
                break
        if not years:
            for m in re.finditer(r'(\d+[.\d]*)\s*year', body, re.I):
                ctx = body[max(0,m.start()-40):m.end()+40].lower()
                if 'full-time' in ctx or 'program' in ctx or 'course' in ctx:
                    y = parse_years(m.group())
                    if y and (not years or y > years):
                        years = y
            if not years:
                # Try 3-year, 2-year etc
                for m in re.finditer(r'\b(\d)\s*year\b', body, re.I):
                    ctx = body[max(0,m.start()-30):m.end()+30].lower()
                    if 'full-time' in ctx or 'program' in ctx or 'course' in ctx:
                        y = parse_years(m.group())
                        if y and (not years or y > years):
                            years = y
        if years:
            result['course_duration_per_week'] = str(int(round(years * 52)))

        # Intake from page
        for dt in s.find_all(['dt', 'th', 'strong', 'span']):
            dtxt = dt.get_text(strip=True).lower()
            if any(k in dtxt for k in ['start', 'intake', 'commence', 'session', 'semester']):
                parent = dt.find_parent('div')
                txt = parent.get_text(strip=True) if parent else dt.get_text(strip=True)
                result['intake_months'] = months_in_text(txt)
                if result['intake_months']:
                    break
        if not result['intake_months']:
            for m in re.finditer(r'Semester\s*[12]|Semester\s+\w+', body):
                result['intake_months'] = months_in_text(m.group())
                if result['intake_months']:
                    break
        if not result['intake_months']:
            # Check for enrollment periods like "February 2025, July 2025"
            dates = re.findall(r'\b(February|July|March|January|October)\s+\d{4}', body)
            if dates:
                months = []
                for d in dates:
                    m = d.split()[0]
                    if m not in months: months.append(m)
                # Keep order
                result['intake_months'] = [m for m in MONTH_ORDER if m in months]

        # Fee from register
        if result['cricos'] and result['cricos'] in register:
            reg = register[result['cricos']]
            fee = reg.get('Tuition Fee', '').replace('$', '').replace(',', '')
            if fee:
                result['offshore_tuition_fee'] = clean_numeric_fee(fee)
            dur = re.sub(r'[^\d]', '', reg.get('Duration (Weeks)') or '')
            if dur and dur.isdigit() and not result['course_duration_per_week']:
                result['course_duration_per_week'] = dur
            nt = reg.get('Non Tuition Fee', '').replace('$', '').replace(',', '')
            if nt and re.match(r'^\d', nt):
                result['enrolment_fee'] = clean_numeric_fee(nt)

        # Description from page
        meta_desc = s.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            d = meta_desc['content'].strip()
            if len(d) > 20:
                result['course_description'] = clean_html(f'<h4>Course overview</h4><p>{d}</p>')

        status = '✅' if result['cricos'] else '⚠️'
        print(f'{status} {result["title"][:44]:44} → {result["cricos"] or "—"} | '
              f'fee {result["offshore_tuition_fee"]} | {result["course_duration_per_week"] or "?"}w | '
              f'intake {", ".join(result["intake_months"])}')
    except Exception as e:
        result['note'] = f'error: {e}'
        print(f'❌ {url}: {e}')
    return result

def main():
    print(f'\n  {PROVIDER_NAME} Scraper\n  {"="*40}\n  Provider: {PROVIDER_CODE}')

    register = load_register()
    print(f'  CSV courses for {PROVIDER_CODE}: {len(register)}')

    # Course URLs from sitemap
    resp = get_page(COURSE_SITEMAP)
    course_urls = re.findall(r'<loc>(.*?)</loc>', resp.text)
    print(f'  Course URLs: {len(course_urls)}')

    results = []
    for url in course_urls:
        r = scrape_course(url, register)
        results.append(r)

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
        })

    # XLSX
    seen = set()
    xd = []
    for d in results:
        if d['cricos']:
            if d['cricos'] in seen: continue
            seen.add(d['cricos'])
        xd.append(d)
    def cell(v):
        v = '' if v in (None, 'NULL') else str(v).replace("''", "'")
        return v[:32000]
    pdf = [{'cricos': d['cricos'], 'title': d['title'], 'url': d['url'],
            'course_duration_per_week': int(d['course_duration_per_week']) if str(d['course_duration_per_week']).isdigit() else '',
            'offshore_tuition_fee': cell(d['offshore_tuition_fee']),
            'onshore_tuition_fee': cell(d['onshore_tuition_fee']),
            'enrolment_fee': cell(d['enrolment_fee']),
            'materials_fee': cell(d['materials_fee']),
            'intake': ', '.join(d['intake_months']),
            'course_description': cell(d['course_description']),
            'entry_requirements': cell(d['entry_requirements']),
            'source': d['source'],
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
    pc = sum(1 for d in results if d['source'] != 'register' and d['cricos'])
    rc = sum(1 for d in results if d['source'] == 'register')
    nc = sum(1 for d in results if not d['cricos'])
    total = len(emitted)
    print(f'\n  ✅ {total} courses ({pc} page, {rc} register, {nc} no CRICOS). Intake: {intake_date}')
    print(f'  {PROVIDER_NAME} scraper complete.\n')

if __name__ == '__main__':
    main()
