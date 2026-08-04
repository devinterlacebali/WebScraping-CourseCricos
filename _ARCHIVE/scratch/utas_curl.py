"""UTas with curl_cffi."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.utas.edu.au'

r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
print(f'Main: {r.status_code}, {len(r.text)}b')
soup = BeautifulSoup(r.text, 'html.parser')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')
has_cf = 'cloudflare' in r.text.lower() or 'cf-browser' in r.text
print(f'Cloudflare: {has_cf}')
has_next = '__NEXT_DATA__' in r.text
has_nuxt = '__NUXT__' in r.text
print(f'Next.js: {has_next}, Nuxt: {has_nuxt}')

# Sitemap
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
if r2.status_code == 200 and len(r2.text) > 100:
    urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
    print(f'\nSitemap: {len(urls)} URLs')
    subs = re.findall(r'<sitemap>', r2.text)
    print(f'Index format: {len(subs)} sub-sitemaps')
    if subs:
        sub_urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
        for su in sub_urls[:8]:
            print(f'  Sub: {su}')
            r3 = curl.get(su, impersonate='chrome120', timeout=30)
            sub_urls2 = re.findall(r'<loc>(.*?)</loc>', r3.text)
            course_like = [u for u in sub_urls2 if any(k in u.lower() for k in ['course','degree','program','bachelor','master'])]
            print(f'     {len(sub_urls2)} URLs, {len(course_like)} course-like')
            if course_like:
                for u in course_like[:3]: print(f'       {u}')
    else:
        course_urls = [u for u in urls if any(k in u.lower() for k in ['/course/', '/degree/', '/program/'])]
        print(f'Course-like: {len(course_urls)}')
        for u in course_urls[:5]: print(f'  {u}')

# Check a course page
print('\n--- Sample course ---')
for slug in ['bachelor-of-nursing', 'bachelor-of-science-nursing']:
    r5 = curl.get(f'{DOMAIN}/courses/{slug}', impersonate='chrome120', timeout=30)
    print(f'/courses/{slug}: {r5.status_code}, {len(r5.text)}b')
    if r5.status_code == 200 and len(r5.text) > 1000:
        s5 = BeautifulSoup(r5.text, 'html.parser')
        h1_5 = s5.find('h1')
        body = re.sub(r'\s+', ' ', s5.get_text())
        cricos = bool(re.search(r'CRICOS', body))
        fee = bool(re.search(r'AUD', body))
        print(f'  H1: {h1_5.get_text(strip=True)[:80] if h1_5 else "none"}')
        print(f'  CRICOS={cricos}, Fee={fee}')
        if cricos:
            for m in re.finditer(r'CRICOS.{0,80}', body):
                print(f'  {m.group()[:100]}')
        if fee:
            for m in re.finditer(r'AUD\s*\$?\s*[0-9,]{4,}', body):
                ctx = body[max(0,m.start()-40):m.end()+40]
                print(f'  {ctx.strip()[:120]}')
        break

# Also check study.utas.edu.au
print('\n--- study.utas.edu.au ---')
r6 = curl.get('https://study.utas.edu.au/', impersonate='chrome120', timeout=30)
print(f'Status: {r6.status_code}, {len(r6.text)}b')
