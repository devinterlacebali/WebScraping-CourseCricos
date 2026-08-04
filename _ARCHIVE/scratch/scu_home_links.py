from curl_cffi import requests
import re

r = requests.get('https://www.scu.edu.au/', impersonate='chrome124')

# Find all hrefs
links = re.findall(r'href=["\']([^"\']+)["\']', r.text)
course_links = [l for l in set(links) if any(x in l.lower() for x in ['course', 'study', 'degree'])]
print('=== Course/Study related links from homepage ===')
for l in sorted(course_links):
    if l.startswith('/') or 'scu.edu.au' in l:
        print(l)

print()
print('Other interesting links (future/international/find/program):')
for l in sorted(set(links)):
    if any(x in l.lower() for x in ['future', 'international', 'program', 'find', 'study-area']):
        if l.startswith('/') or 'scu.edu.au' in l:
            print(l)
