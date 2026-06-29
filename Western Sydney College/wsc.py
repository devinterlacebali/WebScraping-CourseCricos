import os
import re
import sys
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Force UTF-8 encoding for stdout and stderr on Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# === CLEAN HTML ===
def clean_html(html: str) -> str:
    if not html:
        return ""
    # Replace multiple whitespaces with single space
    html = re.sub(r"\s+", " ", html)
    # Escape single quotes for SQL insertion
    html = html.replace("'", "''")
    return html.strip()

# === DYNAMIC TAB EXTRACTOR ===
def extract_tab_content(soup, keyword: str, fallback_id: str) -> str:
    nav_tabs = soup.find(class_="nav-tabs-main")
    target_id = None
    if nav_tabs:
        for a in nav_tabs.find_all("a", href=True):
            text = a.get_text(" ", strip=True)
            if keyword.lower() in text.lower():
                target_id = a["href"].strip().lstrip("#")
                break
                
    if not target_id:
        target_id = fallback_id
        
    pane = soup.find(id=target_id)
    if pane:
        # Clone pane to avoid modifying original soup
        pane_clone = BeautifulSoup(str(pane), "html.parser")
        
        # Decompose scripts and styles
        for tag in pane_clone.find_all(["style", "script", "noscript"]):
            tag.decompose()
            
        # Extract the details-description container if present, otherwise use the pane itself
        desc_div = pane_clone.find(class_="details-description")
        target_el = desc_div if desc_div else pane_clone
        
        return clean_html(str(target_el))
    return ""

# === SCRAPE PER COURSE ===
async def scrape_course(row, browser):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    duration = str(row["duration"]).strip()
    fee = str(row["fee"]).strip()
    
    data = {
        "cricos": cricos,
        "title": str(row["title"]).strip(),
        "url": url,
        "course_description": "",
        "total_course_duration": duration,
        "offshore_tuition_fee": fee,
        "entry_requirements": "",
        "apply_form": url,
    }
    
    try:
        page = await browser.new_page()
        # Use domcontentloaded wait for speed and reliability
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        # 1. Course Description (Overview)
        desc_html = extract_tab_content(soup, "overview", "course-overview")
        data["course_description"] = desc_html
        
        # 2. Entry Requirements
        entry_html = extract_tab_content(soup, "entry", "details-100")
        data["entry_requirements"] = entry_html
        
        await page.close()
        print(f"✅ Scraped successfully: {url}")
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        try:
            await page.close()
        except:
            pass
            
    return data

# === MAIN ===
async def main():
    excel_path = "Western Sydney College/wsc.xlsx"
    sql_path = "Western Sydney College/wsc_courses_update.sql"
    
    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return
        
    df = pd.read_excel(excel_path)
    results = []
    
    async with async_playwright() as p:
        headless_env = os.environ.get("SCRAPER_HEADLESS", "True")
        headless_val = True if headless_env.lower() in ("true", "1") else False
        
        browser = await p.chromium.launch(headless=headless_val)
        
        for idx, row in df.iterrows():
            print(f"\n[{idx+1}/{len(df)}] Scraping: {row['url']}")
            course_data = await scrape_course(row, browser)
            results.append(course_data)
            
        await browser.close()
        
    # Write SQL updates
    with open(sql_path, "w", encoding="utf-8") as f:
        for d in results:
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
    offshore_tuition_fee = '{d["offshore_tuition_fee"]}',
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
            
    print(f"\n✅ Finished! Scraped {len(results)} courses. SQL updates saved to {sql_path}")

if __name__ == "__main__":
    asyncio.run(main())
