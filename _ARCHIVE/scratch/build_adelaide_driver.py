"""Build Adelaide Uni driver xlsx from sitemap (using openpyxl, no pandas)."""
import requests, re, os
from openpyxl import Workbook

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
DIR = r'C:\Users\Dewa(Interlace)\Documents\Interlace Code\WebScraping-CourseCricos\The University Of Adelaide'
EXCEL_PATH = os.path.join(DIR, 'adelaide.xlsx')

print("Fetching sitemap...")
r = requests.get('https://adelaideuni.edu.au/sitemap.xml', headers=headers, timeout=120)
urls = re.findall(r'<loc>(https://adelaide\.edu\.au/study/degrees/[^<]+)</loc>', r.text)
degree_urls = sorted(set(u for u in urls if '/online/' not in u))
print(f"Total degree URLs: {len(degree_urls)}")

wb = Workbook()
ws = wb.active
ws.title = "Courses"
ws.append(['cricos', 'title', 'url'])

for i, url in enumerate(degree_urls, 1):
    try:
        r2 = requests.get(url, headers=headers, timeout=60)
        html = r2.text
        title_m = re.search(r'<title>(.*?)</title>', html)
        title = title_m.group(1) if title_m else ''
        title = re.sub(r'\s*[|]\s*Adelaide University.*$', '', title)
        title = re.sub(r'^Study\s+', '', title).strip()
        cricos_m = re.search(r'cricosCode"\s+content="([^"]+)"', html)
        cricos = cricos_m.group(1) if cricos_m else ''
        ws.append([cricos, title, url])
        if i % 100 == 0:
            print(f"  {i}/{len(degree_urls)}...")
    except Exception as e:
        ws.append(['', '', url])
        print(f"  FAIL #{i}: {url[:80]}: {e}")

wb.save(EXCEL_PATH)
print(f"\n✅ Saved {len(degree_urls)} rows to {EXCEL_PATH}")

# Count how many have CRICOS
with_cricos = sum(1 for row in ws.iter_rows(min_row=2, values_only=True) if row[0])
print(f"   With CRICOS: {with_cricos}")
print(f"   Without: {len(degree_urls) - with_cricos}")
