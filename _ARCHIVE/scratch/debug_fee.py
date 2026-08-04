"""Debug TAFE QLD fee extraction on working page"""
from curl_cffi import requests as curl_requests
from bs4 import BeautifulSoup
import re

url = 'https://tafeqld.edu.au/course/18/18014/diploma-of-marketing-and-communication'
resp = curl_requests.get(url, impersonate='chrome120', timeout=30)
html = resp.text
soup = BeautifulSoup(html, 'html.parser')
text = re.sub(r'\s+', ' ', soup.get_text(' ', strip=True))

# Test extract_fee logic
# 1. Full Fee / total course fee pattern
m = re.search(r'(?:Full\s*Fee|total course fee).{0,30}\$?\s*([\d,]+)', text, re.I)
print(f'Pattern 1 (Full Fee): {m.group(0) if m else "NONE"}')

# 2. Just dollar amounts in course detail section
# Find the cmp-custom-course-details section
detail_div = soup.find('div', class_=lambda c: c and 'course-detail' in str(c).lower())
if detail_div:
    detail_text = re.sub(r'\s+', ' ', detail_div.get_text(' ', strip=True))
    for m in re.finditer(r'\$([\d,]+)', detail_text):
        print(f'  $ in detail: {m.group(0)}')
else:
    print('No course-detail div found')

# Raw text search for $ in first 5000 chars
print()
print('Text around $ in first 5000 chars:')
for m in re.finditer(r'\$([\d,]+)', text[:5000]):
    start = max(0, m.start()-40)
    end = min(5000, m.end()+40)
    print(f'  at {m.start()}: ...{text[start:end]}...')

print()
print('Checking for Full Fee in full page...')
for m in re.finditer(r'Full\s*Fee', text, re.I):
    start = max(0, m.start()-60)
    end = min(len(text), m.end()+100)
    print(f'  Full Fee at {m.start()}: ...{text[start:end]}...')

print()
print('Checking course detail section...')
# Find the course info box
for div in soup.find_all('div'):
    cls = div.get('class', [])
    if any('course' in str(c).lower() and 'detail' in str(c).lower() for c in cls):
        print(f'Found: {cls}')
        print(div.get_text(' ', strip=True)[:500])
        break
