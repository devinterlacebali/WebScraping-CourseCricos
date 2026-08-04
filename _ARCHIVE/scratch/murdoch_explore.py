"""Murdoch University exploratory analysis."""
import requests, re, json, sys

# Strip hermes venv path conflict
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

url = 'https://www.murdoch.edu.au/course/Undergraduate/mj-cams'
r = S.get(url, timeout=30)
text = r.text
print(f'Status: {r.status_code}, Length: {len(text)}')
print(f'Has __NEXT_DATA__: {"__NEXT_DATA__" in text}')

# Look for JSON-LD
print('\n=== JSON-LD ===')
for m in re.finditer(r'<script[^>]*type=["\']?application/ld\+json["\']?[^>]*>(.*?)</script>', text, re.DOTALL | re.I):
    content = m.group(1)[:1000]
    print(content[:500])
    print('---')

# H1
print('\n=== H1 ===')
for m in re.finditer(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL | re.I):
    clean = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    print(f'  H1: {clean}')

# Get body text stripped of scripts
body_match = re.search(r'<body[^>]*>(.*)</body>', text, re.DOTALL)
if body_match:
    body_text = body_match.group(1)
    body_text = re.sub(r'<script[^>]*>.*?</script>', '', body_text, flags=re.DOTALL)
    body_text = re.sub(r'<style[^>]*>.*?</style>', '', body_text, flags=re.DOTALL)
    body_text = re.sub(r'<[^>]+>', ' ', body_text)
    body_text = re.sub(r'\s+', ' ', body_text)
    
    print('\n=== CRICOS candidates ===')
    for m in re.finditer(r'(?<!\w)[0-9]{6,7}[A-Za-z](?!\w)', body_text):
        start = max(0, m.start() - 60)
        ctx = body_text[start:m.end()+60]
        print(f'  {m.group(0)} ... {ctx.strip()[:200]}')
    
    print('\n=== Fee $ mentions ===')
    for m in re.finditer(r'\$[0-9,]+', body_text):
        start = max(0, m.start() - 80)
        ctx = body_text[start:m.end()+120]
        print(f'  ...{ctx.strip()[:250]}...\n')

# Duration mentions
print('\n=== Duration mentions ===')
for m in re.finditer(r'(\d+)\s*(year|month|week|semester)s?', body_text, re.I):
    start = max(0, m.start() - 40)
    ctx = body_text[start:m.end()+40]
    print(f'  {m.group(0)} ... {ctx.strip()[:120]}')

print('\n=== Intake/start mentions ===')
for m in re.finditer(r'(Semester|Trimester|February|March|July|August)\s*[,-]?\s*(\d{4}|Start)', body_text):
    start = max(0, m.start() - 40)
    ctx = body_text[start:m.end()+40]
    print(f'  {m.group(0)} ... {ctx.strip()[:120]}')
