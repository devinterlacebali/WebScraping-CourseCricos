import os
import re
import sys
import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# Force UTF-8 encoding for stdout and stderr on Windows to support emojis in console
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

# === CLEAN NUMERIC FEE ===
def clean_numeric_fee(val: str) -> str:
    if not val or val.lower() in ("nan", "null", "n/a", ""):
        return "NULL"
    # remove any $, commas, spaces, or /week
    val_clean = re.sub(r"[^\d\.]", "", val)
    return val_clean if val_clean else "NULL"

# === EXTRACT COURSE DESCRIPTION ===
def extract_course_description(soup) -> str:
    # Skyline description is inside the first wpb_text_column element
    columns = soup.find_all(class_="wpb_text_column")
    if columns:
        first_col = columns[0]
        # Prefer the wpb_wrapper inside it
        wrapper = first_col.find(class_="wpb_wrapper")
        target_el = wrapper if wrapper else first_col
        
        # Clone target element to decompose style tags
        target_clone = BeautifulSoup(str(target_el), "html.parser")
        for style in target_clone.find_all("style"):
            style.decompose()
            
        return clean_html(str(target_clone))
    return ""

# === EXTRACT ENTRY REQUIREMENTS ===
def extract_entry_requirements(soup) -> str:
    # Skyline features an accordion/tab component with class w-tabs-section
    sections = soup.find_all(class_="w-tabs-section")
    for sec in sections:
        title_el = sec.find(class_="w-tabs-section-title")
        if title_el and "entry" in title_el.text.lower():
            content_el = sec.find(class_="w-tabs-section-content")
            if content_el:
                content_clone = BeautifulSoup(str(content_el), "html.parser")
                for style in content_clone.find_all("style"):
                    style.decompose()
                return clean_html(str(content_clone))
    return ""

# === SCRAPE PER COURSE ===
async def scrape_course(row, browser):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    duration = str(row["duration"]).strip()
    fee = clean_numeric_fee(str(row["fee"]))
    enrolment_fee = clean_numeric_fee(str(row.get("enrolment_fee", "")))
    materials_fee = clean_numeric_fee(str(row.get("materials_fee", "")))
    
    data = {
        "cricos": cricos,
        "title": str(row["title"]).strip(),
        "url": url,
        "course_description": "",
        "total_course_duration": duration,
        "offshore_tuition_fee": fee,
        "enrolment_fee": enrolment_fee,
        "materials_fee": materials_fee,
        "entry_requirements": "",
        "apply_form": url,
    }
    
    try:
        page = await browser.new_page()
        # Using domcontentloaded wait condition as the site has background assets that cause network timeouts
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        # Give 3 seconds for dynamic JS to render tabs
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract description
        desc_html = extract_course_description(soup)
        data["course_description"] = desc_html
        
        # Extract entry requirements
        entry_html = extract_entry_requirements(soup)
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
    excel_path = "Skyline International College/skyline.xlsx"
    sql_path = "Skyline International College/skyline_courses_update.sql"
    
    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return
        
    df = pd.read_excel(excel_path)
    results = []
    
    async with async_playwright() as p:
        # Launch browser in headless mode
        headless_env = os.environ.get("SCRAPER_HEADLESS", "True")
        headless_val = True if headless_env.lower() in ("true", "1") else False
        
        browser = await p.chromium.launch(headless=headless_val)
        
        for idx, row in df.iterrows():
            print(f"\n[{idx+1}/{len(df)}] Scraping: {row['url']}")
            course_data = await scrape_course(row, browser)
            results.append(course_data)
            
        await browser.close()
        
    # Write to SQL
    with open(sql_path, "w", encoding="utf-8") as f:
        # 1. Update provider institution details at the top
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, February, April, July, September',
    updated_at = NOW()
WHERE cricos_provider_code = '03639C';

""")
        # 2. Update courses details
        for d in results:
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
    offshore_tuition_fee = {d["offshore_tuition_fee"]},
    enrolment_fee = {d["enrolment_fee"]},
    materials_fee = {d["materials_fee"]},
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["apply_form"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';
""")
            
    print(f"\n✅ Finished! Scraped {len(results)} courses. SQL updates saved to {sql_path}")

if __name__ == "__main__":
    asyncio.run(main())
