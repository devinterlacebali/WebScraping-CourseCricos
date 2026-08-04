"""USC - check accessibility, try different approaches."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

DOMAIN = 'https://www.unisc.edu.au'

# Check homepage
r = curl.get(DOMAIN + '/', impersonate='chrome120', timeout=15)
print(f'Homepage: {r.status_code} ({len(r.text)} bytes)')

# Check robots.txt
r2 = curl.get(DOMAIN + '/robots.txt', impersonate='chrome120', timeout=15)
print(f'robots.txt: {r2.status_code} ({len(r2.text)} bytes)')
if len(r2.text) > 10:
    # Find sitemap
    for m in re.finditer(r'Sitemap:\s*(.*)', r2.text, re.I):
        print(f'  Sitemap: {m.group(1)}')
    
# Try with different user-agent
r3 = curl.get(DOMAIN + '/sitemap.xml', impersonate='chrome124', timeout=15)
print(f'Sitemap (chrome124): {r3.status_code} ({len(r3.text)} bytes)')

# Check course pages directly
for path in ['/study/courses-and-programs/bachelor-degrees-undergraduate-programs/bachelor-of-computer-science',
             '/study/courses-and-programs/graduate-degrees-postgraduate-programs/master-of-data-science']:
    r4 = curl.get(DOMAIN + path, impersonate='chrome120', timeout=15)
    print(f'{path.split("/")[-1][:30]}: {r4.status_code} ({len(r4.text)} bytes)')
    if r4.status_code == 200 and len(r4.text) > 1000:
        # Extract course URLs from the page
        course_links = re.findall(r'href=[\'"]([^\'"]*courses-and-programs[^\'"]*)[\'"]', r4.text)
        print(f'  Course links on page: {len(course_links)}')
        for l in course_links[:3]:
            print(f'    {l}')
