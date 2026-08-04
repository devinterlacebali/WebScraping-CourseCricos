"""Murdoch - find search API endpoint and extract all courses."""
import requests, re, json, sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

# Get the search page HTML
r = S.get('https://search.murdoch.edu.au/?tab=courses&q=', timeout=30)
text = r.text

# Look for the API endpoint in the HTML
# Check for data-* attributes with API info
for m in re.finditer(r'(?:fetch|ajax|url|endpoint|api)[^=]*=[\"\']([^\"\']+)[\"\']', text, re.I):
    url = m.group(1)
    if 'api' in url.lower() or 'search' in url.lower():
        print(f'Found: {url}')

# Look for the JS bundle that contains the search logic
for m in re.finditer(r'<script[^>]+src=[\"\']([^\"\']+)[\"\']', text):
    src = m.group(1)
    if 'search' in src.lower() or 'bundle' in src.lower() or 'app' in src.lower():
        print(f'Script: {src}')

# Try the Funnelback search API
print('\n=== Try Funnelback API ===')
funnelback_urls = [
    'https://search.murdoch.edu.au/s/search.html?collection=murdoch~courses&form=json',
    'https://search.murdoch.edu.au/s/search.json?collection=murdoch~courses&query=',
    'https://search.murdoch.edu.au/s/search.html?collection=murdoch~courses',
]

for fb_url in funnelback_urls:
    try:
        r2 = S.get(fb_url, timeout=15)
        print(f'{fb_url}: {r2.status_code} ({len(r2.text)} bytes)')
        if r2.status_code == 200 and len(r2.text) > 100:
            print(f'  First 500: {r2.text[:500]}')
    except Exception as e:
        print(f'{fb_url}: ERROR {e}')

# Try the /s/ endpoint (Funnelback)
print('\n=== Funnelback /s/ endpoint ===')
r3 = S.get('https://search.murdoch.edu.au/s/', timeout=15, params={
    'collection': 'murdoch~courses',
    'form': 'json',
    'query': 'nursing',
})
print(f'/s/: {r3.status_code} ({len(r3.text)} bytes)')
if len(r3.text) < 2000:
    print(r3.text[:1000])

# Check /s/search.json
r4 = S.get('https://search.murdoch.edu.au/s/search.json', timeout=15, params={
    'collection': 'murdoch~courses',
    'query': 'nursing',
})
print(f'\n/s/search.json: {r4.status_code} ({len(r4.text)} bytes)')
if '</' not in r4.text[:100]:
    print(r4.text[:2000])
