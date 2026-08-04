#!/usr/bin/env python3
"""Extract structured data from saved Avondale course pages."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from curl_cffi import requests as curl_requests

base = "https://www.avondale.edu.au"

def extract_course_info(html, url_name):
    print(f"\n{'='*60}")
    print(f"COURSE: {url_name}")
    print(f"{'='*60}")
    
    # CRICOS Code
    cricos_matches = re.findall(r'CRICOS Code.*?(\d{5}[A-Z])', html, re.IGNORECASE | re.DOTALL)
    print(f"CRICOS Code: {cricos_matches if cricos_matches else 'NOT FOUND'}")
    
    # Also look for direct span content with CRICOS
    cricos_span = re.findall(r'CRICOS\s*Code[^<]*<\s*/\s*div[^>]*>\s*<\s*div[^>]*>\s*<\s*span[^>]*>\s*(\d{5}[A-Z])\s*<\s*/\s*span', html, re.IGNORECASE | re.DOTALL)
    print(f"CRICOS Span: {cricos_span if cricos_span else 'NOT FOUND (div layout)'}")
    
    # Also try the simpler pattern
    for m in re.finditer(r'CRICOS.{0,30}?(\d{5}[A-Z])', html, re.IGNORECASE):
        print(f"  CRICOS context: ...{m.group()[:80]}...")

    # Duration
    duration_patterns = [
        r'<span[^>]*>[^<]*(Full.time|Part.time|years?|semester)[^<]*</span>',
        r'Duration[^<]*<\s*/\s*div[^>]*>\s*<\s*div[^>]*>(.*?)<\s*/\s*div',
    ]
    for pat in duration_patterns:
        matches = re.findall(pat, html, re.IGNORECASE | re.DOTALL)
        if matches:
            print(f"Duration matches ({pat[:30]}): {matches[:3]}")
            break
    else:
        print("Duration: Not found with regex patterns")
    
    # Study Mode
    mode = re.findall(r'Study Mode[^<]*<\s*/\s*div[^>]*>\s*<\s*div[^>]*>\s*<\s*div[^>]*>\s*<\s*span[^>]*>(.*?)<\s*/\s*span', html, re.IGNORECASE | re.DOTALL)
    print(f"Study Mode: {mode[:2] if mode else 'NOT FOUND'}")
    
    # Location
    loc = re.findall(r'Location[^<]*<\s*/\s*div[^>]*>\s*<\s*div[^>]*>(.*?)<\s*/\s*div', html, re.IGNORECASE | re.DOTALL)
    print(f"Location: {[re.sub(r'<[^>]+>','', l).strip() for l in loc[:2]] if loc else 'NOT FOUND'}")
    
    # Fee info
    fees = re.findall(r'(?:Fee|fees|Fees and Costs|tuition).{0,100}(?:\$[\d,]+\.?\d*)', html, re.IGNORECASE)
    if fees:
        print(f"Fee mentions: {fees[:5]}")
    else:
        print("Fee: No mention in page (likely separate fees page)")
    
    # Fee-specific links
    fee_links = re.findall(r'<a[^>]*href=["\']([^"\']*fee[^"\']*)["\']', html, re.IGNORECASE)
    if fee_links:
        print(f"Fee links: {fee_links[:3]}")
    
    # International student section
    intl_section = re.findall(r'international.{0,200}?(?:fee|cost|CRICOS|visa|Overseas)', html, re.IGNORECASE)
    if intl_section:
        print(f"International mentions: {len(intl_section)}")
        for s in intl_section[:3]:
            print(f"  - {s.strip()[:150]}")

# 1. Check already-saved pages
print("=" * 60)
print("ANALYZING SAVED COURSE PAGES")
print("=" * 60)

for fname in ["avondale_bachelor_of_nursing.html", "avondale_bachelor_of_business.html", "avondale_master_of_teaching_primary.html"]:
    try:
        with open(f"scratch/{fname}", "r", encoding="utf-8") as f:
            html = f.read()
        extract_course_info(html, fname.replace(".html", "").replace("avondale_", ""))
    except FileNotFoundError:
        print(f"\nFile not found: scratch/{fname}")

# 2. Fetch a couple more course pages
print("\n" + "="*60)
print("FETCHING MORE COURSE PAGES")
print("="*60)

more_courses = [
    "https://www.avondale.edu.au/course/diploma-of-business/",
    "https://www.avondale.edu.au/course/bachelor-of-arts/",
    "https://www.avondale.edu.au/course/bachelor-of-science-bachelor-of-teaching/",
]

for url in more_courses:
    name = url.rstrip("/").split("/")[-1]
    print(f"\n--- {name} ---")
    try:
        r = curl_requests.get(url, impersonate="chrome", timeout=30)
        html = r.text
        safe = name.replace("-", "_")
        with open(f"scratch/avondale_{safe}.html", "w", encoding="utf-8") as f:
            f.write(html)
        extract_course_info(html, name)
    except Exception as e:
        print(f"  ERROR: {e}")

# 3. Check the international study page for fee/tuition info
print("\n" + "="*60)
print("INTERNATIONAL PAGE")
print("="*60)
try:
    r = curl_requests.get("https://www.avondale.edu.au/international/", impersonate="chrome", timeout=30)
    html = r.text
    with open("scratch/avondale_international.html", "w", encoding="utf-8") as f:
        f.write(html)
    # Extract fee info for international
    for m in re.finditer(r'(?:fee|tuition|cost|CRICOS|Overseas|international\s+student|visa).{0,200}', html, re.IGNORECASE):
        text = m.group().strip()
        if any(kw in text.lower() for kw in ['fee', 'tuition', 'cricos', 'cost', 'overseas']):
            print(f"  {text[:200]}")
except Exception as e:
    print(f"  ERROR: {e}")

# 4. Check the courses listing page structure
print("\n" + "="*60)
print("COURSES LISTING PAGE STRUCTURE")
print("="*60)
path = f"{base}/courses/"
r = curl_requests.get(path, impersonate="chrome", timeout=30)
html = r.text
# Find all course card/article links
links = re.findall(r'<a[^>]*href="(https?://www\.avondale\.edu\.au/course/[^"]*)"[^>]*>(.*?)</a>', html, re.IGNORECASE | re.DOTALL)
print(f"Course links on listing page: {len(links)}")
for href, text in links[:20]:
    text_clean = re.sub(r'<[^>]+>', '', text).strip()
    print(f"  - {href} -> {text_clean[:80]}")

# Check for category-based filtering
categories = re.findall(r'study/[a-z-]+', html, re.IGNORECASE)
cats = sorted(set(c for c in categories))
print(f"\nStudy area categories: {cats}")

print("\n" + "="*60)
print("DONE")
print("="*60)
