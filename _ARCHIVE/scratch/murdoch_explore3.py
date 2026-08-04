"""Murdoch - extract the JSON metadata and full course data."""
import requests, re, json, sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

url = 'https://www.murdoch.edu.au/course/Undergraduate/mj-cams'
r = S.get(url, timeout=30)
text = r.text

# Get the content metadata JSON
for m in re.finditer(r'<script[^>]+type="application/json"[^>]*>(.*?)</script>', text, re.DOTALL):
    content = m.group(1).strip()
    if 'ContentType' in content:
        try:
            data = json.loads(content)
            print('=== Content Metadata ===')
            if isinstance(data, dict):
                cm = data.get('contentMetadata', '{}')
                if isinstance(cm, str):
                    cm = json.loads(cm)
                print(json.dumps(cm, indent=2)[:2000])
        except:
            print('Raw:', content[:500])
    elif 'PageId' in content:
        print('\n=== Page Info ===')
        print(content[:500])

# Intake table
print('\n=== Available Intakes ===')
for m in re.finditer(r'<td[^>]*>\s*(Semester \d, \d{4})\s*</td>\s*<td[^>]*>\s*([^<]+)\s*</td>', text, re.DOTALL):
    print(f'  {m.group(1).strip()} | {m.group(2).strip()}')

# H1
h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
if h1_match:
    clean = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
    print(f'\nH1: {clean}')

# CRICOS from JS
func_match = re.search(r"function getCricos\(\)\s*\{\s*return '([^']*)'", text)
print(f'\ngetCricos(): {func_match.group(1) if func_match else "NOT FOUND"}')

# Duration
print('\n=== Duration ===')
for m in re.finditer(r'(\d+)\s*(year|month|week)[s]?\s*\(?[fF]ull.?[tT]ime\)?', text):
    ctx = text[max(0,m.start()-40):m.end()+40]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f'  {m.group(0)} -> {clean}')

# Fee section
print('\n=== Fee $ amounts ===')
for m in re.finditer(r'\$[0-9,]+', text):
    start = max(0, m.start()-60)
    ctx = text[start:m.end()+100]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f'  {m.group(0)} -> ...{clean[:250]}')

# Body text 
print('\n=== Body text (first 3000 chars) ===')
body = re.search(r'<body[^>]*>(.*)</body>', text, re.DOTALL)
if body:
    clean = re.sub(r'<script[^>]*>.*?</script>', '', body.group(1), flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'\s+', ' ', clean)
    print(clean[:3000])
