"""Check UWA API endpoints for course data."""
import requests, re, json

headers = {"User-Agent": "Mozilla/5.0"}

# Check if there's a JSON API
apis = [
    '/api/course/bachelor-of-nursing-honours',
    '/api/courses/bachelor-of-nursing-honours',
    '/study/api/courses/bachelor-of-nursing-honours',
    '/study/courses/bachelor-of-nursing-honours.json',
    '/sitecore/api/ssc/item/...',
    '/api/education/courses/bachelor-of-nursing-honours',
]

# Check for XHR endpoints in page source
r = requests.get('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours', 
                 headers=headers, timeout=30)
# Look for API URLs
for m in re.finditer(r'(?:fetch|axios|get|ajax)\([\'"]?([^\'")]*(?:api|course|fee|graphql)[^\'")]*)[\'")]', r.text, re.I):
    print('API call:', m.group(1)[:150])

# Check for graphql
if 'graphql' in r.text.lower():
    for m in re.finditer(r'(https?://[^\'")]*(?:graphql|api)[^\'")]*)', r.text, re.I):
        print('GraphQL:', m.group(1))

# Look for ANY JSON data in scripts  
for m in re.finditer(r'"@type"\s*:\s*"[^"]*Course[^"]*"', r.text):
    start = max(0, m.start() - 200)
    ctx = r.text[start:m.end()+500]
    print('JSON-LD course:', re.sub(r'\s+',' ',ctx)[:500])

print('\nDone')
