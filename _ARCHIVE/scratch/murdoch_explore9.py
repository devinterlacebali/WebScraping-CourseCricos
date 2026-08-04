"""Murdoch - extract ALL course codes from Funnelback search."""
import requests, re, json, sys, time
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

def get_search_page(query='', page=1):
    """Get Funnelback search results page."""
    params = {
        'tab': 'courses',
        'q': query,
        'page': page,
        'results_per_page': 20,
    }
    r = S.get('https://search.murdoch.edu.au/', params=params, timeout=30)
    return r.text

def parse_courses(html):
    """Extract course info from search results HTML."""
    courses = []
    # Find all list items with course data - look for the pattern
    # Each result has: level, type, title (link), description, code, etc.
    
    # Find course blocks
    blocks = re.findall(
        r'<li[^>]*class="[^"]*"[^>]*>.*?'
        r'(?:Undergraduate|Postgraduate|Honours|Research|Enabling)\s*.*?'
        r'(?:Course|Major)\s*.*?'
        r'<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>.*?'
        r'Code:\s*([A-Z0-9-]+)',
        html, re.DOTALL
    )
    
    for href, title, code in blocks:
        courses.append({
            'title': title.strip(),
            'code': code.strip(),
            'url': href if href.startswith('http') else f'https://www.murdoch.edu.au{href}',
        })
    
    return courses

# Check the main search results (no query)
print("=== Getting course list from search ===")
all_courses = []

# Try different approaches
# 1. Set sort to title and get page 1
r = S.get('https://search.murdoch.edu.au/?tab=courses&sort=title', timeout=30)
html = r.text

# Extract total count
total_match = re.search(r'out of\s+<strong>(\d+)</strong>\s+courses', html)
if total_match:
    print(f'Total courses: {total_match.group(1)}')

# Extract individual course items
# Each item has level, type, title link, code
items = re.findall(
    r'<a href="(https://[^"]*)"[^>]*>([^<]+)</a>.*?Code:\s*([A-Z0-9-]+)',
    html
)
print(f'Found {len(items)} course items on page 1')

for url, title, code in items[:10]:
    print(f'  {code}: {title[:50]} -> {url[:80]}')

# Get the Funnelback JSON data if available  
print('\n=== Try Funnelback JSON API ===')
for page_num in range(1, 4):  # Get first 3 pages
    r = S.get('https://search.murdoch.edu.au/s/search.json', params={
        'collection': 'murdoch~courses',
        'query': '',
        'sort': 'title',
        'page': page_num,
    }, timeout=30, headers={
        'Accept': 'application/json',
        **HEADERS
    })
    content_type = r.headers.get('Content-Type', '')
    print(f'Page {page_num}: {r.status_code}, Content-Type: {content_type}, {len(r.text)} bytes')
    if 'json' in content_type.lower() or r.text.strip().startswith('{') or r.text.strip().startswith('['):
        try:
            data = json.loads(r.text)
            print(json.dumps(data, indent=2)[:500])
        except:
            print(r.text[:500])
    else:
        print(r.text[:200])

print('\n=== Try with ?format=json ===')
r = S.get('https://search.murdoch.edu.au/s/search.html', params={
    'collection': 'murdoch~courses',
    'form': 'json',
    'sort': 'title',
}, timeout=30)
print(f'{r.status_code}, {len(r.text)} bytes')
print(r.text[:500])
