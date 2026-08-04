"""
TasTAFE — www.tastafe.tas.edu.au (provider 03041M).

Squiz Matrix SSR.
Sitemap: /sitemap.xml → 662 URLs, ~192 course detail URLs.
Strategy: page-scrape hybrid from the international page course list + CSV register fallback.

Course pages (with ?tab=international) show:
  - CRICOS course code in page text (e.g. "CRICOS: 111020F")
  - CRICOS provider code 03041M in footer
  - International tuition fee ("International $29,495")
  - Duration in weeks (table)
  - Intake dates (e.g. "February & July")
  - Course overview HTML
"""
import re, sys, csv, time
from pathlib import Path
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import pandas as pd
from bs4 import BeautifulSoup
from curl_cffi import requests as curl_requests

PROVIDER_CODE = '03041M'
PROVIDER_NAME = 'TasTAFE'
BASE = 'https://www.tastafe.tas.edu.au'
DIR = Path(__file__).resolve().parent
SLUG = 'tastafe'
EXCEL_PATH = DIR / f'{SLUG}.xlsx'
SQL_PATH = DIR / f'{SLUG}_courses_update.sql'
REGISTER_CSV = DIR.parent / 'cricos-courses.csv'

MONTH_ORDER = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
MONTHS_LOWER = {m.lower(): m for m in MONTH_ORDER}

STOPWORDS = {'bachelor', 'master', 'graduate', 'diploma', 'certificate',
             'of', 'in', 'and', 'the', 'a', 'an', 'for', 'with', 'by', 'to', 'or',
             'advanced'}

ALLOWED_TAGS = {'p', 'ul', 'ol', 'li', 'strong', 'b', 'em', 'i', 'a', 'br', 'h5',
                'table', 'thead', 'tbody', 'tr', 'td', 'th'}


# ---------- helpers ----------
def clean_numeric(val):
    if val is None or str(val).strip().lower() in ('nan', 'null', 'n/a', '', 'none', '-'):
        return None
    v = re.sub(r'[^\d.]', '', str(val))
    if not v:
        return None
    n = float(v)
    return int(n) if n >= 100 else None


def fetch(url, retries=3):
    for attempt in range(retries):
        try:
            r = curl_requests.get(url, impersonate='chrome120', timeout=60)
            if r.status_code == 200:
                return r
            print(f'  ⚠️  {r.status_code} on attempt {attempt+1}: {url[:80]}')
        except Exception as e:
            print(f'  ⚠️  Error on attempt {attempt+1}: {e}')
        time.sleep(1.5)
    return None


def clean_html(html_text):
    if not html_text:
        return ''
    return re.sub(r'\s+', ' ', html_text).replace("'", "''").strip()


def sanitise_html(html_text):
    """Flatten into clean minimal semantic HTML."""
    if not html_text:
        return ''
    frag = BeautifulSoup(html_text or '', 'html.parser')
    for t in frag.find_all(['style', 'script', 'noscript', 'form', 'iframe', 'img', 'svg', 'button']):
        t.decompose()
    for t in frag.find_all(True):
        for a in list(t.attrs):
            if a != 'href':
                del t[a]
    for t in frag.find_all('span'):
        t.unwrap()
    while True:
        div = frag.find('div')
        if div is None:
            break
        if div.find(['p', 'ul', 'ol', 'li', 'div', 'table', 'h5']):
            div.unwrap()
        else:
            div.name = 'p'
    for t in frag.find_all(True):
        if t.name not in ALLOWED_TAGS:
            t.unwrap()
    return str(frag)


