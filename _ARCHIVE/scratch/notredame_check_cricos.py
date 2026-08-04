"""Notre Dame - check sitemap meta for CRICOS."""
import sys, re
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
from curl_cffi import requests as curl

# Get sitemap and check one course URL
r = curl.get('https://www.notredame.edu.au/sitemap.xml', impersonate='chrome120', timeout=30)
urls = re.findall(r'<loc>(.*?)</loc>', r.text)
course_urls = [u for u in urls if '/programs/' in u and re.search(r'/(undergraduate|postgraduate)/[a-z]', u)]
print(f'Course URLs: {len(course_urls)}')

# Check first 3 pages for CRICOS
for u in course_urls[:3]:
    r2 = curl.get(u, impersonate='chrome120', timeout=15)
    body = r2.text
    
    # Search for CRICOS in raw HTML (not JS)
    has_cricos_code = bool(re.search(r'\b\d{6,7}[A-Za-z]\b', body))
    has_provider = bool(re.search(r'01032F', body))
    has_cricos_word = bool(re.search(r'CRICOS', body, re.I))
    
    print(f'  {u.split("/")[-1][:35]}: CRICOS_code={has_cricos_code} provider={has_provider} CRICOS_word={has_cricos_word} | {len(body)}b')
    
    # Get all CRICOS-like numbers
    codes = re.findall(r'\b\d{6}[A-Za-z]\b', body)
    print(f'    Codes: {codes}')
