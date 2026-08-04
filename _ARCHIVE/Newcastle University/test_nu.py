import asyncio
import re
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# ===== UTILITY =====
def clean_html(html: str) -> str:
    """Clean whitespaces and escape SQL single quotes."""
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")
    return html.strip()

def extract_section_html(soup, header_text):
    """Find <h3> with given text and return the next container's HTML."""
    h3 = soup.find("h3", string=lambda x: x and header_text.lower() in x.lower())
    if not h3:
        return ""
    parent = h3.find_parent()
    body = parent.find_next("div")
    return clean_html(str(body)) if body else ""


async def scrape_one(url, page):
    print("🔍 Scraping:", url)

    await page.goto(url, timeout=120000, wait_until="domcontentloaded")
    html = await page.content()
    soup = BeautifulSoup(html, "html.parser")

    # ============ DESCRIPTION ============
    desc_block = soup.find("div", {"id": "Description"})
    description = clean_html(str(desc_block)) if desc_block else ""

    # ============ DURATION ============
    duration = ""
    dur_header = soup.find("h3", string=lambda x: x and "Full time duration" in x)
    if dur_header:
        val = dur_header.find_next("div")
        if val:
            match = re.search(r"(\d+)", val.get_text())
            if match:
                duration = f"{match.group(1)} years"

    # ============ CRICOS CODE ============
    cricos_code = ""
    cri_header = soup.find("h3", string=lambda x: x and "CRICOS" in x)
    if cri_header:
        val = cri_header.find_next("div")
        if val:
            match = re.search(r"\b\d{6}[A-Za-z]\b", val.get_text())
            if match:
                cricos_code = match.group(0)

    # ============ ENTRY REQUIREMENTS ============
    admission = extract_section_html(soup, "Admission requirements")
    english = extract_section_html(soup, "English language requirements")
    program_req = extract_section_html(soup, "Program requirements")

    entry_requirements = clean_html(
        f"{admission} {english} {program_req}"
    )

    # ============ APPLY FORM ============
    apply_form = url

    return {
        "cricos": cricos_code,
        "description": description,
        "duration": duration,
        "requirements": entry_requirements,
        "apply": apply_form
    }


async def main():
    # ===== LOAD EXCEL =====
    df = pd.read_excel("Newcastle University/handbook.xlsx")   # <-- ubah jika nama file berbeda
    urls = df["url"].tolist()

    sql_lines = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in urls:
            data = await scrape_one(url, page)

            sql = f"""
UPDATE courses SET
    course_description = '{data['description']}',
    total_course_duration = '{data['duration']}',
    offshore_tuition_fee = '',
    entry_requirements = '{data['requirements']}',
    apply_form = '{data['apply']}',
    updated_at = NOW()
WHERE cricos_course_code = '{data['cricos']}';
"""

            sql_lines.append(sql)

        await browser.close()

    # ===== SAVE SQL OUTPUT =====
    with open("newcastle_update.sql", "w", encoding="utf-8") as f:
        f.writelines(sql_lines)

    print("✅ Finished! File saved as: newcastle_update.sql")


# ===== RUN SCRIPT =====
if __name__ == "__main__":
    asyncio.run(main())
