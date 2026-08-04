"""UTas - check handbook and API."""
import sys, re, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

# Check known subdomains
domains = ['handbook.utas.edu.au', 'courses.utas.edu.au', 'study.utas.edu.au', 'course.utas.edu.au']
for d in domains:
    try:
        r = curl.get(f'https://{d}', impersonate='chrome120', timeout=15)
        print(f'{d}: {r.status_code}, {len(r.text)}b')
        s = BeautifulSoup(r.text, 'html.parser')
        h1 = s.find('h1')
        print(f'  H1: {h1.get_text(strip=True)[:50] if h1 else "none"}')
        # Check sitemap
        r2 = curl.get(f'https://{d}/sitemap.xml', impersonate='chrome120', timeout=15)
        if r2.status_code == 200 and len(r2.text) > 100:
            urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
            print(f'  Sitemap: {len(urls)} URLs')
            if urls: print(f'  Sample: {urls[0][:100]}')
    except Exception as e:
        print(f'{d}: ERROR {str(e)[:40]}')

# Also check if there's a course search API in Squiz Matrix
print('\n--- Squiz matrix AJAX API ---')
r3 = curl.get('https://www.utas.edu.au/courses', impersonate='chrome120', timeout=30)
# Look for graphql or API endpoints
for m in re.finditer(r'https?://[^"\'<>]*(?:api|graphql|ajax|rest|course|degree|search)[^"\'<>]*', r3.text):
    url = m.group()[:120]
    if 'api' in url or 'graphql' in url:
        print(f'  {url}')

# Check CSV counts  
print('\n--- CSV coverage ---')
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    utas = [r for r in reader if r and r[0].strip() == '00586B']
print(f'UTas (00586B): {len(utas)} courses')
# Show nursing
nursing = [r for r in utas if 'nurs' in r[3].lower()]
print(f'Nursing: {len(nursing)}')
for r in nursing[:5]:
    print(f'  {r[2]} | {r[3][:60]} | fee={r[20][:15]} | dur={r[19]}wk')
