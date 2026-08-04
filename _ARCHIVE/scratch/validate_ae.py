"""Validate Acknowledge Education scraper output by re-fetching key pages."""
import sys
sys.path = [p for p in sys.path if 'hermes' not in p.lower()]
import requests, re
from bs4 import BeautifulSoup

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

import pandas as pd
df = pd.read_excel('Acknowledge Education/acknowledgeeducation.xlsx')

print(f"{'CRICOS':<10} {'Fee':<8} {'Dur':<6} {'Status':<24} {'Title':<50}")
print("="*100)

errors = []
for _, row in df.iterrows():
    cricos = str(row.get('cricos', '')).strip() if row.get('cricos') else ''
    fee = str(row.get('offshore_tuition_fee', ''))
    dur = str(row.get('course_duration_per_week', ''))
    title = str(row.get('title', ''))[:50]
    url = str(row.get('url', ''))
    intake = str(row.get('intake', ''))
    
    if not cricos or cricos.lower() in ('nan', 'none', ''):
        print(f"{'—':<10} {'—':<8} {'—':<6} ⏭️  SKIP (no CRICOS)   {title}")
        continue
    
    try:
        r = requests.get(url, headers=H, timeout=30)
        soup = BeautifulSoup(r.text, 'html.parser')
        body = re.sub(r'\s+', ' ', soup.get_text())
        
        # 1. CRICOS verification
        a = soup.find("a", href=re.compile(r"cricos\.education\.gov\.au", re.I))
        page_cricos = ""
        if a:
            m = re.match(r'^(\d{6,7}[A-Za-z]?)$', a.get_text(strip=True))
            if m:
                page_cricos = m.group(1)
        
        # 2. Fee verification (accordion-based)
        page_fee = ""
        bodies = soup.find_all("div", class_="accordion-body")
        for b in bodies:
            t = b.get_text(strip=True)
            if "international" in t.lower() and ("tuition" in t.lower() or "fee" in t.lower()):
                per_unit = re.findall(r'\$([0-9,]+)\s*per\s*unit', t, re.I)
                unit_counts = re.findall(r'x\s*(\d+)\s*units?', t, re.I)
                if per_unit and unit_counts and len(per_unit) == len(unit_counts):
                    total = 0
                    for p, u in zip(per_unit, unit_counts):
                        total += int(p.replace(',', '')) * int(u)
                    page_fee = str(total)
                else:
                    dm = re.search(r'\$([0-9,]{3,})', t)
                    if dm:
                        page_fee = str(int(dm.group(1).replace(',', '')))
                break
        
        # 3. Duration verification
        page_dur = ""
        label = soup.find("div", class_="course-summary-item__label", string=re.compile("Duration", re.I))
        if label:
            value = label.find_next("div", class_="col-12")
            if value:
                raw = value.text.strip()
                m = re.search(r"(\d+\.?\d*)\s*(year|month|week)", raw, re.I)
                if m:
                    num = float(m.group(1))
                    unit = m.group(2).lower()
                    if "year" in unit:
                        page_dur = str(int(round(num * 52)))
                    elif "month" in unit:
                        page_dur = str(int(round(num * 4.33)))
                    else:
                        page_dur = str(int(num))
        
        # 4. Intake verification
        page_months = set()
        for tok in re.findall(r"[A-Za-z]{3,9}", body):
            k = tok.lower()
            lookup = {"jan":"January","feb":"February","mar":"March","apr":"April",
                      "may":"May","jun":"June","jul":"July","aug":"August",
                      "sep":"September","oct":"October","nov":"November","dec":"December",
                      "january":"January","february":"February","march":"March","april":"April",
                      "june":"June","july":"July","august":"August","september":"September",
                      "october":"October","november":"November","december":"December"}
            if k in lookup:
                page_months.add(lookup[k])
        
        # Status building
        status = ""
        if page_cricos == cricos:
            status += "✅CRICOS "
        elif page_cricos:
            status += f"❌CRICOS(page={page_cricos}) "
        else:
            status += "⚠️CRICOS(no-page-ref) "
        
        xlsx_fee_clean = fee.replace('.0', '') if fee not in ('nan', '', 'NULL', 'None') else ''
        if not xlsx_fee_clean and not page_fee:
            status += "⬜no-fee "
        elif xlsx_fee_clean == page_fee:
            status += "✅FEE "
        elif page_fee and not xlsx_fee_clean:
            status += f"❌FEE(missing-in-xlsx, page=${page_fee}) "
        elif xlsx_fee_clean and not page_fee:
            status += f"❌FEE(in-xlsx-but-not-on-page) "
        else:
            status += f"❌FEE(xlsx=${xlsx_fee_clean}, page=${page_fee}) "
        
        if dur and page_dur:
            if dur.replace('.0','') == page_dur:
                status += "✅DUR "
            else:
                status += f"❌DUR(xlsx={dur},page={page_dur}) "
        elif dur and not page_dur:
            status += f"❌DUR(in-xlsx-not-on-page) "
        elif not dur and page_dur:
            status += f"❌DUR(missing,page={page_dur}) "
        else:
            status += "⬜no-dur "
        
        # Collect errors for summary
        if "❌" in status:
            errors.append((cricos, title, status))
        
        print(f"{cricos:<10} {str(fee)[:8]:<8} {str(dur)[:6]:<6} {status:<24} {title}")
        
    except Exception as e:
        print(f"{cricos:<10} {str(fee)[:8]:<8} {str(dur)[:6]:<6} ❌FETCH: {str(e)[:40]:<24} {title}")
        errors.append((cricos, title, f"FETCH ERROR: {e}"))

print(f"\n{'='*100}")
print(f"\n✅ Validated {len(df)} rows")
cricos_ok = sum(1 for _, r in df.iterrows() if r.get('cricos') and str(r['cricos']).strip().lower() not in ('nan','','none'))
print(f"   CRICOS present: {cricos_ok}")
print(f"   Errors found: {len(errors)}")

if errors:
    print(f"\n❌ DETAILED ERRORS:")
    for c, t, s in errors:
        print(f"   {c:<10} {t:<50} {s}")
