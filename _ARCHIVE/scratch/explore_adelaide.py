"""Explore Adelaide Uni website structure for scraper builder."""
import requests, re, json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
url = 'https://adelaideuni.edu.au/study/degrees/bachelor-of-laws-honours/'
r = requests.get(url, headers=headers, timeout=60)
html = r.text

print(f"Status: {r.status_code}, Length: {len(html)} bytes\n")

# --- Meta properties ---
metas = re.findall(r'<meta\s+property="([^"]+)"\s+content="([^"]*)"', html)
print("=== META PROPERTIES ===")
for p, v in metas:
    print(f"  {p}: {v}")

# CRICOS from meta
cricos_m = re.search(r'cricosCode" content="([^"]+)"', html)
print(f"\nCRICOS from meta: {cricos_m.group(1) if cricos_m else 'NOT FOUND'}")

# --- Dollar amounts ---
print("\n=== DOLLAR AMOUNTS (fee context) ===")
# Find dollar amounts
for m in re.finditer(r'\$[0-9,]+', html):
    start = max(0, m.start() - 200)
    end = min(len(html), m.end() + 200)
    ctx = html[start:end]
    clean = re.sub(r'<[^>]+>', ' ', ctx).strip()
    clean = re.sub(r'\s+', ' ', clean)
    if any(w in clean.lower() for w in ['fee', 'international', 'domestic', 'tuition', 'cost', 'total', 'per year', 'annual']):
        print(f"  ...{clean[:250]}...")
        print()

# --- Duration from meta ---
dur_m = re.search(r'timeRequired" content="([^"]+)"', html)
print(f"Duration from meta: {dur_m.group(1) if dur_m else 'NOT FOUND'}")

# --- Intake months from meta ---
start_m = re.search(r'startMonth" content="([^"]+)"', html)
print(f"Start months: {start_m.group(1) if start_m else 'NOT FOUND'}")

# --- Description from meta ---
desc_m = re.search(r'og:description" content="([^"]*)"', html)
print(f"Description: {desc_m.group(1)[:200] if desc_m else 'NOT FOUND'}...")
