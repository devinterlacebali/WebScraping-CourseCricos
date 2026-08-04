"""Dig deeper into Adelaide Uni course page: fee structure."""
import requests, re, json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
base = 'https://adelaideuni.edu.au/study/degrees/bachelor-of-laws-honours'
r = requests.get(base + '/', headers=headers, timeout=60)
html = r.text

# Find all data-cmp-data-layer attributes
datalayers = re.findall(r"data-cmp-data-layer='([^']+)'", html)
print("Data layer components:", len(datalayers))

all_txt = ''
for dl in datalayers:
    try:
        # decode HTML entities
        d = dl.replace('&#34;', '"').replace('&quot;', '"').replace('&#39;', "'")
        obj = json.loads(d)
        txt = obj.get('xdm:text', '')
        if txt:
            all_txt += txt + '\n'
    except:
        pass

clean = re.sub(r'<[^>]+>', ' ', all_txt)
clean = re.sub(r'\s+', ' ', clean)
print("=== ALL COMPONENT TEXT ===")
print(clean[:2000])

print("\n=== FEE SPECIFIC ===")
# Extract fee-adjacent text
for m in re.finditer(r'\$[0-9,]+', clean):
    start = max(0, m.start()-100)
    end = min(len(clean), m.end()+100)
    ctx = clean[start:end]
    print(f"  {ctx.strip()}")
    print()
