from bs4 import BeautifulSoup
import re

def main():
    with open("scratch/latrobe_course.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    
    # Let's search for select elements
    selects = soup.find_all("select")
    print("Found selects:", len(selects))
    for s in selects:
        print("Select ID:", s.get("id"), "Class:", s.get("class"))
        for opt in s.find_all("option"):
            print("  Option:", opt.get("value"), "Text:", opt.get_text(strip=True))
            
    # Search for button elements with data attributes
    buttons = soup.find_all("button")
    print("\nSome buttons with classes or text:")
    for b in buttons:
        cls = str(b.get("class"))
        text = b.get_text(strip=True)
        if "location" in cls.lower() or "year" in cls.lower() or "campus" in cls.lower() or any(c in text.lower() for c in ["melbourne", "online", "sydney", "bendigo"]):
            print(f"  Button: text='{text}', class='{cls}', attrs={b.attrs}")
            
    # Let's search for specific wrapper classes like ds-accordion or customiser
    customiser = soup.find(id="customiser")
    if customiser:
        print("\nStructure inside #customiser:")
        print(customiser.get_text("\n", strip=True))
    else:
        print("No #customiser found")

if __name__ == "__main__":
    main()
