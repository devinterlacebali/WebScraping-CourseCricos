"""Murdoch - find actual degree pages with CRICOS codes."""
import requests, re, json, sys, gzip, io
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

# 1. Check if there are better degree/course pages
print('=== Check alternative URL patterns ===')
patterns = [
    '/study/courses/',
    '/future-students/courses/',
    '/courses/',
    '/study/',
]

for p in patterns:
    url = f'https://www.murdoch.edu.au{p}'
    r = S.get(url, timeout=30, allow_redirects=True)
    print(f'{p}: {r.status_code} -> {r.url} ({len(r.text)} bytes)')

# 2. Check /study/courses page for links
print('\n=== Course links on /study/courses ===')
r = S.get('https://www.murdoch.edu.au/study/courses', timeout=30)
# Find all <a> with href containing "course"
for m in re.finditer(r'<a[^>]*href=[\"\']([^\"\']*course[^\"\']*)[\"\'][^>]*>(.*?)</a>', r.text, re.DOTALL | re.I):
    href = m.group(1)
    text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    if text and len(text) > 3:
        full_url = href if href.startswith('http') else f'https://www.murdoch.edu.au{href}'
        print(f'  {text[:60]:50s} -> {full_url[:80]}')

# 3. Check for a dedicated nursing course page
print('\n=== Looking for nursing/health courses ===')
for kw in ['nursing', 'health', 'bachelor', 'degree']:
    r = S.get(f'https://www.murdoch.edu.au/search?q={kw}', timeout=30, allow_redirects=True)
    print(f'Search "{kw}": {r.status_code} ({len(r.text)} bytes) -> {r.url}')

# 4. Check the search API
print('\n=== Search API ===')
for api in [
    'https://www.murdoch.edu.au/api/search?q=nursing',
    'https://www.murdoch.edu.au/sitefinity/public/services/search/search.svc/search?q=nursing',
]:
    try:
        r = S.get(api, timeout=15)
        print(f'{api}: {r.status_code} {r.text[:200]}')
    except Exception as e:
        print(f'{api}: ERROR {e}')

# 5. Look at a few pages more carefully for "International" fee info
print('\n=== Check international student fee pages ===')
for level in ['Undergraduate', 'Postgraduate']:
    u = f'https://www.murdoch.edu.au/course/{level}/mj-cams'
    r = S.get(u, timeout=30)
    # Look for data-student-type-toggle
    has_intl_section = 'is-international' in r.text
    has_domestic_section = 'is-domestic' in r.text
    print(f'{level}: has international section: {has_intl_section}, domestic: {has_domestic_section}')
    # Check for fee in the international tab
    if has_intl_section:
        intl_section = re.search(r'is-international.*?</table>', r.text, re.DOTALL)
        if intl_section:
            print(f'  International section found ({len(intl_section.group(0))} chars)')
            # Check for dollar amounts
            fees = re.findall(r'\$[0-9,]+', intl_section.group(0))
            print(f'  Fees found: {fees}')
