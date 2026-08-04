"""Find fee info on Adelaide Uni page - try raw text extraction."""
import requests, re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
r = requests.get('https://adelaideuni.edu.au/study/degrees/bachelor-of-laws-honours/', headers=headers, timeout=60)
html = r.text

# Save the raw HTML for analysis
with open(r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\scratch\adelaide_sample.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved HTML to scratch/adelaide_sample.html")
print(f"Size: {len(html)} bytes")

# Extract just body text
text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', '\n', text)
text = re.sub(r'\n\s*\n', '\n', text)
text = re.sub(r'[ \t]+', ' ', text)

# Print relevant sections
lines = text.split('\n')
print("\n=== RELEVANT LINES ===")
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    if any(kw in line.lower() for kw in ['fee', '$', 'intake', 'start', 'duration', 'cricos', 'year', 'month', 'entry', 'requirement', 'admission', 'ielts']):
        print(f"{i}: {line[:200]}")
