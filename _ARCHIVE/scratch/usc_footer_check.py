"""
USC Website Footer Check
Extracts CRICOS code from footer
"""
import requests
import re

URL = "https://www.unisc.edu.au/"

def main():
    print(f"[+] Fetching: {URL}")
    r = requests.get(URL, timeout=30)
    html = r.text
    
    # Find footer content
    footer_section = re.search(r'<footer[^>]*>(.*?)</footer>', html, re.DOTALL | re.I)
    
    print(f"\n{'='*60}")
    print("FOOTER ANALYSIS")
    print(f"{'='*60}")
    
    if footer_section:
        footer = footer_section.group(1)
        print("Footer found ✓")
        
        # CRICOS
        cricos = re.findall(r'CRICOS[^<]*?([0-9A-Z]+)', footer, re.I)
        print(f"CRICOS: {cricos}")
        
        # TEQSA
        teqsa = re.findall(r'TEQSA[^<]*?([0-9A-Z]+)', footer, re.I)
        print(f"TEQSA: {teqsa}")
        
        # Other footer info
        other_info = re.findall(r'(?:ABN|Provider|RTO|National)[^<]{0,100}', footer, re.I)
        for o in other_info:
            print(f"  {o.strip()}")
    else:
        print("No <footer> tag found with regex - searching full page...")
        cricos = re.findall(r'CRICOS[^<]*?([0-9A-Z]+)', html, re.I)
        print(f"CRICOS in page: {cricos}")
    
    # Also display the footer text
    print(f"\nRaw footer text snippet:")
    if footer_section:
        # Clean tags
        text = re.sub(r'<[^>]+>', ' ', footer)
        text = re.sub(r'\s+', ' ', text).strip()
        print(text[:500])
    else:
        text = re.sub(r'<[^>]+>', ' ', html[-2000:])
        text = re.sub(r'\s+', ' ', text).strip()
        print(text[:500])

if __name__ == '__main__':
    main()
