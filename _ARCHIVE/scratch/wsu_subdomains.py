"""WSU - find course system."""
import sys, re, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Check for coursefinder subdomain
for sub in ['coursefinder', 'courses', 'study', 'handbook', 'degrees']:
    try:
        r = curl.get(f'https://{sub}.westernsydney.edu.au', impersonate='chrome120', timeout=15)
        print(f'{sub}.westernsydney.edu.au: {r.status_code}, {len(r.text)}b')
        if r.status_code == 200 and len(r.text) > 500:
            s = BeautifulSoup(r.text, 'html.parser')
            h1 = s.find('h1')
            print(f'  H1: {h1.get_text(strip=True)[:60] if h1 else "?"}')
    except Exception as e:
        print(f'{sub}: ERROR {str(e)[:40]}')

# Check /future/ path
for path in ['/future', '/future/students', '/international',
             '/study', '/courses', '/course']:
    r2 = curl.get(f'{DOMAIN}{path}', impersonate='chrome120', timeout=15)
    print(f'{path}: {r2.status_code}')
    if r2.status_code == 200 and len(r2.text) > 5000:
        s2 = BeautifulSoup(r2.text, 'html.parser')
        h1 = s2.find('h1')
        print(f'  H1: {h1.get_text(strip=True)[:60] if h1 else "?"}')

# Also check /hie/ sub-categories for degree info
print('\n=== HIE section ===')
r3 = curl.get(f'{DOMAIN}/hie', impersonate='chrome120', timeout=15)
if r3.status_code == 200:
    s3 = BeautifulSoup(r3.text, 'html.parser')
    links = [a['href'] for a in s3.find_all('a', href=True)]
    degree_links = [l for l in links if any(k in l.lower() for k in ['degree','course','program','bachelor','master'])]
    print(f'  Degree links: {len(degree_links)}')
    for l in degree_links[:5]: print(f'    {l}')

# Find course-related from sitemap more carefully
print('\n=== Sitemap search for course patterns ===')
r4 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r4.text)

# Look for URLs that match degree structure
degree_urls = [u for u in urls if re.search(r'/degree|/course|/bachelor|/master|/graduate', u, re.I)]
print(f'Degree/course URLs: {len(degree_urls)}')
for u in sorted(degree_urls)[:10]:
    print(f'  {u}')

# Search for nursing in sitemap
nurs_urls = [u for u in urls if 'nurs' in u.lower()]
print(f'\nNursing URLs: {len(nurs_urls)}')
for u in sorted(nurs_urls)[:10]:
    print(f'  {u}')
