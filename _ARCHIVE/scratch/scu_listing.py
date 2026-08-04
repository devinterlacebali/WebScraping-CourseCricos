from curl_cffi import requests
import re
from bs4 import BeautifulSoup

# Check the international courses & fees page - likely the course listing
urls = [
    'https://www.scu.edu.au/study/international-courses-and-fees/',
    'https://www.scu.edu.au/study/',
]

for url in urls:
    print(f'\n{"="*60}')
    print(f'URL: {url}')
    print(f'{"="*60}')
    r = requests.get(url, impersonate='chrome124', timeout=30)
    print(f'Status: {r.status_code}, Length: {len(r.text)}')
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Find course links
    course_links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if '/study/courses/' in href:
            course_links.append(href)
    
    print(f'Course links on page: {len(set(course_links))}')
    for l in sorted(set(course_links))[:15]:
        title = a.get_text(strip=True)[:80] if a else ''
        print(f'  {l}')
    
    # Find structured data / JSON-LD
    for script in soup.find_all('script', type='application/ld+json'):
        print(f'\nJSON-LD found: {script.string[:200] if script.string else "empty"}...')
    
    # Check for any course list/grid
    print(f'\n--- Page sections ---')
    for h2 in soup.find_all('h2'):
        print(f'H2: {h2.get_text(strip=True)[:100]}')
    for h3 in soup.find_all('h3'):
        text = h3.get_text(strip=True)[:100]
        if any(x in text.lower() for x in ['course', 'study', 'degree', 'fee', 'bachelor', 'master']):
            print(f'H3: {text}')
