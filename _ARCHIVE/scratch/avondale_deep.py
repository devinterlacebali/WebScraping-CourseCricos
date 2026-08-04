#!/usr/bin/env python3
"""Avondale University — deep dive into course sitemap and course pages."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from curl_cffi import requests as curl_requests

base = "https://www.avondale.edu.au"

def fetch(url, desc=""):
    r = curl_requests.get(url, impersonate="chrome", timeout=30)
    print(f"  [{r.status_code}] {desc or url} ({len(r.text)} bytes)")
    return r.text

# 1. Course sitemap
print("=" * 60)
print("COURSE SITEMAP: /course-sitemap.xml")
print("=" * 60)
body = fetch(base + "/course-sitemap.xml", "course-sitemap.xml")
with open("scratch/avondale_course_sitemap.xml", "w", encoding="utf-8") as f:
    f.write(body)

urls = re.findall(r'<loc>(.*?)</loc>', body, re.IGNORECASE)
print(f"\nTotal course URLs in sitemap: {len(urls)}")
for i, u in enumerate(urls):
    print(f"  {i+1:3d}. {u}")

# 2. Check all sub-sitemaps for total URL count
print("\n" + "=" * 60)
print("ALL SUB-SITEMAPS — TOTAL URL COUNTS")
print("=" * 60)
sitemap_index = fetch(base + "/sitemap.xml", "sitemap index")
subs = re.findall(r'<loc>(.*?)</loc>', sitemap_index, re.IGNORECASE)
total_all = 0
for sub in subs:
    name = sub.split("/")[-1]
    try:
        sub_body = fetch(sub, name)
        sub_urls = re.findall(r'<loc>(.*?)</loc>', sub_body, re.IGNORECASE)
        print(f"    -> {len(sub_urls)} URLs")
        total_all += len(sub_urls)
    except Exception as e:
        print(f"    -> ERROR: {e}")
print(f"\nTOTAL URLs across all sitemaps: {total_all}")

# 3. Course detail pages — SSR check
print("\n" + "=" * 60)
print("COURSE DETAIL PAGES — SSR CHECK")
print("=" * 60)

course_samples = [
    "https://www.avondale.edu.au/course/bachelor-of-nursing/",
    "https://www.avondale.edu.au/course/bachelor-of-business/",
    "https://www.avondale.edu.au/course/master-of-teaching-primary/",
]

for course_url in course_samples:
    name = course_url.rstrip("/").split("/")[-1]
    print(f"\n--- {name} ---")
    html = fetch(course_url, course_url)
    
    # Save HTML for inspection
    safe_name = name.replace("-", "_")
    with open(f"scratch/avondale_{safe_name}.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    # Check SSR: is CRICOS code present in HTML?
    cricos = re.findall(r'CRICOS[:\s]*(\d{5}[0-9A-Z])', html, re.IGNORECASE)
    print(f"  CRICOS code(s): {cricos if cricos else 'NOT FOUND'}")
    
    # Fee
    fee_patterns = [
        r'\$\s*[\d,]+\.?\d*\s*(?:per\s*year|pa|annum|total)',
        r'(?:tuition|fee|cost|price|indicative).{0,50}\$\s*[\d,]+\.?\d*',
        r'\$\s*[\d,]+\.?\d*',
    ]
    for pat in fee_patterns:
        matches = re.findall(pat, html, re.IGNORECASE)
        if matches:
            print(f"  Fee matches: {matches[:5]}")
            break
    else:
        print("  Fee: NOT FOUND in raw HTML")
    
    # Duration
    duration_patterns = [
        r'(\d+)\s*(?:year|semester|trimester|month)',
        r'duration.{0,30}(\d+\s*(?:year|semester))',
        r'(?:full.time|part.time)',
        r'(\d+)\s*(?:years?\s+full.time)',
    ]
    for pat in duration_patterns:
        matches = re.findall(pat, html, re.IGNORECASE)
        if matches:
            print(f"  Duration matches: {matches[:5]}")
            break
    else:
        print("  Duration: NOT FOUND in raw HTML")
    
    # Intake / Start dates
    intake = re.findall(r'(?:intake|start|commence|session|semester|trimester).{0,50}(?:february|march|july|august|january|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|\d{4}|\d{2}/\d{2})', html, re.IGNORECASE)
    print(f"  Intake mentions: {len(intake)}")
    for i in intake[:5]:
        print(f"    - {i.strip()}")
    
    # Check for JSON-LD / structured data
    jsonld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if jsonld:
        print(f"  JSON-LD blocks: {len(jsonld)}")
        for j in jsonld[:2]:
            try:
                data = json.loads(j)
                print(f"    @type: {data.get('@type', 'N/A')}")
                print(f"    name: {data.get('name', 'N/A')}")
                if 'description' in data:
                    print(f"    description: {data['description'][:100]}...")
            except:
                print(f"    (parse error)")
    
    # Check for JavaScript-heavy content indicators
    js_indicators = ['<script src=', 'react', 'vue', 'angular', 'ng-', 'v-bind', 'v-model', ':src=']
    js_count = sum(1 for ind in js_indicators if ind.lower() in html.lower())
    print(f"  JS framework indicators: {js_count}/7")
    
    # Check if page content is actually rendered (look for visible text content)
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    if body_match:
        body_text = re.sub(r'<[^>]+>', ' ', body_match.group(1))
        body_text = re.sub(r'\s+', ' ', body_text).strip()
        print(f"  Body text length: {len(body_text)} chars")
        # Look for course-specific content
        course_terms = ['course', 'program', 'unit', 'credit', 'prerequisite', 'overseas', 'international']
        found_terms = [t for t in course_terms if t in body_text.lower()]
        print(f"  Course content terms found: {found_terms}")
    
    # Check for Ajax/API-driven content
    xhr_patterns = ['api/', 'wp-json', '/graphql', 'rest_route', 'admin-ajax']
    for xhr in xhr_patterns:
        if xhr in html.lower():
            print(f"  REST/API endpoint found: {xhr}")
            break

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)
