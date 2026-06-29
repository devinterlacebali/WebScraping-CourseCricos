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

# === EXTRACT COURSE DESCRIPTION ===
def extract_course_description(soup) -> str:
    post_content = soup.find("div", class_="elementor-widget-theme-post-content")
    if post_content:
        container = post_content.find("div", class_="elementor-widget-container")
        if container:
            # Clean style tags
            for style in container.find_all("style"):
                style.decompose()
            return clean_html(str(container))
    return ""

# === EXTRACT ENTRY REQUIREMENTS ===
def extract_entry_requirements(soup) -> str:
    details_elts = soup.find_all("details")
    for detail in details_elts:
        summary = detail.find("summary")
        if summary and any(k in summary.text.lower() for k in ["admission", "entry", "criteria"]):
            widgets = detail.find_all(class_=["elementor-widget-text-editor", "elementor-widget-heading"])
            parts = []
            for widget in widgets:
                container = widget.find(class_="elementor-widget-container")
                if container:
                    # Clean style tags inside the widget container
                    for style in container.find_all("style"):
                        style.decompose()
                    parts.append(str(container))
                else:
                    for style in widget.find_all("style"):
                        style.decompose()
                    parts.append(str(widget))
            if parts:
                return clean_html(" ".join(parts))
            else:
                for style in detail.find_all("style"):
                    style.decompose()
                return clean_html(str(detail))
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
        await page.goto(url, wait_until="networkidle", timeout=90000)
        # Wait a bit for Elementor dynamic content
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract course description
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
    excel_path = "Brighton College/brighton.xlsx"
    sql_path = "Brighton College/brighton_courses_update.sql"
    
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
