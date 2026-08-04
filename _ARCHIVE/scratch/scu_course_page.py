from curl_cffi import requests
import re

# Try a couple of course pages from the sitemap
course_urls = [
    'https://www.scu.edu.au/study/courses/diploma-of-business-2127279/',
    'https://www.scu.edu.au/study/courses/bachelor-of-nursing-3007011/',
]

for url in course_urls:
    print(f'\n{"="*60}')
    print(f'URL: {url}')
    print(f'{"="*60}')
    r = requests.get(url, impersonate='chrome124')
    print(f'Status: {r.status_code}, Length: {len(r.text)}')
    
    # Check for SSR signs (content rendered in HTML)
    body = r.text
    
    # Search for common course details
    print('\n--- CRICOS ---')
    for m in re.finditer(r'(?i)(?:cricos|provider code)[^<]{0,80}', body):
        print(m.group()[:150])
    for m in re.finditer(r'\b0[0-9]{3}[A-F0-9][A-Z0-9]\b', body):
        print(f'  Found code-like: {m.group()}')
    
    print('\n--- Fee / Tuition ---')
    for m in re.finditer(r'(?i)(?:fee|tuition|cost|\$)[^<]{0,100}', body):
        snippet = m.group()[:150]
        if '$' in snippet or 'fee' in snippet.lower() or 'tuition' in snippet.lower():
            print(snippet)
    
    print('\n--- Duration ---')
    for m in re.finditer(r'(?i)(?:duration|year|month|week|semester)[^<]{0,80}', body):
        if any(x in m.group().lower() for x in ['year', 'month', 'week', 'semester', 'duration']):
            print(m.group()[:120])
    
    print('\n--- Intake / Session ---')
    for m in re.finditer(r'(?i)(?:intake|session|start date|commence)[^<]{0,80}', body):
        print(m.group()[:120])
    
    # Check if it's SSR - look for course content in HTML vs needing JS
    has_js_rendered = 'data-react' in body or 'ng-app' in body or '__NEXT_DATA__' in body
    has_static_content = bool(re.search(r'(?i)(?:course overview|about this course|key information)', body))
    print(f'\n--- Tech Check ---')
    print(f'JS framework detected: {has_js_rendered}')
    print(f'Static course content: {has_static_content}')
    
    # Save sample
    with open(f'scratch/scu_course_sample_{url.split("/")[-2]}.html', 'w', encoding='utf-8') as f:
        f.write(body)
    print(f'Saved sample to scratch/')
