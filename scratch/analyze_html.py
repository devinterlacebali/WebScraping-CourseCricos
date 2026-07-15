from bs4 import BeautifulSoup
import re

def main():
    with open("scratch/latrobe_course.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    print("HTML Length:", len(html))
    
    # 1. Look for CRICOS code patterns
    cricos_matches = soup.find_all(string=re.compile(r"CRICOS", re.IGNORECASE))
    print(f"\nFound {len(cricos_matches)} elements containing 'CRICOS':")
    for m in cricos_matches[:10]:
        parent = m.parent
        print(f"Parent tag: <{parent.name}> with text: {parent.get_text(strip=True)[:150]}")
        # print parent of parent
        if parent.parent:
            print(f"  Parent's parent: <{parent.parent.name}> classes: {parent.parent.get_class() if hasattr(parent.parent, 'get_class') else parent.parent.get('class')}")
            
    # 2. Look for duration
    dur_matches = soup.find_all(string=re.compile(r"duration|year", re.IGNORECASE))
    print(f"\nFound {len(dur_matches)} elements containing 'duration' or 'year':")
    for m in dur_matches[:10]:
        parent = m.parent
        print(f"Parent tag: <{parent.name}> with text: {parent.get_text(strip=True)[:150]}")

    # 3. Look for tuition fee
    fee_matches = soup.find_all(string=re.compile(r"fee|estimate|\$", re.IGNORECASE))
    print(f"\nFound {len(fee_matches)} elements containing 'fee', 'estimate', or '$':")
    for m in fee_matches[:10]:
        parent = m.parent
        print(f"Parent tag: <{parent.name}> with text: {parent.get_text(strip=True)[:150]}")

    # 4. Let's see some structure: print all section, article, or div tags with class names
    print("\n--- Divisions and Sections ---")
    for tag in soup.find_all(["section", "article"]):
        print(f"Tag: <{tag.name}> ID: {tag.get('id')} Class: {tag.get('class')} Text snippet: {tag.get_text(' ', strip=True)[:100]}")

if __name__ == "__main__":
    main()
