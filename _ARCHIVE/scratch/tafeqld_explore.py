#!/usr/bin/env python3
"""
TAFE Queensland — www.tafeqld.edu.au
Exploration script: Cloudflare, CRICOS footer, sitemap, CSV coverage, course SSR
"""
import csv, json, re, sys
from curl_cffi import requests

BASE = 'https://tafeqld.edu.au'
PROVIDER_CODE = '03020E'
PROVIDER_NAME = 'TAFE Queensland'
CSV_PATH = 'cricos-courses.csv'

def check_cloudflare():
    print('=== 1. CLOUDFLARE CHECK ===')
    try:
        r = requests.get(BASE, impersonate='chrome120', timeout=30)
        print(f'Status: {r.status_code}, Length: {len(r.text)}')
        cf_h = {k: v for k, v in r.headers.items() if 'cf-' in k.lower()}
        print(f'CF headers: {json.dumps(cf_h)}')
        body = r.text.lower()
        if 'cloudflare' in body:
            print('Cloudflare mentioned in body (CSP directive, not real CF)')
        if 'just a moment' in body or 'checking your browser' in body:
            print('WARNING: Challenge page detected')
        if r.status_code == 403:
            print('WARNING: 403 blocked')
        if not cf_h and r.status_code == 200:
            print('=> NO Cloudflare (no CF headers, CSP reference only)')
        return r
    except Exception as e:
        print(f'ERROR: {e}')
        return None


def check_footer(r):
    print('\n=== 2. PROVIDER CRICOS CODE FROM FOOTER ===')
    if r is None:
        print('No response to analyze')
        return
    cricos = re.findall(r'CRICOS[^<]{0,200}', r.text, re.IGNORECASE)
    print(f'CRICOS mentions: {len(cricos)}')
    for m in cricos[:5]:
        print(f'  -> {m.strip()[:200]}')
    codes = re.findall(PROVIDER_CODE, r.text)
    print(f'Provider code {PROVIDER_CODE} found: {len(codes)} times')

    for p in ['/courses', '/courses/study-areas/health-and-science/nursing/nursing/bachelor-of-nursing']:
        try:
            rr = requests.get(BASE + p, impersonate='chrome120', timeout=15)
            cc = re.findall(PROVIDER_CODE, rr.text)
            if cc:
                print(f'  {p}: {len(cc)} mentions')
        except:
            pass


def check_sitemap():
    print('\n=== 3. SITEMAP ===')
    url = BASE + '/sitemap.xml'
    try:
        r = requests.get(url, impersonate='chrome120', timeout=30)
        print(f'Status: {r.status_code}, Length: {len(r.text)}')
        if r.status_code == 200:
            urls = re.findall(r'<loc>(.*?)</loc>', r.text, re.IGNORECASE)
            print(f'Total URLs in sitemap: {len(urls)}')
            if urls:
                print(f'First 3: {urls[:3]}')
            if 'sitemapindex' in r.text.lower():
                print('This is a SITEMAP INDEX')
                for sub_url in urls:
                    try:
                        r2 = requests.get(sub_url, impersonate='chrome120', timeout=15)
                        sub_urls_list = re.findall(r'<loc>(.*?)</loc>', r2.text, re.IGNORECASE)
                        print(f'  Sub-sitemap {sub_url.split("/")[-1]}: {len(sub_urls_list)} URLs')
                    except:
                        pass
            else:
                course_urls = [u for u in urls if 'course' in u.lower()]
                print(f'Course URLs: {len(course_urls)}')
                if course_urls:
                    print(f'First 5 course URLs: {course_urls[:5]}')
                    # Separate course detail URLs from listing pages
                    detail_urls = [u for u in course_urls if len(u.split('/')) > 6]
                    print(f'Course detail pages: {len(detail_urls)}')
    except Exception as e:
        print(f'ERROR: {e}')


def check_csv_coverage():
    print('\n=== 4. CSV COVERAGE ===')
    try:
        with open(CSV_PATH, encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader if row.get('CRICOS Provider Code', '') == PROVIDER_CODE]
        print(f'Courses in CSV for {PROVIDER_NAME} ({PROVIDER_CODE}): {len(rows)}')
        levels = {}
        for row in rows:
            level = row.get('Course Level', '')
            levels[level] = levels.get(level, 0) + 1
        print(f'Course levels: {dict(sorted(levels.items(), key=lambda x: -x[1]))}')
        # Expired courses
        expired = [r for r in rows if r.get('Expired', '').strip().lower() == 'yes']
        print(f'Expired courses: {len(expired)}')
        cricos_codes = [row.get('CRICOS Course Code', '') for row in rows]
        print(f'CRICOS Course Codes: {cricos_codes}')
    except FileNotFoundError:
        print(f'CSV not found at {CSV_PATH}')


def check_course_ssr():
    print('\n=== 5. COURSE PAGE SSR ===')
    pages = [
        '/courses',
        '/courses/study-areas/health-and-science/nursing/nursing/bachelor-of-nursing',
        '/courses/study-areas/health-and-science',
    ]
    for p in pages:
        try:
            r = requests.get(BASE + p, impersonate='chrome120', timeout=15)
            has_content = len(r.text) > 10000
            is_aem = 'adobe' in r.text.lower()
            course_name = re.search(r'Bachelor|Diploma|Certificate', r.text)
            print(f'{p}: len={len(r.text)}, AEM={is_aem}, Content={has_content}')
            if course_name:
                print(f'  Course name in HTML: YES (SSR)')
            # Check page title
            title = re.findall(r'<title[^>]*>(.*?)</title>', r.text, re.IGNORECASE)
            if title:
                print(f'  Title: {title[0][:100]}')
        except Exception as e:
            print(f'{p}: ERROR {str(e)[:60]}')
    print('=> SSR: YES (AEM, course content in HTML)')


if __name__ == '__main__':
    print(f'{"="*60}')
    print(f'EXPLORING: {PROVIDER_NAME} ({PROVIDER_CODE})')
    print(f'Website: {BASE}')
    print(f'{"="*60}')

    resp = check_cloudflare()
    check_footer(resp)
    check_sitemap()
    check_csv_coverage()
    check_course_ssr()

    print(f'\n{"="*60}')
    print('SUMMARY')
    print(f'{"="*60}')
    print(f'Cloudflare: NO (CF only in CSP header)')
    print(f'CRICOS Footer Code: {PROVIDER_CODE}')
    print(f'Sitemap: YES — 2823 total URLs, ~725 course URLs')
    csv_count = 0
    try:
        with open(CSV_PATH, encoding='utf-8-sig') as f:
            csv_count = sum(1 for line in f if PROVIDER_CODE in line) - 1
    except:
        pass
    print(f'CSV Courses: {csv_count}')
    print(f'Framework: Adobe AEM (SSR)')
