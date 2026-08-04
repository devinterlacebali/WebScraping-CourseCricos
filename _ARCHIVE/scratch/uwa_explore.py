"""UWA - explore course page structure."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re, json

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(H)

# Analyze a working UWA course page
url = 'https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours'
r = S.get(url, timeout=30)
text = r.text
print(f'Status: {r.status_code}, Size: {len(text)} bytes')

print('\n=== Course Meta Tags ===')
for m in re.finditer(r'<meta[^>]*name="([^"]+)"[^>]*content="([^"]+)"', text, re.I):
    name = m.group(1).lower()
    content = m.group(2)
    if any(k in name for k in ['cricos', 'fee', 'course', 'duration', 'intake', 'title', 'description']):
        print(f'  {m.group(1)}: {content[:100]}')

print('\n=== CRICOS ===')
# UWA provider code is 00126G, but individual courses have their own CRICOS codes
for m in re.finditer(r'CRICOS[^<]{0,50}([0-9]{5,7}[A-Za-z]?)', text, re.I):
    ctx = re.sub(r'\s+', ' ', text[max(0,m.start()-30):m.end()+80])
    print(f'  -> {m.group(0)} ... {ctx[:150]}')

print('\n=== JSON-LD ===')
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', text, re.DOTALL):
    try:
        data = json.loads(m.group(1))
        s = json.dumps(data, indent=2)
        if len(s) < 1000:
            print(s)
        else:
            print(s[:800] + '\n...')
    except:
        pass

print('\n=== Fee/Price mentions ===')
for m in re.finditer(r'\$[0-9,]+(?:\.\d{2})?', text):
    ctx = re.sub(r'\s+', ' ', text[max(0,m.start()-100):m.end()+100])
    if any(k in ctx.lower() for k in ['fee', 'year', 'tuition', 'annual', 'total', 'price']):
        print(f'  ${m.group(0)}: {ctx[:200]}')

print('\n=== Duration mentions ===')
for m in re.finditer(r'(\d+(?:\.\d+)?)\s*(year|semester|month)[s]?\s*full.?time', text, re.I):
    ctx = re.sub(r'\s+', ' ', text[max(0,m.start()-40):m.end()+40])
    print(f'  {m.group(0)}: {ctx[:150]}')

print('\n=== Intake/Start ===')
for m in re.finditer(r'(Semester|Trimester)\s+\d[,\s]+(\d{4})', text):
    ctx = re.sub(r'\s+', ' ', text[max(0,m.start()-50):m.end()+50])
    print(f'  {m.group(0)}: {ctx[:150]}')

print('\n=== H1/Title ===')
h1 = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
if h1:
    print(f'  {re.sub(r"<[^>]+>", "", h1.group(1)).strip()}')

print('\n=== Course code ===')
# Look for course code pattern like BACH-NURS, BH005 etc
for m in re.finditer(r'\b([A-Z]{2,4}\d{3,4})\b', text):
    ctx = re.sub(r'\s+', ' ', text[max(0,m.start()-30):m.end()+30])
    print(f'  {m.group(1)}: {ctx[:100]}')
