from bs4 import BeautifulSoup
import re
import json

def main():
    with open("scratch/latrobe_course.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    print("Page Title:", soup.find("title").get_text(strip=True) if soup.find("title") else "No Title")
    
    # 1. Search for CRICOS code pattern in the whole text
    # Standard CRICOS code is 6 digits + 1 letter, or 7 digits (sometimes 6 digits + 1 letter or 7 digits + 1 letter).
    # e.g., 002080A, 0100796, 025405F
    cricos_patterns = re.findall(r"\b\d{5,7}[A-Za-z]\b", html)
    print("CRICOS code pattern matches in raw HTML:", set(cricos_patterns))
    
    # 2. Print all script tags containing JSON or having specific IDs
    print("\n--- Script Tags of Interest ---")
    scripts = soup.find_all("script")
    print(f"Total script tags: {len(scripts)}")
    for idx, s in enumerate(scripts):
        src = s.get("src")
        s_type = s.get("type")
        s_id = s.get("id")
        if s_id or (s_type and "json" in s_type) or (src and "course" in src):
            print(f"[{idx}] src: {src}, type: {s_type}, id: {s_id}")
            if s.string:
                print(f"    Content snippet: {s.string[:200]}")
                
    # 3. Look for meta tags
    print("\n--- Meta Tags ---")
    for meta in soup.find_all("meta"):
        name = meta.get("name")
        prop = meta.get("property")
        content = meta.get("content")
        if name or prop:
            print(f"name: {name}, property: {prop}, content: {content}")

    # 4. Search for the word "business" to see if course-specific content is in the HTML
    text = soup.get_text(" ", strip=True)
    business_count = text.lower().count("business")
    print(f"\nOccurrences of 'business' in visible text: {business_count}")
    
    # Print the first 2000 characters of the body text
    body = soup.find("body")
    if body:
        print("\n--- Body Text (First 1500 chars) ---")
        print(body.get_text("\n", strip=True)[:1500])

if __name__ == "__main__":
    main()
