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

# === EXTRACT SECTION CONTENT ===
def extract_section_html(soup, class_name):
    # Find all sections with the specified class name
    sections = soup.find_all("section", class_=class_name)
    if not sections:
        return ""
    
    parts = []
    for section in sections:
        # Find all text editors and headings inside the section
        widgets = section.find_all(class_=["elementor-widget-text-editor", "elementor-widget-heading"])
        for widget in widgets:
            container = widget.find(class_="elementor-widget-container")
            if container:
                parts.append(str(container))
            else:
                parts.append(str(widget))
                
    if parts:
        return clean_html(" ".join(parts))
    
    # Fallback to the text of the section
    return clean_html("".join(str(s) for s in sections))

# === SCRAPE PER COURSE ===
async def scrape_course(row, browser):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    duration = str(row["duration"]).strip()
    fee = str(row["fee"]).strip()
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
        # Set custom viewport and agent
        await page.goto(url, wait_until="networkidle", timeout=90000)
        # Wait a bit for Elementor dynamic content
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract course description
        desc_html = extract_section_html(soup, "about")
        if not desc_html:
            # Fallback search for heading
            about_h = soup.find(lambda tag: tag.name in ["h2", "h3", "h4"] and "about" in tag.text.lower())
            if about_h:
                parent_section = about_h.find_parent("section")
                if parent_section:
                    desc_html = clean_html(str(parent_section))
        data["course_description"] = desc_html
        
        # Extract entry requirements
        entry_html = extract_section_html(soup, "admission_req")
        if not entry_html:
            # Fallback search for heading
            req_h = soup.find(lambda tag: tag.name in ["h2", "h3", "h4"] and "admission" in tag.text.lower())
            if req_h:
                parent_section = req_h.find_parent("section")
                if parent_section:
                    entry_html = clean_html(str(parent_section))
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
    excel_path = "Crown Institute of Higher Education/cihe.xlsx"
    sql_path = "Crown Institute of Higher Education/cihe_courses_update.sql"
    
    if not os.path.exists(excel_path):
        print(f"❌ Excel file not found at: {excel_path}")
        return
        
    df = pd.read_excel(excel_path)
    results = []
    
    async with async_playwright() as p:
        # Launch browser in headless mode
        # The run_all.py runner passes environment variable to control headed mode
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
    intake_date = 'February, July, November',
    updated_at = NOW()
WHERE cricos_provider_code = '03744B';

""")
        # 2. Update courses details
        for d in results:
            f.write(f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["total_course_duration"]}',
    offshore_tuition_fee = '{d["offshore_tuition_fee"]}',
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
