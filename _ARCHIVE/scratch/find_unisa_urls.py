import asyncio
import aiohttp
import re
import pandas as pd
from bs4 import BeautifulSoup
import os

# === PATHS ===
EXCEL_INPUT = "The University Of Adelaide/Book1.xlsx"
CRICOS_CSV = "cricos-courses.csv"
OUTPUT_DIR = "University of South Australia (UniSA)"
OUTPUT_EXCEL = os.path.join(OUTPUT_DIR, "unisa.xlsx")

# Regex to find CRICOS codes (e.g. 115756M or 000537M)
CRICOS_RE = re.compile(r"\b(\d{5,6}[A-Za-z]|\d{7})\b")

async def fetch_cricos_code(session, base_url):
    int_url = base_url.rstrip("/") + "/int/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    try:
        async with session.get(int_url, headers=headers, timeout=20) as r:
            if r.status != 200:
                # Try domestic as fallback
                dom_url = base_url.rstrip("/") + "/dom/"
                async with session.get(dom_url, headers=headers, timeout=20) as r2:
                    if r2.status != 200:
                        return base_url, None, f"HTTP Status {r.status}/{r2.status}"
                    html = await r2.text()
            else:
                html = await r.text()
            
            # 1. Look for meta cricosCode
            m = re.search(r'<meta[^>]*property="cricosCode"[^>]*content="([^"]+)"', html)
            if m:
                return base_url, m.group(1).strip(), None
            
            m = re.search(r'<meta[^>]*name="cricosCode"[^>]*content="([^"]+)"', html)
            if m:
                return base_url, m.group(1).strip(), None

            # 2. Look for cricos in soup
            soup = BeautifulSoup(html, "html.parser")
            label = soup.find("span", string=re.compile(r"^\s*CRICOS code\s*$", re.I))
            if label:
                container = label.find_parent(class_=re.compile(r"degree-details-content-section-icon-list-top"))
                if container:
                    val = container.select_one(".degree-details-content-section-subtitle span")
                    if val:
                        return base_url, val.get_text(strip=True), None

            # 3. Look for general CRICOS pattern
            matches = CRICOS_RE.findall(html)
            if matches:
                # Exclude provider code 04249J
                valid_codes = [c for c in matches if c != "04249J" and c != "00121B" and c != "00123M"]
                if valid_codes:
                    return base_url, valid_codes[0], None

            return base_url, None, "CRICOS code not found in HTML"
    except Exception as e:
        return base_url, None, str(e)

async def main():
    print("Loading CRICOS database...")
    cricos_df = pd.read_csv(CRICOS_CSV, dtype=str)
    
    # Get set of all UniSA and Adelaide Uni CRICOS codes from CSV
    unisa_cricos = set(cricos_df[cricos_df["CRICOS Provider Code"] == "00121B"]["CRICOS Course Code"].dropna().tolist())
    adelaide_cricos = set(cricos_df[cricos_df["CRICOS Provider Code"] == "04249J"]["CRICOS Course Code"].dropna().tolist())
    
    # We combine them since UniSA courses may have transitioned to 04249J under Adelaide Uni
    target_cricos_set = unisa_cricos.union(adelaide_cricos)
    print(f"Total target CRICOS course codes: {len(target_cricos_set)} (UniSA: {len(unisa_cricos)}, Adelaide Uni: {len(adelaide_cricos)})")

    print(f"Reading links from {EXCEL_INPUT}...")
    df_links = pd.read_excel(EXCEL_INPUT)
    urls = df_links.iloc[:, 0].dropna().tolist()
    print(f"Loaded {len(urls)} URLs to scan.")

    # Fetch concurrently
    conn = aiohttp.TCPConnector(limit=25)  # limit concurrency to not overwhelm server
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = [fetch_cricos_code(session, url) for url in urls]
        print("Scanning pages concurrently...")
        results = await asyncio.gather(*tasks)

    # Process results
    matched_rows = []
    skipped_count = 0
    not_found_count = 0

    for url, cricos, err in results:
        if err:
            # print(f"Error {url}: {err}")
            not_found_count += 1
            continue
        if not cricos:
            not_found_count += 1
            continue
        
        # Check if the CRICOS code belongs to UniSA or Adelaide University
        if cricos in target_cricos_set:
            # Get course name from cricos-courses.csv
            row_cricos = cricos_df[cricos_df["CRICOS Course Code"] == cricos]
            course_name = row_cricos.iloc[0]["Course Name"] if not row_cricos.empty else ""
            provider = row_cricos.iloc[0]["Institution Name"] if not row_cricos.empty else "Adelaide University"
            matched_rows.append({
                "url": url,
                "cricos_course_code": cricos,
                "course_name": course_name,
                "institution": provider
            })
        else:
            skipped_count += 1

    # Save to Excel
    if matched_rows:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        df_out = pd.DataFrame(matched_rows)
        df_out.to_excel(OUTPUT_EXCEL, index=False)
        print(f"Finished scanning!")
        print(f"   - Total matched UniSA / Adelaide Uni courses: {len(matched_rows)}")
        print(f"   - Skipped other provider courses: {skipped_count}")
        print(f"   - Errors/Not found: {not_found_count}")
        print(f"Saved to {OUTPUT_EXCEL}")
    else:
        print("No matching courses found!")

if __name__ == "__main__":
    asyncio.run(main())
