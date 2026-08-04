"""Find Acknowledge Education fee data - check JS data."""
import requests, re, json
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = 'https://www.acknowledgeeducation.edu.au/courses/diploma-of-nursing-draft'
r = requests.get(url, headers=headers, timeout=60)
html = r.text

# Find all __NEXT_DATA__ or JSON-LD
print("=== __NEXT_DATA__ ===")
m = re.search(r'__NEXT_DATA__\s*=\s*(\{.*?\});', html, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    print(json.dumps(data, indent=2)[:3000])
else:
    print("Not found")

print("\n=== JSON-LD scripts ===")
for script in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL):
    try:
        data = json.loads(script.group(1))
        print(json.dumps(data, indent=2)[:500])
    except:
        pass

print("\n=== Data attributes with fee ===")
# Search for any data-* with fee info
for m in re.finditer(r'data-[^=]+=[\"\']([^\"\']+)[\"\']', html):
    val = m.group(1)
    if any(kw in val.lower() for kw in ['fee', '$', 'tuition']):
        print(f"  {m.group(0)[:100]}")
