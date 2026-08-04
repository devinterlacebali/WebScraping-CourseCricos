"""WSU - build URLs from CSV titles and try to fetch."""
import sys, re, csv, time
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl
from bs4 import BeautifulSoup

DOMAIN = 'https://www.westernsydney.edu.au'

# Load CSV for provider 00917K
csv_courses = []
with open('cricos-courses.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row and row[0].strip() == '00917K':
            csv_courses.append({
                'cricos': row[2].strip(),
                'title': row[3].strip() if len(row) > 3 else '',
                'level': row[12].strip().lower() if len(row) > 12 else '',
            })

print(f'CSV: {len(csv_courses)} courses')

# Try to find course detail URLs from sitemap for nursing
# From earlier: course URLs at /future/study/courses/{level}/{slug}
# Let's search sitemap for bachelor-of-nursing
r = curl.get(f'{DOMAIN}/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
nursing_in_sitemap = [u for u in urls if 'nurs' in u.lower() and 'future/study' in u]
print(f'Nursing in sitemap: {len(nursing_in_sitemap)}')
for u in sorted(nursing_in_sitemap)[:5]:
    print(f'  {u}')

# Try to match course URLs from different pages
# Check if /future/study/courses page has embedded data
r2 = curl.get(f'{DOMAIN}/future/study/courses', impersonate='chrome120', timeout=30)
s2 = BeautifulSoup(r2.text, 'html.parser')

# Look for any data attributes with course info
for el in s2.find_all(attrs={'data-course': True})[:5]:
    print(f'data-course: {el["data-course"][:200]}')
for el in s2.find_all(attrs={'data-code': True})[:5]:
    print(f'data-code: {el["data-code"][:200]}')

# Look for JSON-LD
for sc in s2.find_all('script', type='application/ld+json'):
    print(f'JSON-LD: {sc.string[:200]}')

# Hardcoded: try generating URLs from well-known courses
print('\n=== Generate URLs from CSV titles ===')
# WSU URL pattern: /future/study/courses/{level}/{kebab-title}
# level = 'undergraduate' for bachelor/associate, 'postgraduate' for master/graduate

def title_to_slug(title):
    """Convert course title to WSU URL slug."""
    slug = title.lower()
    # Remove special chars
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    slug = re.sub(r'-{2,}', '-', slug)
    return slug[:80]

def guess_level(title, level_from_csv):
    """Guess if undergraduate or postgraduate from title."""
    t = title.lower()
    if level_from_csv:
        csv_lower = level_from_csv.strip().lower()
        if 'master' in csv_lower or 'graduate' in csv_lower or 'postgrad' in csv_lower:
            return 'postgraduate'
        if 'bachelor' in csv_lower or 'diploma' in csv_lower or 'certificate' in csv_lower:
            return 'undergraduate'
    if any(k in t for k in ['master', 'graduate', 'phd', 'doctor']):
        return 'postgraduate'
    if any(k in t for k in ['bachelor', 'diploma', 'certificate', 'associate']):
        return 'undergraduate'
    return 'undergraduate'  # default

# Test with 5 nursing courses
nursing = [c for c in csv_courses if 'nurs' in c['title'].lower()]
print(f'\nNursing courses: {len(nursing)}')
for nc in nursing[:5]:
    level = guess_level(nc['title'], nc['level'])
    slug = title_to_slug(nc['title'])
    url = f'{DOMAIN}/future/study/courses/{level}/{slug}'
    try:
        r3 = curl.get(url, impersonate='chrome120', timeout=15)
        if r3.status_code == 200 and len(r3.text) > 5000:
            s3 = BeautifulSoup(r3.text, 'html.parser')
            h1 = s3.find('h1')
            body = re.sub(r'\s+', ' ', r3.text)
            cricos_in_page = bool(re.search(r'CRICOS', body))
            print(f'{nc["cricos"]} | {nc["title"][:50]} | {url.split("/")[-1][:40]} | {r3.status_code} | CRICOS={cricos_in_page}')
            if cricos_in_page:
                for m in re.finditer(r'CRICOS.{0,60}', body):
                    print(f'  {m.group()[:80]}')
                    break
        else:
            # Try alternate level
            alt_level = 'postgraduate' if level == 'undergraduate' else 'undergraduate'
            url2 = f'{DOMAIN}/future/study/courses/{alt_level}/{slug}'
            r4 = curl.get(url2, impersonate='chrome120', timeout=15)
            if r4.status_code == 200 and len(r4.text) > 5000:
                s4 = BeautifulSoup(r4.text, 'html.parser')
                print(f'{nc["cricos"]} | {nc["title"][:50]} | {url2.split("/")[-1][:40]} | {r4.status_code} | CRICOS={bool(re.search(r"CRICOS", r4.text))}')
            else:
                print(f'{nc["cricos"]} | {nc["title"][:50]} | {slug[:40]} | {r3.status_code}')
    except Exception as e:
        print(f'{nc["cricos"]} | {nc["title"][:50]} | ERROR: {str(e)[:30]}')
