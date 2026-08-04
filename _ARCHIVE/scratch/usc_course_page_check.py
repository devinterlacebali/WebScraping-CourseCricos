"""
USC Course Page Structure Analysis
Checks if SSR, extracts CRICOS, fees, duration, intake
"""
import requests
import re
import json

BACHELOR_CS = "https://www.unisc.edu.au/study/courses-and-programs/bachelor-degrees-undergraduate-programs/bachelor-of-computer-science"
MASTER_DS = "https://www.unisc.edu.au/study/courses-and-programs/graduate-degrees-postgraduate-programs/master-of-data-science"
NURSING = "https://www.unisc.edu.au/study/courses-and-programs/bachelor-degrees-undergraduate-programs/bachelor-of-nursing-science"

def analyze_course_page(url, label):
    print(f"\n{'='*70}")
    print(f"[{label}] {url}")
    print(f"{'='*70}")
    
    r = requests.get(url, timeout=30)
    html = r.text
    
    # SSR check
    is_ssr = len(html) > 10000 and '<!DOCTYPE' in html[:500] and ('class=' in html or 'id=' in html)
    print(f"  SSR: {'YES' if is_ssr else 'NO'} (content length: {len(html):,} chars)")
    print(f"  JS-dependent areas: {'<script' in html and 'dynamic' in html}")
    
    # CRICOS
    cricos_matches = re.findall(r'CRICOS[^<]*?([0-9A-Z]{5,8})', html, re.I)
    print(f"  CRICOS codes: {cricos_matches if cricos_matches else 'NOT FOUND'}")
    
    # Provider code
    provider = re.search(r'(?:Provider|CRICOS)[^<]*?((?:01[0-9]{3}[A-Z]))', html, re.I)
    if provider:
        print(f"  Provider code: {provider.group(1)}")
    
    # Fees
    fee_patterns = re.findall(r'\$[\d,]+(?:\.\d{2})?[^<]{0,100}(?:fee|tuition|cost|per year|total|per annum)', html, re.I)
    print(f"  Fee mentions:")
    for f in fee_patterns[:5]:
        print(f"    - {f.strip()[:120]}")
    
    # Duration
    dur_patterns = re.findall(r'(\d+)[- ]?(?:year|semester|trimester|month)[^<]{0,60}(?:program|course|full.time|duration|degree)', html, re.I)
    print(f"  Duration mentions:")
    for d in dur_patterns[:5]:
        print(f"    - {d.strip()[:120]}")
    
    # Intake
    intake = re.findall(r'(?:Intake|Commence(?:ment)?|Start date|Session|Semester|Trimester)\s*[^<]{0,60}', html)
    print(f"  Intake/start mentions ({len(intake)}):")
    for i in intake[:8]:
        print(f"    - {i.strip()[:100]}")
    
    # JSON-LD structured data
    jsonld_blocks = re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', html, re.DOTALL)
    if jsonld_blocks:
        print(f"  JSON-LD blocks: {len(jsonld_blocks)}")
        for i, j in enumerate(jsonld_blocks[:2]):
            try:
                data = json.loads(j)
                print(f"    Block {i+1}: {json.dumps(data, indent=2)[:500]}")
            except:
                print(f"    Block {i+1}: [invalid JSON] {j[:200]}")
    else:
        print(f"  JSON-LD: None found")
    
    return html

if __name__ == '__main__':
    analyze_course_page(BACHELOR_CS, "BACHELOR OF COMPUTER SCIENCE")
    analyze_course_page(MASTER_DS, "MASTER OF DATA SCIENCE")
    analyze_course_page(NURSING, "BACHELOR OF NURSING SCIENCE")
