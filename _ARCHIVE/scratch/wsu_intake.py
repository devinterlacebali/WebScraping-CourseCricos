"""WSU - try find intake from course pages."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Try to find a course detail page with SSR
# Check inherent-requirements which has nursing course pages
r = curl.get(f'{DOMAIN}/inherent-requirements/bachelor-of-nursing-inherent-requirements', impersonate='chrome120', timeout=30)
if r.status_code == 200:
    s = BeautifulSoup(r.text, 'html.parser')
    body = re.sub(r'\s+', ' ', s.get_text())
    # Look for intake, session, semester, start months
    for kw in ['intake', 'session', 'semester', 'start date', 'commence', 'study period']:
        for m in re.finditer(kw + r'.{0,100}', body, re.I):
            print(f'{kw}: {m.group()[:120]}')
            break

# Try future/study pages  
print('\n=== /future ===')
r2 = curl.get(f'{DOMAIN}/future', impersonate='chrome120', timeout=30)
s2 = BeautifulSoup(r2.text, 'html.parser')
links = [a['href'] for a in s2.find_all('a', href=True)]
print(f'Links: {len(links)}')
course_links = [l for l in links if 'course' in l.lower() or 'degree' in l.lower() or 'study' in l.lower()]
for l in sorted(course_links)[:8]:
    print(f'  {l}')

# Check if courses are under /study or /schools/
print('\n=== Schools ===')
r3 = curl.get(f'{DOMAIN}/schools', impersonate='chrome120', timeout=30)
s3 = BeautifulSoup(r3.text, 'html.parser')
links3 = [a['href'] for a in s3.find_all('a', href=True)]
school_links = [l for l in links3 if '/schools/' in l.lower() and len(l.split('/')) > 4]
print(f'School links: {len(school_links)}')
for l in sorted(school_links)[:3]:
    print(f'  {l}')
    # Check this school's course page
    r4 = curl.get(f'{DOMAIN}{l}', impersonate='chrome120', timeout=15)
    s4 = BeautifulSoup(r4.text, 'html.parser')
    body4 = re.sub(r'\s+', ' ', s4.get_text())
    for kw in ['intake', 'session', 'semester', 'start']:
        for m in re.finditer(kw + r'.{0,80}', body4, re.I):
            print(f'    {m.group()[:100]}')
            break
