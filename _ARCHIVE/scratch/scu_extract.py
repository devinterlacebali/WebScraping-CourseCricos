from curl_cffi import requests
import json, re

# Try to get more detailed metadata from funnelback - try with different params
# and also try the padre gateway directly

# 1. First try search.json with explicit metadata fields
url = 'https://course-search.scu.edu.au/s/search.json'
params = {
    'collection': 'scu~sp-search',
    'profile': '_default',
    'f.Tabs|scu~ds-courses': 'Courses',
    'sort': 'title',
    'num_ranks': 200,
}
r = requests.get(url, params=params, impersonate='chrome124', timeout=30)
data = r.json()
results = data.get('response', {}).get('resultPacket', {}).get('results', [])
print(f'Results: {len(results)}')

# Show full structure of one result
if results:
    print('\n=== Full result structure (first) ===')
    res = results[0]
    for k, v in res.items():
        if isinstance(v, dict):
            print(f'  {k}:')
            for k2, v2 in v.items():
                if isinstance(v2, (list, dict)):
                    print(f'    {k2}: {json.dumps(v2, indent=2)[:200]}')
                else:
                    print(f'    {k2}: {v2}')
        elif isinstance(v, list):
            print(f'  {k}: list[{len(v)}]')
            if v:
                print(f'    first={v[0]}')
        else:
            print(f'  {k}: {v}')

# 2. Try with 'meta' flag
print('\n=== Try detail API ===')
params2 = {
    'collection': 'scu~sp-search',
    'profile': '_default',
    'query': '!padrenull',
    'sort': 'title',
    'num_ranks': 10,
    'meta': 'true',
    'meta_all': 'true',
}
r2 = requests.get(url, params=params2, impersonate='chrome124', timeout=30)
data2 = r2.json()
results2 = data2.get('response', {}).get('resultPacket', {}).get('results', [])
if results2:
    print(f'Results with meta: {len(results2)}')
    for k, v in results2[0].items():
        if k == 'metaData' and isinstance(v, dict):
            print(f'\n  metaData keys: {list(v.keys())}')

# 3. Check the same course page we already fetched - extract CRICOS from the HTML
from bs4 import BeautifulSoup

r3 = requests.get('https://www.scu.edu.au/study/courses/diploma-of-business-2127279/', impersonate='chrome124')
soup = BeautifulSoup(r3.text, 'html.parser')

# Find the course snapshot section
print('\n=== Course Snapshot Parsing ===')

# Find CRICOS
cricos_elem = soup.find(string=re.compile(r'CRICOS'))
if cricos_elem:
    parent = cricos_elem.find_parent(['div', 'p', 'span', 'li'])
    print(f'CRICOS parent: {parent.get_text(strip=True)[:200] if parent else cricos_elem[:100]}')

# Find all elements with CRICOS in it
for tag in soup.find_all(['p', 'span', 'div', 'li'], string=re.compile(r'CRICOS')):
    print(f'CRICOS element: {tag.get_text(strip=True)[:200]}')

# Find the specific CRICOS value
cricos_pattern = re.compile(r'\b0\d{4}[A-Z0-9]\b')
cricos_values = set()
for tag in soup.find_all(string=cricos_pattern):
    cricos_values.update(cricos_pattern.findall(tag))
print(f'\nAll CRICOS-like codes found: {cricos_values}')

# Find the "Availability and fees" table
print('\n=== Availability and Fees Section ===')
for heading in soup.find_all(['h2', 'h3'], string=re.compile(r'(?i)availability.*fee')):
    print(f'Found heading: {heading.get_text(strip=True)}')
    # Next sibling content
    parent_section = heading.find_parent(['div', 'section'])
    if parent_section:
        print(f'  Section content (first 300): {parent_section.get_text(strip=True)[:300]}')

# Check for JSON data in the page
print('\n=== Script data in page ===')
for s in soup.find_all('script'):
    if s.string and 'course' in s.string.lower() and len(s.string) > 100:
        # Check if it's JSON
        try:
            j = json.loads(s.string)
            print(f'JSON found! Keys: {list(j.keys())[:10]}')
        except:
            pass

# The international fees page
print('\n=== International Courses and Fees page ===')
r4 = requests.get('https://www.scu.edu.au/study/international-courses-and-fees/', impersonate='chrome124')
soup4 = BeautifulSoup(r4.text, 'html.parser')

# Find if there's a course grid/listing
course_grid = soup4.find_all('div', class_=lambda c: c and 'grid' in c.lower())
print(f'Grid elements: {len(course_grid)}')

# Look for links with course codes in them
for a in soup4.find_all('a', href=True):
    if 'cricos' in a.get('href', '').lower() or ('study/courses' in a.get('href', '') and '2026' in a['href']):
        print(f'  {a["href"]} - {a.get_text(strip=True)[:80]}')
