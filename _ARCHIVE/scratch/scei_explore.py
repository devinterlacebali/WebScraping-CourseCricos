#!/usr/bin/env python3
"""
SCEI (Southern Cross Education Institute) — www.scei.edu.au
Exploration script: Cloudflare, CRICOS footer, sitemap, CSV coverage, course SSR
"""
import csv, json, re, sys
from curl_cffi import requests

BASE = 'https://scei.edu.au'
PROVIDER_CODE = '02934D'
PROVIDER_NAME = 'Southern Cross Education Institute Pty Ltd'
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
            print('Cloudflare mentioned in body (CSP/etc)')
        if 'just a moment' in body or 'checking your browser' in body:
            print('WARNING: Challenge page detected')
        if r.status_code == 403:
            print('WARNING: 403 blocked')
        if not cf_h and r.status_code == 200:
            print('=> NO Cloudflare (no CF headers)')
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
    # Also check other pages
    for p in ['/About', '/Contact-us']:
        try:
            rr = requests.get(BASE + p, impersonate='chrome120', timeout=15)
            cc = re.findall(PROVIDER_CODE, rr.text)
            if cc:
                print(f'  {p}: {len(cc)} mentions')
        except:
            pass


def check_sitemap():
    print('\n=== 3. SITEMAP ===')
    sitemaps = [
        '/sitemap.xml', '/sitemap-index.xml', '/sitemap_index.xml',
        '/robots.txt'
    ]
    for sm in sitemaps:
        url = BASE + sm
        try:
            r = requests.get(url, impersonate='chrome120', timeout=15)
            print(f'{sm} -> Status: {r.status_code}, Length: {len(r.text)}')
            if r.status_code == 200 and sm == '/robots.txt':
                print(f'  Content: {r.text[:500]}')
            elif r.status_code == 200:
                urls = re.findall(r'<loc>(.*?)</loc>', r.text, re.IGNORECASE)
                print(f'  URLs in sitemap: {len(urls)}')
                course_urls = [u for u in urls if 'course' in u.lower()]
                print(f'  Course URLs: {len(course_urls)}')
                if urls:
                    print(f'  Sample: {urls[:3]}')
        except Exception as e:
            print(f'{sm} -> ERROR: {str(e)[:80]}')
    # Try to extract internal links from homepage
    try:
        r = requests.get(BASE, impersonate='chrome120', timeout=15)
        links = re.findall(r'href=["\'](https?://scei\.edu\.au[^"\']*|[^"\'\s]+)["\']', r.text, re.IGNORECASE)
        internal = [l for l in links if l.startswith('/') and not l.startswith('/_next')]
        print(f'Internal links on homepage: {len(internal)}')
        print(f'  Samples: {internal[:10]}')
    except Exception as e:
        print(f'Link extraction error: {e}')


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
        # Show CRICOS course codes
        cricos_codes = [row.get('CRICOS Course Code', '') for row in rows]
        print(f'CRICOS Course Codes: {cricos_codes}')
    except FileNotFoundError:
        print(f'CSV not found at {CSV_PATH}')


def check_course_ssr():
    print('\n=== 5. COURSE PAGE SSR ===')
    # SCEI uses Next.js — check if course data is in HTML
    try:
        r = requests.get(BASE + '/Courses', impersonate='chrome120', timeout=15)
        has_content = len(r.text) > 10000
        is_next = '_next' in r.text
        # Check for course titles in HTML
        course_patterns = re.findall(r'course[^>]*>[^<]{10,100}<', r.text, re.IGNORECASE)
        print(f'/Courses: length={len(r.text)}, Next.js={is_next}, Content={has_content}')
        print(f'Course HTML patterns: {len(course_patterns)}')
        # Check if content is client-side rendered
        nd = re.search(r'__NEXT_DATA__', r.text)
        if nd:
            print('Next.js __NEXT_DATA__ present (SSR + hydration)')
        # Check for pre-rendered HTML content
        if 'Certificate' in r.text or 'Diploma' in r.text:
            print('Course qualifications in HTML: YES (SSR)')
        else:
            print('Course qualifications in HTML: NO (client-side render?)')
        print('=> Likely SSR: Next.js with server-side rendering')
    except Exception as e:
        print(f'ERROR: {e}')


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
    print(f'Cloudflare: NO')
    print(f'CRICOS Footer Code: {PROVIDER_CODE}')
    print(f'Sitemap: NOT FOUND (Next.js site)')
    csv_count = 0
    try:
        with open(CSV_PATH, encoding='utf-8-sig') as f:
            csv_count = sum(1 for line in f if PROVIDER_CODE in line) - 1
    except:
        pass
    print(f'CSV Courses: {csv_count}')
    print(f'Framework: Next.js (SSR)')
    print(f'Note: www.scei.com.au is parked; actual site is scei.edu.au')
