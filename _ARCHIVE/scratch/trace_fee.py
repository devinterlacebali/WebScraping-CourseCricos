"""Find where $54,900 lives in the HTML."""
import requests, re
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
r = requests.get('https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/', headers=headers, timeout=60)
html = r.text

# Search for 54900 in every possible form
patterns = ['54,900', '54900', '54.900']
for pat in patterns:
    positions = [m.start() for m in re.finditer(re.escape(pat), html)]
    print(f"'{pat}' found at {len(positions)} positions")
    for pos in positions[:3]:
        ctx = html[max(0,pos-200):pos+200]
        clean = re.sub(r'\s+', ' ', ctx)
        print(f"  ...{clean[:300]}...")
        print()

# Also check for the expected JSON structure
print("\n=== Looking for 'Indicative annual fees' in raw HTML ===")
for m in re.finditer(r'Indicative\s+annual\s+fee[s]?', html):
    ctx = html[max(0,m.start()-300):m.end()+500]
    clean = re.sub(r'\s+', ' ', ctx)
    print(f"  {clean[:400]}")
    print()
