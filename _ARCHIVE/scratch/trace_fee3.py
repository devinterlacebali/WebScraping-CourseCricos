"""Find exact path to fee $54,900."""
import requests, re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
r = requests.get('https://adelaide.edu.au/study/degrees/bachelor-of-laws-honours/', headers=headers, timeout=60)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

# Find the span with $54,900
for span in soup.find_all('span'):
    text = span.get_text(strip=True)
    if '$54,900' in text:
        print("=== PATH TO FEE SPAN ===")
        # Print parent chain with classes/ids
        for level, parent in enumerate(span.parents):
            classes = ' '.join(parent.get('class', [])) if parent.get('class') else ''
            pid = parent.get('id', '')
            tag = parent.name
            extra = f"class='{classes}'" if classes else ""
            extra += f" id='{pid}'" if pid else ""
            print(f"  [{level}] <{tag} {extra}>".strip())
            
            # If it has a specific class we can target
            if parent.get('class'):
                print(f"      -> selector: {'.'.join(parent.get('class'))}")
        
        # Print the HTML of the direct parent div
        parent = span.parent
        print(f"\n=== Direct parent HTML ===")
        print(str(parent)[:500])
        
        # Print grandparent
        gp = parent.parent
        print(f"\n=== Grandparent HTML ===")
        print(str(gp)[:500])
        break
