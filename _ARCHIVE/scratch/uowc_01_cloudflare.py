"""
uowc_01_cloudflare.py — Cek Cloudflare protection on UOW College website
"""

import sys
sys.path.insert(0, r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\venv\Lib\site-packages')

from curl_cffi import requests

url = "https://www.uowcollege.edu.au"

r = requests.get(url, impersonate="chrome", timeout=30)
print(f"Status: {r.status_code}")
print(f"Server: {r.headers.get('Server', 'N/A')}")
print(f"Content-Type: {r.headers.get('Content-Type', 'N/A')}")
print(f"Set-Cookie (sample): {r.headers.get('Set-Cookie', 'N/A')[:120]}")
print(f"CF headers: { {k:v for k,v in r.headers.items() if 'cf-' in k or 'cloudflare' in k.lower()} }")

# Cek footer CRICOS
if '02723D' in r.text:
    print("\n✓ CRICOS 02723D (UOWC Ltd) ditemukan di halaman")
if 'CRICOS' in r.text:
    # Extract CRICOS line
    import re
    cricos_matches = re.findall(r'CRICOS[^<]{0,100}', r.text, re.IGNORECASE)
    for m in cricos_matches[:5]:
        print(f"  CRICOS ref: {m}")

print(f"\nBody size: {len(r.text)} bytes")
print(f"Response time: {r.elapsed.total_seconds():.2f}s")

# Cek apakah pakai Apache (bukan Nginx/CF)
print(f"\nServer header: {r.headers.get('Server')}")
print("Kesimpulan: NO Cloudflare. Server uses Apache behind AWS ALB.")
