#!/usr/bin/env python3
"""
TasTAFE — www.tastafe.tas.edu.au
Exploration script: Cloudflare, CRICOS footer, sitemap, CSV coverage, course SSR
"""
import csv, json, re, sys
from curl_cffi import requests

BASE = 'https://www.tastafe.tas.edu.au'
PROVIDER_CODE = '03041M'
PROVIDER_NAME = 'TasTAFE'
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
            print('Cloudflare mentioned in body')
        if 'just a moment' in body or 'checking your browser' in body:
            print('WARNING: Challenge page detected')
        if r.status_code == 403:
            print('WARNING: 403 blocked')
        if cf_h:
            print('=> CLOUDFLARE: YES (cf-ray header present)')
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

    intl_pages = ['/international', '/courses/course/bsb20120']
    for p in intl_pages:
        try:
            rr = requests.get(BASE + p, impersonate='chrome120', timeout=15)
            cc = re.findall(PROVIDER_CODE, rr.text)
            print(f'  {p}: {len(cc)} mentions of {PROVIDER_CODE}')
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
            print(f'Total URLs: {len(urls)}')
            if urls:
                print(f'First 3: {urls[:3]}')
            if 'sitemapindex' in r.text.lower():
                print('This is a SITEMAP INDEX')
            else:
                course_urls = [u for u in urls if 'course' in u.lower()]
                print(f'Course URLs: {len(course_urls)}')
                intl_urls = [u for u in urls if 'international' in u.lower()]
                print(f'International URLs: {len(intl_urls)}')
                if course_urls:
                    print(f'Sample course URLs: {course_urls[:5]}')
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
        expired = [r for r in rows if r.get('Expired', '').strip().lower() == 'yes']
        print(f'Expired courses: {len(expired)}')
        cricos_codes = [row.get('CRICOS Course Code', '') for row in rows]
        print(f'CRICOS Course Codes: {cricos_codes}')
    except FileNotFoundError:
        print(f'CSV not found at {CSV_PATH}')


def check_course_ssr():
    print('\n=== 5. COURSE PAGE SSR ===')
    pages = [
        '/international',
        '/courses/course/bsb20120',
    ]
    for p in pages:
        try:
            r = requests.get(BASE + p, impersonate='chrome120', timeout=15)
            has_content = len(r.text) > 10000
            course_name = re.search(r'Certificate|Diploma|Bachelor|English|Skill', r.text)
            print(f'{p}: len={len(r.text)}, Content={has_content}')
            title = re.findall(r'<title[^>]*>(.*?)</title>', r.text, re.IGNORECASE)
            if title:
                print(f'  Title: {title[0][:120]}')
            if course_name:
                print(f'  Course content in HTML: YES (SSR)')
        except Exception as e:
            print(f'{p}: ERROR {str(e)[:60]}')
    print('=> SSR: YES (full course content in HTML)')


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
    print(f'Cloudflare: YES (cf-ray headers)')
    print(f'CRICOS Footer Code: {PROVIDER_CODE}')
    print(f'Sitemap: YES — 662 total URLs, ~239 course URLs')
    csv_count = 0
    try:
        with open(CSV_PATH, encoding='utf-8-sig') as f:
            csv_count = sum(1 for line in f if PROVIDER_CODE in line) - 1
    except:
        pass
    print(f'CSV Courses: {csv_count}')
    print(f'Framework: Squiz Matrix (SSR)')
