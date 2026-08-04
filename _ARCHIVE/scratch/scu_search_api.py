from curl_cffi import requests
from bs4 import BeautifulSoup
import json, re

# Explore course search API for programmatic access
# Funnelback search - try programmatic params
search_url = 'https://course-search.scu.edu.au/s/search.html'
params = {
    'collection': 'scu~sp-search',
    'profile': '_default',
    'f.Tabs|scu~ds-courses': 'Courses',
    'sort': 'title',
    'num_ranks': 100,
}

print('=== Course Search API Attempt ===')
r = requests.get(search_url, params=params, impersonate='chrome124', timeout=30)
print(f'Status: {r.status_code}, Length: {len(r.text)}')
soup = BeautifulSoup(r.text, 'html.parser')

# Look for courses list
results = soup.find_all('div', class_='result-body')
print(f'Results found: {len(results)}')

# Look for JSON data embedded
for script in soup.find_all('script'):
    if script.string:
        if 'var' in script.string and 'courses' in script.string.lower():
            print(f'Found script with courses data: {script.string[:200]}')
            
# Check for JSON API endpoint
print('\n--- Try JSON endpoint ---')
json_params = dict(params)
json_params['format'] = 'json'
rj = requests.get(search_url, params=json_params, impersonate='chrome124', timeout=30)
print(f'JSON: Status={rj.status_code}, Content type={rj.headers.get("content-type","")}')
print(f'Body: {rj.text[:300]}')

# Try alternative
print('\n--- Try JSON structured endpoint ---')
rj2 = requests.get(
    'https://course-search.scu.edu.au/s/search.json',
    params=params,
    impersonate='chrome124',
    timeout=30
)
print(f'Status={rj2.status_code}, Body: {rj2.text[:500]}')
