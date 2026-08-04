"""Check exact fee display on Adelaide Uni course page."""
import requests, re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
r = requests.get('https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/', headers=headers, timeout=60)
html = r.text

# Find the exact fee section - look for the component text
print("=== FEE SECTION - RAW HTML AROUND '54,900' ===")
for m in re.finditer(r'\$54,900', html):
    start = max(0, m.start() - 500)
    end = min(len(html), m.end() + 500)
    snippet = html[start:end]
    # Strip tags for readability
    clean = re.sub(r'<[^>]+>', ' ', snippet)
    clean = re.sub(r'\s+', ' ', clean)
    print(clean)
    print("---")

print()
print("=== ALL DOLLAR AMOUNTS IN CONTEXT ===")
text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', '\n', text)
text = re.sub(r'\n\s*\n', '\n', text)

for line in text.split('\n'):
    line = line.strip()
    if '$' in line and line:
        print(f"  {line[:200]}")
