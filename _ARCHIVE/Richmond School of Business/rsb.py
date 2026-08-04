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
    cols = soup.find_all(class_="wpb_text_column")
    desc = ""
    # Col 4 is Course Overview
    if len(cols) >= 4:
        overview_html = str(cols[3].find(class_="wpb_wrapper") or cols[3])
        desc += f"<h4>Course Overview</h4>{overview_html}"
    # Col 5 is Target Group / Who should undertake
    if len(cols) >= 5:
        target_html = str(cols[4].find(class_="wpb_wrapper") or cols[4])
        desc += f"<h4>Who Should Undertake This Qualification</h4>{target_html}"
    # Col 7 is Course Subjects / Units
    if len(cols) >= 7:
        subjects_html = str(cols[6].find(class_="wpb_wrapper") or cols[6])
        desc += f"<h4>Course Subjects</h4>{subjects_html}"
        
    if desc:
        desc_soup = BeautifulSoup(desc, "html.parser")
        for tag in desc_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        # Clean class and style attributes
        for tag in desc_soup.find_all(True):
            if tag.has_attr("class"):
                del tag["class"]
            if tag.has_attr("style"):
                del tag["style"]
        return clean_html(str(desc_soup))
    return ""

# === EXTRACT ENTRY REQUIREMENTS ===
def extract_entry_requirements(soup) -> str:
    cols = soup.find_all(class_="wpb_text_column")
    req = ""
    
    # Let's find the columns dynamically or by standard positions
    # For most courses, entry requirements are around Col 9, and LLN is around Col 10
    # Let's scan columns containing relevant keywords
    academic_req = ""
    lln_req = ""
    
    for c in cols:
        text = c.get_text().lower()
        if "entry into this course requires" in text or "satisfactory completion of studies" in text or "entry requirements where international" in text:
            academic_req = str(c.find(class_="wpb_wrapper") or c)
        elif "undertake an lln test" in text or "language, literacy and numeracy" in text:
            lln_req = str(c.find(class_="wpb_wrapper") or c)
            
    if academic_req:
        req += f"<h4>Entry Requirements</h4>{academic_req}"
    elif len(cols) >= 9:
        req_html = str(cols[8].find(class_="wpb_wrapper") or cols[8])
        req += f"<h4>Entry Requirements</h4>{req_html}"
        
    if lln_req:
        req += f"<h4>Language, Literacy and Numeracy</h4>{lln_req}"
    elif len(cols) >= 10:
        lln_html = str(cols[9].find(class_="wpb_wrapper") or cols[9])
        req += f"<h4>Language, Literacy and Numeracy</h4>{lln_html}"
        
    if req:
        req_soup = BeautifulSoup(req, "html.parser")
        for tag in req_soup.find_all(["style", "script", "noscript"]):
            tag.decompose()
        for tag in req_soup.find_all(True):
            if tag.has_attr("class"):
                del tag["class"]
            if tag.has_attr("style"):
                del tag["style"]
        return clean_html(str(req_soup))
    return ""

# === SCRAPE PER COURSE ===
async def scrape_course(row, browser):
    url = str(row["url"]).strip()
    cricos = str(row["cricos"]).strip()
    duration = str(row["duration"]).strip()
    fee = clean_numeric_fee(str(row["fee"]))
    enrolment_fee = clean_numeric_fee(str(row.get("enrolment_fee", "250")))
    materials_fee = clean_numeric_fee(str(row.get("materials_fee", "95")))
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
        "entry_requirements": "",
        "apply_form": url,
    }
    
    try:
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract course description
        data["course_description"] = extract_course_description(soup)
        
        # Extract entry requirements
        data["entry_requirements"] = extract_entry_requirements(soup)
        
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
    excel_path = "Richmond School of Business/rsb.xlsx"
    sql_path = "Richmond School of Business/rsb_courses_update.sql"
    
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
        f.write(f"""-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, February, April, May, July, August, October, November',
    updated_at = NOW()
WHERE cricos_provider_code = '03717E';

""")
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
