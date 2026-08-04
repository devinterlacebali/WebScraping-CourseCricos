"""
uowc_04_course_pages.py — Cek course structure & SSR pada UOW College course listing
"""

import sys
sys.path.insert(0, r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\venv\Lib\site-packages')

from curl_cffi import requests
import re

pages = [
    "https://www.uowcollege.edu.au/courses-pathways/",
    "https://www.uowcollege.edu.au/courses-pathways/business/",
    "https://www.uowcollege.edu.au/courses-pathways/diploma-nursing/",
    "https://www.uowcollege.edu.au/courses-pathways/engineering/engineering-listings/",
    "https://www.uowcollege.edu.au/courses-pathways/english-language/",
]

for url in pages:
    r = requests.get(url, impersonate="chrome", timeout=30)
    text = r.text
    print(f"\n{'='*70}")
    print(f"URL: {url}")
    print(f"Status: {r.status_code} | Size: {len(text)} bytes")

    # Cek SSR — apakah course data ada di HTML atau JS?
    # Cek apakah ada course title di HTML
    headings = re.findall(r'<h[1-4][^>]*>([^<]+)</h[1-4]>', text)
    print(f"  Headings found: {len(headings)}")
    for h in headings[:8]:
        print(f"    - {h.strip()}")

    # Cek CRICOS mention
    cricos_in_html = 'CRICOS' in text
    print(f"  CRICOS in HTML: {cricos_in_html}")

    # Cek duration/intake/price di HTML
    for term in ['Duration', 'duration', 'Starts', 'Intake', 'Fee', 'CRICOS', 'Location', 'location']:
        matches = re.findall(rf'{term}[^<]*<[^>]*>[^<]*', text, re.IGNORECASE) 
        if matches:
            for m in matches[:3]:
                clean = re.sub(r'<[^>]+>', '', m).strip()
                print(f"  [{term}]: {clean}")

    # Apakah ada script dengan JSON course data?
    scripts_with_course = re.findall(r'<script[^>]*>([^<]*course[^<]*)</script>', text, re.IGNORECASE | re.DOTALL)
    scripts_with_diploma = re.findall(r'<script[^>]*>([^<]*diploma[^<]*)</script>', text, re.IGNORECASE | re.DOTALL)
    print(f"  Scripts containing 'course': {len(scripts_with_course)}")
    print(f"  Scripts containing 'diploma': {len(scripts_with_diploma)}")

    # Apakah data dimuat via XHR? Cek fetch/XHR references
    xhr_refs = re.findall(r'(fetch|XMLHttpRequest|axios|api\.)', text)
    print(f"  XHR/API references: {len(xhr_refs)}")

    print(f"  SSR kesimpulan: {'SERVER-SIDE RENDERED' if not scripts_with_course and not xhr_refs else 'Hybrid/Client-side render'}")

print("\n\n=== DETAILED COURSE PAGE ANALYSIS ===")
# Check 1 course detail page thoroughly
detail_url = "https://www.uowcollege.edu.au/courses-pathways/diploma-nursing/"
r = requests.get(detail_url, impersonate="chrome", timeout=30)
text = r.text

print(f"\nAnalyzing: {detail_url}")

# Extract structured data from HTML
print("\n--- Course meta data in HTML ---")
patterns = {
    'Location': r'Location[:\s]*</strong>[^<]*<[^>]*>([^<]+)',
    'Duration': r'Duration[:\s]*</strong>[^<]*<[^>]*>([^<]+)',
    'Pathways': r'Pathways[:\s]*</strong>[^<]*<[^>]*>([^<]+)',
    'Starts': r'Starts[:\s]*</strong>[^<]*<[^>]*>([^<]+)',
    'National Code': r'NATIONAL CODE[:\s]*<[^>]*>([^<]+)',
}

for label, pat in patterns.items():
    m = re.search(pat, text, re.IGNORECASE)
    if m:
        print(f"  {label}: {m.group(1).strip()}")
    else:
        print(f"  {label}: NOT FOUND in HTML (might be JS-rendered)")
