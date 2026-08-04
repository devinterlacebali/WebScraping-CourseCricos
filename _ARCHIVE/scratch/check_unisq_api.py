"""Check USQ for API endpoints or Playwright approach."""
import requests, re, json

headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get('https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing', 
                 headers=headers, timeout=30)
html = r.text

# Look for API/GraphQL endpoints
for m in re.finditer(r'(https?://[^"\']*(?:api|graphql|fee|cost)[^"\']*)', html, re.I):
    print('Endpoint:', m.group(1)[:150])

# Check for any JSON in scripts
for m in re.finditer(r'<script[^>]*id="[^"]*data[^"]*"[^>]*>(.*?)</script>', html, re.DOTALL):
    txt = m.group(1)
    if 'fee' in txt.lower() or 'cost' in txt.lower():
        print(f'Data script ({len(txt)} chars): {txt[:200]}')

# Some universities use StudyLink or similar
# Check known patterns
known_patterns = [
    '/api/course/',
    '/api/v1/course/',
    '/course-data/',
    '/api/degree/',
    '/study/api/',
]
for pat in known_patterns:
    if pat in html:
        print(f'Pattern found: {pat}')

# Check Playwright
print('\nWill use Playwright to extract fee from USQ')
