"""Murdoch - deeper page analysis, extract full text, find data in HTML."""
import requests, re, json, sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
S = requests.Session()
S.headers.update(HEADERS)

# Test multiple course pages
test_urls = [
    'https://www.murdoch.edu.au/course/Undergraduate/mj-cams',
    'https://www.murdoch.edu.au/course/Undergraduate/B1306',
    'https://www.murdoch.edu.au/course/Postgraduate/mj-advpraccrimpsych',
]

for url in test_urls:
    print(f'\n{"="*60}')
    print(f'URL: {url}')
    try:
        r = S.get(url, timeout=30)
        text = r.text
        
        # H1
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
        title = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else 'N/A'
        print(f'Title: {title}')
        
        # Get full body text
        body = re.search(r'<body[^>]*>(.*)</body>', text, re.DOTALL)
        if body:
            clean = re.sub(r'<script[^>]*>.*?</script>', '', body.group(1), flags=re.DOTALL)
            clean = re.sub(r'<style[^>]*>.*?</style>', '', clean, flags=re.DOTALL)
            clean = re.sub(r'<[^>]+>', ' ', clean)
            clean = re.sub(r'&nbsp;', ' ', clean)
            clean = re.sub(r'\s+', ' ', clean).strip()
        else:
            clean = ''
        
        # Overview / description
        ov_idx = clean.lower().find('overview')
        if ov_idx >= 0:
            print(f'Overview (first 500ch): {clean[ov_idx:ov_idx+500]}')
        
        # Fee mentions
        print('\nFee mentions:')
        for m in re.finditer(r'\$[0-9,]+', text):
            start = max(0, m.start()-60)
            ctx = text[start:m.end()+100]
            clean_ctx = re.sub(r'\s+', ' ', ctx)
            print(f'  {m.group(0)} -> ...{clean_ctx[:250]}')
        if not re.search(r'\$[0-9,]+', text):
            print('  (none found)')
        
        # Duration (year)
        print('\nDuration mentions:')
        for m in re.finditer(r'(\d+)\s*(year|semester|month|week|trimester)[s]?', clean, re.I):
            ctx = clean[max(0,m.start()-30):m.end()+60]
            print(f'  {m.group(0)} -> ...{ctx.strip()[:150]}')
        if not re.search(r'\d+\s*(year|semester|month)', clean, re.I):
            print('  (none found)')
        
        # Intake
        print('\nIntake/start mentions:')
        for m in re.finditer(r'(Semester|Trimester|February|January|March|April|May|June|July|August|September|October|November|December)\s*\d{0,4}', clean, re.I):
            ctx = clean[max(0,m.start()-20):m.end()+30]
            print(f'  {m.group(0)} -> ...{ctx.strip()[:100]}')
    except Exception as e:
        print(f'ERROR: {e}')