# ---------- CSV register ----------
def load_register():
    """Build {cricos: row} dict and {VET_code: cricos} dict."""
    by_code = {}
    by_vet = {}
    with open(REGISTER_CSV, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r['CRICOS Provider Code'].strip() != PROVIDER_CODE:
                continue
            if r.get('Expired', '').strip().lower() == 'yes':
                continue
            code = r['CRICOS Course Code'].strip()
            title = r['Course Name'].strip()
            dur_raw = r.get('Duration (Weeks)', '').strip()
            dur = re.sub(r'[^\d]', '', dur_raw) if dur_raw else ''
            fee_raw = r.get('Tuition Fee', '').strip().replace('$', '').replace(',', '')
            vet = r.get('VET National Code', '').strip()
            by_code[code] = {
                'cricos': code,
                'title': title,
                'vet': vet,
                'course_duration_per_week': int(dur) if dur.isdigit() else None,
                'offshore_tuition_fee': clean_numeric(fee_raw),
            }
            if vet:
                by_vet[vet.lower()] = code
    return by_code, by_vet


def match_cricos(page_title, register, threshold=0.45):
    """Word-overlap matching against CSV titles."""
    if not page_title:
        return ''
    norm = re.sub(r'[^a-z0-9]+', ' ', page_title.lower()).strip()
    page_words = set(w for w in norm.split() if w not in STOPWORDS)
    if not page_words:
        return ''
    local_th = 0.55 if len(page_words) < 4 else threshold
    best_score, best_code = 0.0, ''
    for code, row in register.items():
        cname = row['title']
        cnorm = re.sub(r'[^a-z0-9]+', ' ', cname.lower()).strip()
        cwords = set(w for w in cnorm.split() if w not in STOPWORDS)
        if not cwords:
            continue
        inter = page_words & cwords
        union = page_words | cwords
        score = len(inter) / len(union) if union else 0
        if score > best_score:
            best_score = score
            best_code = code
    return best_code if best_score >= local_th else best_code if best_score >= 0.35 else ''


# ---------- sitemap + international page course list ----------
def collect_international_courses():
    """
    Scrape the /international page which lists all CRICOS-registered courses
    with their CRICOS codes. Returns {cricos_code: {'title': ..., 'url': ...}}.
    """
    print('  📡 Fetching international course list...')
    r = fetch(f'{BASE}/international')
    if not r:
        print('  ❌ Failed to fetch /international')
        return {}, []
    soup = BeautifulSoup(r.text, 'html.parser')
    text = re.sub(r'\s+', ' ', soup.get_text(' ', strip=True))

    # Build CRICOS-indexed course list from the page
    # The page has course links like: /courses/course/{code}?tab=international
    # With text: "BSB30120 - Certificate III in Business (CRICOS: 107218D)"
    courses_by_cricos = {}
    course_urls = []

    for a in soup.find_all('a', href=True):
        href = a['href']
        if '/courses/course/' in href:
            full_href = href if href.startswith('http') else urljoin(BASE, href)
            # Normalize: strip trailing slash, keep ?tab=international
            full_href = full_href.rstrip('/')
            if full_href not in course_urls:
                course_urls.append(full_href)

            a_text = a.get_text(' ', strip=True)
            # Extract CRICOS from text
            cricos_m = re.search(r'CRICOS[:\s]*(\d{6}[A-Za-z])', a_text)
            if cricos_m:
                cricos = cricos_m.group(1)
                # Clean title: remove trailing CRICOS part
                title = re.sub(r'\s*\(\s*CRICOS[^)]*\)\s*$', '', a_text).strip()
                title = re.sub(r'^[A-Z0-9]+\s*-\s*', '', title).strip()
                if cricos not in courses_by_cricos:
                    courses_by_cricos[cricos] = {
                        'url': full_href,
                        'title': title,
                    }

    print(f'    {len(courses_by_cricos)} CRICOS-mapped courses on international page')
    print(f'    {len(course_urls)} course URLs found')
    return courses_by_cricos, course_urls


# ---------- page scrape ----------
def scrape_course(url, expected_cricos=None):
    """Scrape a single course detail page (with ?tab=international for fee data)."""
    # Always use ?tab=international to show international fee
    page_url = url if 'tab=international' in url else url + '?tab=international'
    print(f'    {page_url.split("/")[-1]}...', end=' ')

    r = fetch(page_url)
    if not r:
        print('❌')
        # Try without ?tab=
        if 'tab=international' in page_url:
            r = fetch(url)
            if not r:
                return None
        else:
            return None
    soup = BeautifulSoup(r.text, 'html.parser')
    text = re.sub(r'\s+', ' ', soup.get_text(' ', strip=True))

    # Title from <title>
    title = ''
    title_tag = soup.find('title')
    if title_tag:
        t = title_tag.get_text(strip=True)
        title = t

    # CRICOS course code
    cricos = ''
    m = re.search(r'CRICOS[:\s]*(\d{6}[A-Za-z])', text)
    if m:
        cricos = m.group(1)

    # VET / course code (e.g., HLT54121)
    vet_code = ''
    m = re.search(r'([A-Z]{2,4}\d{4,6})', title.split('-')[0].strip())
    if m:
        vet_code = m.group(1)

    # Duration: look in structured content
    dur_weeks = None
    # Look for specific "Course Duration" label
    dur_m = re.search(r'Course\s*Duration[:\s]*(\d+)\s*[Ww]eeks?', text, re.I)
    if dur_m:
        dur_weeks = int(dur_m.group(1))
    if not dur_weeks:
        # Check for "Duration" next to a weeks value
        dur_m = re.search(r'(?:Duration|Course Duration)[:\s]*(\d+)\s*[Ww]eeks?', text, re.I)
        if dur_m:
            dur_weeks = int(dur_m.group(1))
    if not dur_weeks:
        # Look for range like "19 Oct 2026 - 7 Apr 2028" calculate weeks
        range_m = re.search(r'(\d{1,2}\s+[A-Z][a-z]+\s+\d{4})\s*-\s*(\d{1,2}\s+[A-Z][a-z]+\s+\d{4})', text)
        if range_m:
            try:
                from datetime import datetime
                d1 = datetime.strptime(range_m.group(1), '%d %B %Y')
                d2 = datetime.strptime(range_m.group(2), '%d %B %Y')
                days = (d2 - d1).days
                if days > 0:
                    dur_weeks = round(days / 7)
            except Exception:
                pass
        if not dur_weeks:
            # Look for year-based duration
            yr_m = re.search(r'(\d+\.?\d*)\s*year', text, re.I)
            if yr_m:
                yrs = float(yr_m.group(1))
                dur_weeks = int(yrs * 52)

    # Fee: look for international fee section
    fee = None
    # Target the specific "Tuition Fees International" section
    # which appears after the domestic fee section
    idx = text.find('Tuition Fees International')
    if idx >= 0:
        section = text[idx:idx+300]
        fee_m = re.search(r'\$([\d,]+)', section)
        if fee_m:
            fee = clean_numeric(fee_m.group(1))
    if not fee:
        # Also check just "International" near a dollar amount with tight context
        for m in re.finditer(r'International\s+\$?([\d,]+)', text, re.I):
            fee = clean_numeric(m.group(1))
            if fee and fee > 1000:
                break

    # Intake dates
    months = []
    # Look for "Intake Dates Ongoing February & July" or similar
    intake_text_m = re.search(r'Intake\s*Dates?\s*[^.]*(Ongoing.*|February|January|March|April|May|June|July|August|September|October|November|December)', text, re.I)
    if intake_text_m:
        intake_text = intake_text_m.group(0)
        for mon in MONTH_ORDER:
            if mon in intake_text or mon[:3] in intake_text:
                if mon not in months:
                    months.append(mon)
    if not months:
        # Check for month names near "intake" keyword
        for m_name in MONTH_ORDER:
            if re.search(r'(?:Intake|Start|Commence|Session)[^.]{0,80}' + m_name[:3], text, re.I):
                if m_name not in months:
                    months.append(m_name)

    # Course overview content
    desc = ''
    overview_div = soup.find('h3', string=re.compile(r'Course overview', re.I))
    if overview_div:
        parts = []
        for sib in overview_div.find_next_siblings():
            if sib.name and sib.name.startswith('h'):
                break
            parts.append(str(sib))
        if parts:
            desc = sanitise_html(''.join(parts))
            desc = clean_html(desc)
    if not desc:
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            desc = clean_html(meta_desc['content'])

    # Entry requirements (might not be explicitly on page)
    entry = ''
    for h in soup.find_all(['h3', 'h4', 'h5']):
        if re.search(r'(?:entry|requirement|admission|prerequisite)', h.get_text(strip=True), re.I):
            parts = []
            for sib in h.find_next_siblings():
                if sib.name and sib.name.startswith('h'):
                    break
                parts.append(str(sib))
            if parts:
                entry = sanitise_html(''.join(parts))
                entry = clean_html(entry)
            break

    intake_str = ', '.join(m for m in MONTH_ORDER if m in months)

    # Printable progress
    flags = []
    if cricos:
        flags.append(f'CRICOS {cricos}')
    else:
        flags.append('no CRICOS')
    if fee:
        flags.append(f'${fee}')
    if dur_weeks:
        flags.append(f'{dur_weeks}w')
    flags.append(f'{len(months)}m')
    print(f'✅ {" | ".join(flags)}')

    return {
        'title': title,
        'cricos': cricos,
        'vet_code': vet_code,
        'url': page_url,
        'course_duration_per_week': dur_weeks,
        'offshore_tuition_fee': fee,
        'months': months,
        'intake': intake_str,
        'course_description': desc,
        'entry_requirements': entry,
    }


# ---------- main ----------
def main():
    print(f'\n  {PROVIDER_NAME} Scraper\n  {"="*40}\n  Provider: {PROVIDER_CODE}\n')

    register, register_by_vet = load_register()
    print(f'  📋 {len(register)} courses in CSV register')

    # Get course list from /international page (has CRICOS codes embedded)
    intl_courses, intl_urls = collect_international_courses()
    if not intl_urls:
        print('  ❌ No course URLs from international page')
        return

    # Scrape each course page
    scraped = []
    for i, url in enumerate(intl_urls):
        # Check if this URL has a pre-known CRICOS from the international page
        known_cricos = None
        slug = url.rstrip('/').split('/')[-1].split('?')[0]
        for cricos, info in intl_courses.items():
            if info['url'] == url or slug in info['url']:
                known_cricos = cricos
                break
        d = scrape_course(url, known_cricos)
        if d:
            # If page didn't find CRICOS but we know it from international page
            if not d['cricos'] and known_cricos:
                d['cricos'] = known_cricos
            scraped.append(d)
        time.sleep(0.5)

    # ----- Match to CSV -----
    all_months = set()
    results = []
    matched_cricos = set()

    for d in scraped:
        cricos = d.get('cricos', '') or ''

        if not cricos and d.get('vet_code'):
            # Try VET code matching
            vet_lower = d['vet_code'].lower()
            if vet_lower in register_by_vet:
                cricos = register_by_vet[vet_lower]
            else:
                # Try partial VET match
                for vcode, cc in register_by_vet.items():
                    if vcode.startswith(vet_lower[:5]) or vet_lower.startswith(vcode[:5]):
                        cricos = cc
                        break

        if not cricos:
            # Word-overlap title matching
            cricos = match_cricos(d['title'], register)

        if cricos:
            matched_cricos.add(cricos)

        months = d.get('months', [])
        all_months.update(months)

        fee = d.get('offshore_tuition_fee')
        if not fee and cricos and cricos in register:
            fee = register[cricos]['offshore_tuition_fee']

        dur = d.get('course_duration_per_week')
        if not dur and cricos and cricos in register:
            dur = register[cricos]['course_duration_per_week']

        results.append({
            'cricos': cricos,
            'title': d['title'],
            'url': d['url'],
            'course_duration_per_week': dur,
            'offshore_tuition_fee': fee,
            'onshore_tuition_fee': None,
            'enrolment_fee': 0,
            'materials_fee': None,
            'intake': d.get('intake', ''),
            'course_description': d.get('course_description', ''),
            'entry_requirements': d.get('entry_requirements', ''),
            'source': 'page-scrape' if cricos else 'no-cricos',
        })

    # ----- Register-only backfill -----
    backfill_count = 0
    for code, row in register.items():
        if code not in matched_cricos:
            results.append({
                'cricos': code,
                'title': row['title'],
                'url': '',
                'course_duration_per_week': row['course_duration_per_week'],
                'offshore_tuition_fee': row['offshore_tuition_fee'],
                'onshore_tuition_fee': None,
                'enrolment_fee': 0,
                'materials_fee': None,
                'intake': '',
                'course_description': '',
                'entry_requirements': '',
                'source': 'register-only',
            })
            backfill_count += 1

    intake_date = ', '.join(m for m in MONTH_ORDER if m in all_months)
    if not intake_date:
        intake_date = 'February, July'

    # ----- SQL -----
    print(f'\n  💾 SQL -> {SQL_PATH.name}')
    with open(SQL_PATH, 'w', encoding='utf-8') as f:
        f.write('-- Update provider institution details\n'
                'UPDATE provider_institution SET\n'
                f"    intake_date = '{intake_date}',\n"
                '    updated_at = NOW()\n'
                f"WHERE cricos_provider_code = '{PROVIDER_CODE}';\n\n")

        emitted = set()
        sql_count = 0
        for d in results:
            if not d['cricos']:
                f.write(f"-- ⚠️ Skipped (no CRICOS matched): {d['title'][:60]} | {d.get('url', '')[:80]}\n\n")
                continue
            if d['cricos'] in emitted:
                continue
            emitted.add(d['cricos'])
            sql_count += 1

            desc = d.get('course_description', '') or ''
            if desc in ('nan', 'None', ''):
                desc = ''
            else:
                desc = desc.replace("'", "''")
                if desc and not desc.startswith('Course overview'):
                    desc = f'Course overview <p>{desc}</p>'

            entry = d.get('entry_requirements', '') or ''
            if entry in ('nan', 'None', ''):
                entry = ''
            else:
                entry = entry.replace("'", "''")

            fee = d.get('offshore_tuition_fee')
            fee_sql = str(fee) if fee else 'NULL'
            dur = d.get('course_duration_per_week')
            dur_sql = str(dur) if dur else 'NULL'

            url = d.get('url', '') or ''
            if url in ('nan', 'None'):
                url = ''
            else:
                url = url.replace("'", "''")

            if d['source'] == 'register-only':
                f.write(
                    f"-- Register-only: {d['title']}\n"
                    f"UPDATE courses SET\n"
                    f"    course_duration_per_week = {dur_sql},\n"
                    f"    offshore_tuition_fee = {fee_sql},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = 0,\n"
                    f"    materials_fee = NULL,\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{d['cricos']}';\n\n"
                )
            else:
                f.write(
                    f"UPDATE courses SET\n"
                    f"    course_description = '{desc}',\n"
                    f"    course_duration_per_week = {dur_sql},\n"
                    f"    offshore_tuition_fee = {fee_sql},\n"
                    f"    onshore_tuition_fee = NULL,\n"
                    f"    enrolment_fee = 0,\n"
                    f"    materials_fee = NULL,\n"
                    f"    entry_requirements = '{entry}',\n"
                    f"    apply_form = '{url}',\n"
                    f"    updated_at = NOW()\n"
                    f"WHERE cricos_course_code = '{d['cricos']}';\n\n"
                )

    # ----- XLSX -----
    print(f'  💾 XLSX -> {EXCEL_PATH.name}')
    out_rows = []
    for d in results:
        def cell(v):
            if v is None or str(v).strip().lower() in ('nan', 'none', ''):
                return ''
            return str(v)[:32000]
        fee = d.get('offshore_tuition_fee')
        dur = d.get('course_duration_per_week')
        out_rows.append({
            'cricos': d['cricos'],
            'title': d['title'],
            'url': d['url'],
            'course_duration_per_week': dur if dur else '',
            'offshore_tuition_fee': fee if fee else '',
            'onshore_tuition_fee': '',
            'enrolment_fee': '',
            'materials_fee': '',
            'intake': cell(d.get('intake', '')),
            'course_description': cell(d.get('course_description', '')),
            'entry_requirements': cell(d.get('entry_requirements', '')),
            'source': d['source'],
        })

    pd.DataFrame(out_rows).to_excel(EXCEL_PATH, index=False)

    page_match = sum(1 for d in results if d['source'] == 'page-scrape')
    print(f'\n  🏁 Done. {sql_count} SQL rows | {len(results)} total XLSX rows')
    print(f'     Page-matched: {page_match} | Register-only backfill: {backfill_count}')
    print(f'     Intake: {intake_date}\n')


if __name__ == '__main__':
    main()
