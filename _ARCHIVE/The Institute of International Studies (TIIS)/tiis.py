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

# === CLEAN NUMERIC FEE ===
def clean_numeric_fee(val: str) -> str:
    if not val or val.lower() in ("nan", "null", "n/a", ""):
        return "NULL"
    # remove any $, commas, spaces, or /week
    val_clean = re.sub(r"[^\d\.]", "", val)
    return val_clean if val_clean else "NULL"

# === EXTRACT COURSE DESCRIPTION ===
def extract_course_description(soup) -> str:
    # Look for the elementor-widget-wrap containing Overview heading
    for h in soup.find_all(["h1", "h2", "h3", "h4", "h5"]):
        if "overview" in h.get_text().lower():
            wrap = h.find_parent(class_="elementor-widget-wrap")
            if wrap:
                wrap_clone = BeautifulSoup(str(wrap), "html.parser")
                for tag in wrap_clone.find_all(["style", "script", "noscript"]):
                    tag.decompose()
                return clean_html(str(wrap_clone))
    return ""

# === SCRAPE CRITERIA PAGE ===
async def scrape_criteria(browser):
    url = "https://www.tiis.edu.au/criteria/"
    page = await browser.new_page()
    try:
        print(f"Fetching admission criteria from: {url}")
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        entry1_div = soup.find(id="entry1")
        entry2_div = soup.find(id="entry2")
        
        english_header = soup.find(id="english-proficiency")
        english_wrap = None
        if english_header:
            english_wrap = english_header.find_parent(class_="elementor-widget-wrap")
            
        return {
            "postgrad_entry": str(entry1_div) if entry1_div else "",
            "undergrad_entry": str(entry2_div) if entry2_div else "",
            "english": str(english_wrap) if english_wrap else ""
        }
    except Exception as e:
        print(f"❌ Error scraping criteria page: {e}")
        return {"postgrad_entry": "", "undergrad_entry": "", "english": ""}
    finally:
        await page.close()

# === BUILD ENTRY REQUIREMENTS ===
def build_entry_requirements(title: str, criteria_data) -> str:
    title_lower = title.lower()
    entry_html = ""
    if "bachelor" in title_lower:
        entry_html = criteria_data["undergrad_entry"]
    else:
        entry_html = criteria_data["postgrad_entry"]
        
    combined = f"""<div class="entry-requirements-container">
    <div class="academic-requirements">
        {entry_html}
    </div>
    <div class="english-requirements">
        {criteria_data["english"]}
    </div>
</div>"""
    
    soup = BeautifulSoup(combined, "html.parser")
    for tag in soup.find_all(["style", "script", "noscript"]):
        tag.decompose()
        
    return clean_html(str(soup))

# === SCRAPE PER COURSE ===
async def scrape_course(row, browser, criteria_data):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    duration = str(row["duration"]).strip()
    fee = clean_numeric_fee(str(row["fee"]))
    enrolment_fee = clean_numeric_fee(str(row.get("enrolment_fee", "")))
    materials_fee = clean_numeric_fee(str(row.get("materials_fee", "")))
    title = str(row["title"]).strip()
    
    data = {
        "cricos": cricos,
        "title": title,
        "url": url,
        "course_description": "",
        "total_course_duration": duration,
        "offshore_tuition_fee": fee,
        "enrolment_fee": enrolment_fee,
        "materials_fee": materials_fee,
        "entry_requirements": build_entry_requirements(title, criteria_data),
        "apply_form": url,
    }
    
    try:
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract course description (overview)
        desc_html = extract_course_description(soup)
        data["course_description"] = desc_html
        
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
    excel_path = "The Institute of International Studies (TIIS)/tiis.xlsx"
    sql_path = "The Institute of International Studies (TIIS)/tiis_courses_update.sql"
    
    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return
        
    df = pd.read_excel(excel_path)
    results = []
    
    async with async_playwright() as p:
        headless_env = os.environ.get("SCRAPER_HEADLESS", "True")
        headless_val = True if headless_env.lower() in ("true", "1") else False
        
        browser = await p.chromium.launch(headless=headless_val)
        
        # Scrape criteria first
        criteria_data = await scrape_criteria(browser)
        
        for idx, row in df.iterrows():
            print(f"\n[{idx+1}/{len(df)}] Scraping: {row['url']}")
            course_data = await scrape_course(row, browser, criteria_data)
            results.append(course_data)
            
        await browser.close()
        
    # Write SQL updates
    with open(sql_path, "w", encoding="utf-8") as f:
        # 1. Update provider institution details at the top
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, March, May, July, September, November',
    updated_at = NOW()
WHERE cricos_provider_code = '03705J';

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
