import re
import asyncio
import pandas as pd
import sys
import os
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

# ===============================================================
# CLEAN HTML AND STRING HELPERS
# ===============================================================
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = html.replace("\n", " ").replace("\r", " ")
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")  # SQL safe
    return html.strip()

# ===============================================================
# EXTRACTION HELPERS
# ===============================================================
def get_accordion_body_by_title(soup, title_pattern):
    pattern = re.compile(title_pattern, re.I)
    
    # Try finding class accordion-button or accordion-header first
    for btn in soup.find_all(class_=re.compile(r"accordion-button|accordion-header", re.I)):
        if pattern.search(btn.get_text()):
            parent = btn.find_parent(class_="accordion-item")
            if parent:
                body = parent.select_one(".accordion-collapse") or parent.select_one(".accordion-body")
                if body:
                    return body
                    
    # Fallback to search any button, h2, h3, h4, a
    for tag in soup.find_all(["button", "h2", "h3", "h4", "a"]):
        if pattern.search(tag.get_text()):
            parent = tag.find_parent(class_="accordion-item")
            if parent:
                body = parent.select_one(".accordion-collapse") or parent.select_one(".accordion-body")
                if body:
                    return body
            sib = tag.find_next_sibling()
            if sib:
                return sib
    return None

def extract_description(soup):
    body = get_accordion_body_by_title(soup, r"About|Description")
    if body:
        return clean_html(str(body))
    return ""

def extract_duration(soup):
    body = get_accordion_body_by_title(soup, r"Duration")
    if body:
        text = body.get_text(" ", strip=True)
        m = re.search(r"\b(\d+)\s*weeks?\b", text, re.I)
        if m:
            return f"{m.group(1)} weeks"
        m_yr = re.search(r"\b(\d+|one|two|three)\s*years?\b", text, re.I)
        if m_yr:
            return f"{m_yr.group(1)} year"
        return clean_html(text)
    return ""

def extract_fee(soup):
    body = get_accordion_body_by_title(soup, r"Fees")
    if body:
        text = body.get_text(" ", strip=True)
        m = re.search(r"Tuition Fees?\s*(?:AUD\s*)?\$?\s*([\d,]+)", text, re.I)
        if m:
            return m.group(1).replace(",", "")
    return ""

def extract_requirements(soup):
    body = get_accordion_body_by_title(soup, r"Requirement")
    if body:
        return clean_html(str(body))
    return ""

def extract_cricos(soup, text_content):
    matches = re.findall(r"\b([0-9]{6,7}[A-Z])\b", text_content)
    # Exclude provider code 03800K
    matches = [m for m in matches if m != "03800K"]
    if matches:
        return matches[0]
    return "UNKNOWN"

# ===============================================================
# SCRAPER CORE FUNCTION
# ===============================================================
async def scrape_acmi(url, browser, retry=3):
    for attempt in range(retry):
        try:
            page = await browser.new_page()
            # Set extra headers to avoid 406
            await page.set_extra_http_headers({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            })
            await page.goto(url, timeout=90000)
            await page.wait_for_load_state("load")

            html = await page.content()
            soup = BeautifulSoup(html, "html.parser")
            text_content = soup.get_text(" ")

            data = {
                "url": url,
                "course_description": extract_description(soup),
                "total_course_duration": extract_duration(soup),
                "offshore_tuition_fee": extract_fee(soup),
                "entry_requirements": extract_requirements(soup),
                "cricos_course_code": extract_cricos(soup, text_content),
                "apply_form": url
            }

            await page.close()

            # SQL script generation
            sql = f"""UPDATE courses SET
    course_description = '{data["course_description"]}',
    total_course_duration = '{data["total_course_duration"]}',
    offshore_tuition_fee = '{data["offshore_tuition_fee"]}',
    entry_requirements = '{data["entry_requirements"]}',
    apply_form = '{data["apply_form"]}',
    created_at = NOW(),
    updated_at = NOW()
WHERE cricos_course_code = '{data["cricos_course_code"]}';"""

            print(f"\n--- Scraped {url} ---")
            print(f"CRICOS: {data['cricos_course_code']}")
            print(f"Duration: {data['total_course_duration']}")
            print(f"Fee: {data['offshore_tuition_fee']}")
            sys.stdout.flush()

            return sql, data

        except PlaywrightTimeout:
            print(f"[TIMEOUT] Retrying {url} ({attempt+1}/{retry})")
            await page.close()
            await asyncio.sleep(2)
        except Exception as e:
            print(f"[ERROR] {url}: {e}")
            try:
                await page.close()
            except:
                pass
            await asyncio.sleep(1)

    return None, None

# ===============================================================
# MAIN LOOP
# ===============================================================
async def main():
    # Make sure we use the correct path relative to project root or current dir
    excel_path = "Australian College of Management and Innovation/acmi.xlsx"
    if not os.path.exists(excel_path):
        excel_path = "acmi.xlsx"

    df = pd.read_excel(excel_path)
    urls = df["url"].dropna().tolist()

    out_file = "Australian College of Management and Innovation/acmi_courses_update.sql"
    if not os.path.exists("Australian College of Management and Innovation"):
        out_file = "acmi_courses_update.sql"

    sql_out = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for idx, url in enumerate(urls, 1):
            print(f"[{idx}/{len(urls)}] Scraping: {url}")
            sql, data = await scrape_acmi(url, browser)
            if sql:
                sql_out.append(sql)
        await browser.close()

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sql_out))

    print(f"\n=== DONE! SQL saved to {out_file} ===")

if __name__ == "__main__":
    asyncio.run(main())
