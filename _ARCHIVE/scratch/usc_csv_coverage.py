"""
USC CSV Coverage Analysis
Checks cricos-courses.csv for USC courses
"""
import csv
import requests
import re

CSV_PATH = "cricos-courses.csv"
PROVIDER_CODE = "01595D"

def main():
    print(f"[+] Reading CSV: {CSV_PATH}")
    
    rows = []
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    
    print(f"    Total rows: {len(rows):,}")
    
    # Filter for USC
    usc_rows = [r for r in rows if r.get('CRICOS Provider Code') == PROVIDER_CODE]
    print(f"    USC rows (provider {PROVIDER_CODE}): {len(usc_rows)}")
    
    # Also match by name
    name_matches = [r for r in rows if 'sunshine' in r.get('Institution Name', '').lower() or 'usc' in r.get('Institution Name', '').lower()]
    print(f"    By name 'Sunshine Coast': {len(name_matches)}")
    if name_matches:
        print(f"    Institution names: {set(r['Institution Name'] for r in name_matches)}")
    
    if not usc_rows:
        print("WARNING: No USC rows found by provider code!")
        return
    
    # Course level breakdown
    from collections import Counter
    levels = Counter(r.get('Course Level', 'Unknown') for r in usc_rows)
    print(f"\n    Course level breakdown:")
    for level, count in sorted(levels.items(), key=lambda x: -x[1]):
        print(f"      {level}: {count}")
    
    # Status breakdown
    expired = sum(1 for r in usc_rows if r.get('Expired', '').strip().upper() == 'YES')
    not_expired = sum(1 for r in usc_rows if r.get('Expired', '').strip().upper() != 'YES')
    print(f"\n    Active: {not_expired}, Expired: {expired}")
    
    # Sample courses
    print(f"\n    Sample active courses:")
    active = [r for r in usc_rows if r.get('Expired', '').strip().upper() != 'YES']
    for r in active[:10]:
        print(f"      {r['CRICOS Course Code']} | {r['Course Name'][:60]} | ${r.get('Estimated Total Course Cost', 'N/A')} | {r.get('Duration (Weeks)', 'N/A')}wks")
    
    # Compare with sitemap
    print(f"\n{'='*60}")
    print(f"Checking sitemap for course coverage")
    print(f"{'='*60}")
    
    try:
        r = requests.get('https://www.unisc.edu.au/XMLsitemap', timeout=60)
        sitemap_courses = re.findall(r'(https://www\.unisc\.edu\.au/study/courses-and-programs/[^<]+)', r.text)
        print(f"    Sitemap course URLs: {len(sitemap_courses):,}")
        print(f"    CSV courses: {len(usc_rows)}")
        print(f"    Note: CSV has CRICOS courses only; sitemap has all programs incl. non-CRICOS")
    except Exception as e:
        print(f"    Error fetching sitemap: {e}")

if __name__ == '__main__':
    main()
