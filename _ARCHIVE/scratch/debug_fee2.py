"""Find ALL degree-details-content-section-subtitle elements."""
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
r = requests.get('https://adelaide.edu.au/study/degrees/bachelor-of-software-engineering-honours/', headers=headers, timeout=60)
soup = BeautifulSoup(r.text, 'html.parser')

for i, el in enumerate(soup.select('.degree-details-content-section-subtitle')):
    print(f"\n[{i}] Parent classes: {el.parent.get('class', [])}")
    print(f"    HTML: {str(el)[:200]}")
    
    # Check if this is in the fee section
    for parent in el.parents:
        if parent.get('class') and ('fee' in ' '.join(parent.get('class', [])).lower() or 'icon' in ' '.join(parent.get('class', [])).lower()):
            print(f"    PARENT with class: {parent.get('class')}")
        if parent.name == 'main':
            break

# More targeted: find element near "Indicative annual fees"
print("\n\n=== Find by 'Indicative annual fees' label ===")
for span in soup.find_all('span'):
    if 'Indicative annual fees' in span.get_text():
        print(f"Found label: {span}")
        # Get next sibling or parent's next
        parent = span.find_parent(['div'])
        if parent:
            grandparent = parent.parent if parent.parent else parent
            print(f"Parent: {parent.get('class', [])}")
            print(f"Grandparent: {grandparent.get('class', [])}")
            # Find fee amount nearby
            subtitle = grandparent.select_one('.degree-details-content-section-subtitle')
            if subtitle:
                print(f"Fee amount: '{subtitle.get_text(strip=True)}'")
            else:
                print(f"Full HTML: {str(grandparent)[:500]}")
        break
