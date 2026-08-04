#!/usr/bin/env python3
"""Avondale University exploration — www.avondale.edu.au
Checks: Cloudflare, footer CRICOS, sitemap, course page SSR."""

import asyncio
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

# Ensure we're in venv
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from curl_cffi import requests as curl_requests
    print("[OK] curl_cffi imported successfully")
    CURL_AVAILABLE = True
except ImportError:
    print("[!] curl_cffi not available, falling back to urllib")
    CURL_AVAILABLE = False


async def main():
    base_url = "https://www.avondale.edu.au"
    
    # 1. Cloudflare check: fetch homepage with curl_cffi
    print("\n" + "="*60)
    print("1. HOMEPAGE FETCH (Cloudflare check)")
    print("="*60)
    try:
        if CURL_AVAILABLE:
            r = curl_requests.get(base_url, impersonate="chrome", timeout=30)
            print(f"Status: {r.status_code}")
            print(f"Content-Length: {len(r.text)} bytes")
            print(f"URL: {r.url}")
            
            # Check for CF indicators
            cf_indicators = ["cloudflare", "__cf_bm", "cf-ray", "cf-challenge", "iuam"]
            body_lower = r.text.lower()
            for ind in cf_indicators:
                if ind in body_lower:
                    print(f"  [!] Cloudflare indicator found: '{ind}'")
            
            # Check for JS challenge
            if "checking your browser" in body_lower or "attention required" in body_lower:
                print("  [!] Cloudflare challenge/JS challenge detected!")
            else:
                print("  [OK] No Cloudflare challenge detected")
            
            # Check response headers
            headers = dict(r.headers)
            cf_headers = {k: v for k, v in headers.items() if 'cf-' in k.lower() or 'cloudflare' in k.lower()}
            if cf_headers:
                print(f"  Cloudflare headers: {json.dumps(cf_headers, indent=2)}")
            else:
                print("  No Cloudflare headers found")
            
            # Save sample
            with open("scratch/avondale_homepage.html", "w", encoding="utf-8") as f:
                f.write(r.text)
            print("  Homepage saved to scratch/avondale_homepage.html")
        else:
            import urllib.request
            with urllib.request.urlopen(base_url, timeout=30) as resp:
                body = resp.read().decode()
                print(f"Status: {resp.status}")
                print(f"Content-Length: {len(body)} bytes")
    except Exception as e:
        print(f"  [ERROR] Fetch failed: {e}")
    
    # 2. CRICOS provider from footer
    print("\n" + "="*60)
    print("2. FOOTER CRICOS PROVIDER INFO")
    print("="*60)
    try:
        with open("scratch/avondale_homepage.html", "r", encoding="utf-8") as f:
            html = f.read()
        
        # Search for CRICOS patterns
        cricos_patterns = [
            r'CRICOS.*?(\d{5}[0-9A-Z])',
            r'cricos.*?(\d{5}[0-9A-Z])',
            r'Provider.*?(\d{5}[0-9A-Z])',
            r'PRV\d+',
            r'TEQSA',
            r'(\d{5}[0-9A-Z]).*?(?:provider|CRICOS)',
        ]
        
        for pat in cricos_patterns:
            matches = re.findall(pat, html, re.IGNORECASE)
            if matches:
                print(f"  Matched '{pat}': {matches}")
        
        # Grab footer text (~last 5000 chars)
        footer_text = html[-8000:]
        # Extract everything between footer tags if possible
        footer_match = re.search(r'<footer[^>]*>(.*?)</footer>', html, re.DOTALL | re.IGNORECASE)
        if footer_match:
            footer_html = footer_match.group(1)
            # Strip tags for readable text
            footer_clean = re.sub(r'<[^>]+>', ' ', footer_html)
            footer_clean = re.sub(r'\s+', ' ', footer_clean).strip()
            print(f"\n  Footer text:\n{footer_clean[:2000]}")
        else:
            print("  No <footer> tag found, searching broadly...")
            # Try to find CRICOS anywhere
            for m in re.finditer(r'.{0,100}(CRICOS|PRV|TEQSA|provider code).{0,100}', html, re.IGNORECASE):
                print(f"  {m.group().strip()}")
    except FileNotFoundError:
        print("  Homepage not saved yet, can't analyze footer")
    
    # 3. Sitemap analysis
    print("\n" + "="*60)
    print("3. SITEMAP /sitemap.xml")
    print("="*60)
    try:
        sitemap_url = urljoin(base_url, "/sitemap.xml")
        if CURL_AVAILABLE:
            r = curl_requests.get(sitemap_url, impersonate="chrome", timeout=30)
        else:
            import urllib.request
            with urllib.request.urlopen(sitemap_url, timeout=30) as resp:
                r = resp
        print(f"Status: {r.status_code}")
        print(f"Content-Type: {r.headers.get('content-type', 'N/A')}")
        
        if r.status_code == 200:
            body = r.text
            with open("scratch/avondale_sitemap.xml", "w", encoding="utf-8") as f:
                f.write(body)
            print(f"Size: {len(body)} bytes")
            
            # Parse URLs
            urls = re.findall(r'<loc>(.*?)</loc>', body, re.IGNORECASE)
            print(f"Total URLs in sitemap: {len(urls)}")
            
            # Check if it's a sitemap index
            if '<sitemapindex' in body.lower() or '<sitemap>' in body.lower():
                print("  [!] This is a SITEMAP INDEX (points to sub-sitemaps)")
                sub_sitemaps = re.findall(r'<loc>(.*?)</loc>', body, re.IGNORECASE)
                for ss in sub_sitemaps:
                    print(f"    Sub-sitemap: {ss}")
            else:
                # Categorize URLs
                course_urls = [u for u in urls if any(kw in u.lower() for kw in ['course', 'program', 'study', 'degree', 'diploma', 'certificate', 'bachelor', 'master', 'doctor', 'phd'])]
                print(f"  Course-like URLs: {len(course_urls)}")
                print(f"  Non-course URLs: {len(urls) - len(course_urls)}")
                
                # Sample course URLs
                for u in course_urls[:10]:
                    print(f"    - {u}")
                if len(course_urls) > 10:
                    print(f"    ... and {len(course_urls)-10} more")
        else:
            # Try alternative paths
            alt_paths = ["/sitemap_index.xml", "/sitemap1.xml", "/sitemap/", "/sitemap"]
            for ap in alt_paths:
                full_url = urljoin(base_url, ap)
                try:
                    r2 = curl_requests.get(full_url, impersonate="chrome", timeout=15)
                    if r2.status_code == 200:
                        print(f"  Found at {ap} (status {r2.status_code})")
                        urls = re.findall(r'<loc>(.*?)</loc>', r2.text, re.IGNORECASE)
                        print(f"  URLs: {len(urls)}")
                        break
                except:
                    pass
    except Exception as e:
        print(f"  [ERROR] Sitemap fetch failed: {e}")
    
    # 4. Check course listing / course pages
    print("\n" + "="*60)
    print("4. COURSE LISTING PAGE STRUCTURE")
    print("="*60)
    
    # Try common course listing paths
    listing_paths = [
        "/study/", "/courses/", "/course/", "/programs/", "/future-students/",
        "/international/", "/study-at-avondale/", "/academics/"
    ]
    
    for path in listing_paths:
        full_url = urljoin(base_url, path)
        try:
            r = curl_requests.get(full_url, impersonate="chrome", timeout=15)
            if r.status_code == 200:
                print(f"\n  [200] {full_url} ({len(r.text)} bytes)")
                # Look for course links
                course_links = re.findall(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>', r.text, re.IGNORECASE)
                course_rel = [c for c in course_links if any(kw in c.lower() for kw in ['course', 'program', 'degree', 'diploma', 'bachelor', 'master'])]
                if course_rel:
                    print(f"    Course links found: {len(course_rel)}")
                    for cl in course_rel[:8]:
                        print(f"      - {cl}")
        except:
            pass


if __name__ == "__main__":
    asyncio.run(main())
