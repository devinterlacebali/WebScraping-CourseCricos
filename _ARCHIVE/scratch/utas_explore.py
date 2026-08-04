"""UTas exploration with Scrapling."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from scrapling import Fetcher
from bs4 import BeautifulSoup
import re

DOMAIN = 'https://www.utas.edu.au'
f = Fetcher()

r = f.get(DOMAIN)
print(f'Main: {r.status}, {len(r.text)}b')
body = r.text
print(f'Cloudflare: {"cloudflare" in body.lower() or "cf-browser" in body}')
print(f'Body has content: {len(body) > 1000}')
soup = BeautifulSoup(body, 'html.parser')
h1 = soup.find('h1')
print(f'H1: {h1.get_text(strip=True)[:60] if h1 else "none"}')

# Check for Next.js / Nuxt
has_next = '__NEXT_DATA__' in body
has_nuxt = '__NUXT__' in body
print(f'Next.js: {has_next}, Nuxt: {has_nuxt}')

# Check sitemaps
print('\n=== Sitemaps ===')
for sp in ['/sitemap.xml', '/sitemap_index.xml', '/sitemap-index.xml']:
    try:
        r2 = f.get(f'{DOMAIN}{sp}')
        if r2.status == 200 and len(r2.text) > 50:
            urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
            print(f'{sp}: {r2.status}, {len(urls)} URLs')
            if urls: print(f'  First: {urls[0][:100]}')
            if not urls and len(r2.text) > 100:
                # Check if it's an index
                subs = re.findall(r'<sitemap>(.*?)</sitemap>', r2.text)
                print(f'  Sub-sitemaps in text: {len(subs)}')
        else:
            print(f'{sp}: {r2.status}')
    except Exception as e:
        print(f'{sp}: {str(e)[:50]}')

# Try international page
print('\n=== International page ===')
r3 = f.get(f'{DOMAIN}/international')
print(f'Status: {r3.status}, {len(r3.text)}b')
s3 = BeautifulSoup(r3.text, 'html.parser')
h1_3 = s3.find('h1')
print(f'H1: {h1_3.get_text(strip=True)[:80] if h1_3 else "none"}')
links = [a['href'] for a in s3.find_all('a', href=True) if 'course' in a.get('href','').lower()]
print(f'Course links: {len(links)}')
for l in links[:5]: print(f'  {l}')
