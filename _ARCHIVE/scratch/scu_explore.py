"""
SCU (Southern Cross University) Exploration Script
==================================================
Comprehensive exploration of SCU website structure for CRICOS course data extraction.

Key findings:
- No Cloudflare → CloudFront (AWS)
- Funnelback search API: course-search.scu.edu.au/s/search.json
- Fully SSR course pages with JavaScript year/location selector
- Sitemap: /google-sitemap/index.xml (13,296 URLs)
- CRICOS provider: 01241G
"""

from curl_cffi import requests
from bs4 import BeautifulSoup
import json, re, csv

BASE = 'https://www.scu.edu.au'

def check_cloudflare():
    """Verify no Cloudflare protection."""
    r = requests.get(BASE + '/', impersonate='chrome124')
    headers_str = str(r.headers).lower()
    is_cf = 'cloudflare' in headers_str
    is_cfront = 'cloudfront' in headers_str
    return {
        'status': r.status_code,
        'server': r.headers.get('Server'),
        'via': r.headers.get('Via'),
        'cloudflare': is_cf,
        'cloudfront': is_cfront,
        'conclusion': 'CloudFront (AWS CDN)' if is_cfront else ('Cloudflare' if is_cf else 'No CDN detected')
    }

def check_sitemap():
    """Analyse sitemap."""
    r = requests.get(BASE + '/google-sitemap/index.xml', impersonate='chrome124')
    locs = re.findall(r'<loc>([^<]+)</loc>', r.text)
    course_urls = [u for u in locs if '/study/courses/' in u]
    unit_urls = [u for u in locs if '/study/units/' in u]
    news_urls = [u for u in locs if '/news/' in u]
    return {
        'total': len(locs),
        'course_urls': len(course_urls),
        'unit_urls': len(unit_urls),
        'news_urls': len(news_urls),
        'sample_course': course_urls[:3] if course_urls else []
    }

def check_cricos_provider():
    """Extract CRICOS provider code from footer."""
    r = requests.get(BASE + '/', impersonate='chrome124')
    soup = BeautifulSoup(r.text, 'html.parser')
    footer = soup.find('footer') or soup
    text = footer.get_text()
    cricos_match = re.search(r'CRICOS[^:]*:\s*(\w+)', text)
    teqsa_match = re.search(r'TEQSA[^:]*:\s*(\w+)', text)
    return {
        'cricos_provider': cricos_match.group(1) if cricos_match else 'Not found',
        'teqsa': teqsa_match.group(1) if teqsa_match else 'Not found',
    }

def check_csv_coverage(csv_path):
    """Count SCU courses in the CSV."""
    count = 0
    course_names = []
    unique_codes = set()
    levels = {}
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            if len(row) >= 4 and row[0].strip() == '01241G':
                count += 1
                course_names.append(row[3])
                unique_codes.add(row[2])
                level = row[12] if len(row) > 12 else 'N/A'
                levels[level] = levels.get(level, 0) + 1
    return {
        'total_rows': count,
        'unique_course_names': len(set(course_names)),
        'unique_cricos_codes': len(unique_codes),
        'levels': levels,
        'sample_names': list(set(course_names))[:10]
    }

def sample_course_page(url):
    """Parse a course page CRICOS, fee, duration, intake."""
    r = requests.get(url, impersonate='chrome124')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Extract CRICOS from availability tables
    cricos_codes = set()
    for td in soup.find_all('td'):
        text = td.get_text(strip=True)
        m = re.search(r'\b0\d{4}[A-Z0-9]\b', text)
        if m and len(m.group()) >= 6:
            cricos_codes.add(m.group())
    
    # Snapshot data
    snapshot = {
        'title': soup.title.string if soup.title else '',
        'domestic_fee': '',
        'international_fee': '',
        'duration': '',
        'start_dates': [],
        'cricos_courses': list(cricos_codes),
        'is_ssr': True,  # Content rendered in HTML
        'has_json_ld': bool(soup.find('script', type='application/ld+json'))
    }
    
    # Fee from DOM
    fee_elem = soup.find(id='dom_snapshot_fee')
    if fee_elem:
        snapshot['domestic_fee'] = fee_elem.get_text(strip=True)
    
    # International fee
    for tag in soup.find_all(string=re.compile(r'\$[\d,]+.*per unit')):
        snapshot['international_fee'] = tag.strip()[:100]
        break
    
    # Duration
    for div in soup.find_all('div', class_='course-snapshot__data'):
        text = div.get_text(strip=True)
        if 'year' in text and 'full-time' in text:
            snapshot['duration'] = text[:100]
            break
    
    # Start dates
    for div in soup.find_all('div', class_='course-snapshot__data'):
        text = div.get_text(strip=True)
        months = re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)', text)
        if months:
            snapshot['start_dates'] = months
    
    return snapshot

def check_listing_page():
    """Explore the course listing/search API."""
    url = 'https://course-search.scu.edu.au/s/search.json'
    params = {
        'collection': 'scu~sp-search',
        'profile': '_default',
        'query': '!padrenull',
        'sort': 'title',
        'num_ranks': 10,
    }
    r = requests.get(url, params=params, impersonate='chrome124')
    data = r.json()
    results = data.get('response', {}).get('resultPacket', {}).get('results', [])
    
    listing_info = {
        'api_url': url,
        'total_results': len(results),
        'result_structure': list(results[0].keys()) if results else [],
        'available_metadata': list(results[0].get('listMetadata', {}).keys()) if results else [],
        'sample_url': results[0].get('liveUrl') if results else '',
    }
    if results:
        listing_info['sample_meta'] = results[0].get('listMetadata', {})
    return listing_info


if __name__ == '__main__':
    print('='*70)
    print('SCU (Southern Cross University) Exploration')
    print('='*70)
    
    print('\n--- 1. Cloudflare Check ---')
    cf = check_cloudflare()
    for k,v in cf.items():
        print(f'  {k}: {v}')
    
    print('\n--- 2. Sitemap ---')
    sm = check_sitemap()
    for k,v in sm.items():
        print(f'  {k}: {v}')
    
    print('\n--- 3. Provider Code ---')
    pc = check_cricos_provider()
    for k,v in pc.items():
        print(f'  {k}: {v}')
    
    print('\n--- 4. CSV Coverage ---')
    csv_info = check_csv_coverage('cricos-courses.csv')
    for k,v in csv_info.items():
        print(f'  {k}: {v}')
    
    print('\n--- 5. Course Page Structure (SSR check) ---')
    for url in [
        'https://www.scu.edu.au/study/courses/diploma-of-business-2127279/',
        'https://www.scu.edu.au/study/courses/bachelor-of-nursing-3007011/',
    ]:
        print(f'\n  URL: {url}')
        cp = sample_course_page(url)
        print(f'  Title: {cp["title"]}')
        print(f'  Domestic fee: {cp["domestic_fee"]}')
        print(f'  Intl fee: {cp["international_fee"]}')
        print(f'  Duration: {cp["duration"]}')
        print(f'  Start dates: {cp["start_dates"]}')
        print(f'  CRICOS course codes: {cp["cricos_courses"]}')
        print(f'  SSR: {cp["is_ssr"]}')
    
    print('\n--- 6. Course Listing API ---')
    li = check_listing_page()
    for k,v in li.items():
        print(f'  {k}: {v}')
