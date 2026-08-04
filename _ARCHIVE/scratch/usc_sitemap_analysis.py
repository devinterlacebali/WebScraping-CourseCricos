"""
USC/UniSC Sitemap Analysis
Checks: /XMLsitemap, counts URLs, course URLs
"""
import requests
import xml.etree.ElementTree as ET
import re
import json
from collections import Counter

SITEMAP_URL = "https://www.unisc.edu.au/XMLsitemap"

def main():
    print(f"[+] Fetching sitemap: {SITEMAP_URL}")
    r = requests.get(SITEMAP_URL, timeout=120)
    print(f"    Status: {r.status_code}, Size: {len(r.text):,} bytes")
    
    root = ET.fromstring(r.content)
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    loc_elems = root.findall('.//ns:loc', ns)
    all_urls = [e.text for e in loc_elems]
    
    print(f"\n{'='*60}")
    print(f"TOTAL URLs in sitemap: {len(all_urls):,}")
    print(f"{'='*60}")
    
    # Category breakdown
    categories = Counter()
    for u in all_urls:
        path = u.replace('https://www.unisc.edu.au/', '')
        parts = path.split('/')
        cat = parts[0] if parts[0] else 'root'
        categories[cat] += 1
    
    print(f"\nURL categories:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  /{cat}/: {count:,}")
    
    # Course URLs
    course_urls = [u for u in all_urls if '/study/courses-and-programs/' in u.lower()]
    print(f"\nCourse/program URLs (incl. location variants): {len(course_urls):,}")
    
    # Unique course base URLs
    unique_courses = set()
    for url in course_urls:
        path = url.replace('https://www.unisc.edu.au/study/courses-and-programs/', '')
        base = re.sub(
            r'/(sunshine-coast|moreton-bay|caboolture|gympie|fraser-coast|online|south-bank|petrie)-[^/]+-commencement.*$', 
            '', path
        )
        unique_courses.add(base)
    
    print(f"Unique course/program base paths: {len(unique_courses):,}")
    
    # Course types
    print(f"\nSample of course page types:")
    course_types = Counter()
    for u in course_urls[:500]:
        path = u.replace('https://www.unisc.edu.au/study/courses-and-programs/', '')
        if path.count('/') >= 1:
            level = path.split('/')[0]
            course_types[level] += 1
    
    for ct, cnt in sorted(course_types.items(), key=lambda x: -x[1]):
        print(f"  /{ct}/: {cnt}")
    
    # Save sample URLs
    print(f"\nFirst 20 course URLs:")
    for u in sorted(course_urls)[:20]:
        print(f"  {u}")

if __name__ == '__main__':
    main()
