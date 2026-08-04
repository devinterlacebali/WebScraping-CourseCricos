"""Notre Dame - find provider code + course pages."""
import sys, re, csv
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.notredame.edu.au'

# Check footer for CRICOS
r = curl.get(DOMAIN, impersonate='chrome120', timeout=30)
s = BeautifulSoup(r.text, 'html.parser')
body = r.text

# Find CRICOS provider code
for m in re.finditer(r'(?:CRICOS|Provider)[^0-9]*(\d{6}[A-Z])', body, re.I):
    print(f'CRICOS in footer: {m.group(1)}')

# Find all course URLs from sitemap
r2 = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r2.text)
course_urls = [u for u in urls if '/courses/' in u.lower() or '/degrees/' in u.lower() or '/study/' in u.lower()]
print(f'Course URLs from sitemap: {len(course_urls)}')
if course_urls:
    for u in course_urls[:5]:
        print(f'  {u}')

# Check CSV for various provider codes
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    codes = {}
    for row in reader:
        if not row or len(row) < 3: continue
        codes.setdefault(row[0].strip(), 0)
        codes[row[0].strip()] += 1

# Known Notre Dame code from memory
for code in ['01032F', '01269G', '01280A', '00898F', '00899E']:
    if code in codes:
        print(f'Code {code}: {codes[code]} courses in CSV')
