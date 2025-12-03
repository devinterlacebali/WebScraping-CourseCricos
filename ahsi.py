import re, asyncio, pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

CSV_FILE = "ahsi-2025-11-25.csv"
OUTPUT_SQL = "ahsi_update.sql"


# ========= CLEAN HTML =========
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")
    return html.strip()


# ========= SCRAPER PER COURSE =========
async def scrape_ahsi_course(page, url):
    print(f"🌐 Scraping {url} ...")
    data = {
        "url": url,
        "cricos": "",
        "course_description": "",
        "duration": "",
        "entry_requirements": ""
    }

    try:
        await page.goto(url, timeout=90000)
        await page.wait_for_load_state("domcontentloaded")
        await page.wait_for_timeout(2000)

        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        # === CRICOS ===
        h4 = soup.find("h4", string=re.compile("CRICOS", re.I))
        if h4:
            text = h4.get_text()
            m = re.search(r"CRICOS\s*([0-9A-Za-z]+)", text)
            data["cricos"] = m.group(1) if m else ""

        # === DESCRIPTION ===
        h3_desc = soup.find("h3", string=re.compile("Course Description", re.I))
        if h3_desc:
            p_tag = h3_desc.find_next("p")
            if p_tag:
                data["course_description"] = clean_html(str(p_tag))

        # === DURATION ===
        td = soup.find("td", string=re.compile("weeks", re.I))
        if td:
            m = re.search(r"(\d{1,3}\s*weeks?)", td.get_text())
            if m:
                data["duration"] = m.group(1)

        # === ENTRY REQUIREMENTS ===
        h3_entry = soup.find("h3", string=re.compile("Course Entry Requirements", re.I))
        if h3_entry:
            div_row = h3_entry.find_next("div", class_="row")
            if div_row:
                data["entry_requirements"] = clean_html(str(div_row))

        return data

    except Exception as e:
        print(f"❌ Error: {e}")
        return data


# ========= MAIN LOOP =========
async def main():
    df = pd.read_csv(CSV_FILE)
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for i, row in df.iterrows():
            title = str(row["title"])
            url = str(row["url"])

            print(f"\n[{i+1}/{len(df)}] {title}")
            course_data = await scrape_ahsi_course(page, url)
            results.append(course_data)

        await browser.close()

    # ========= OUTPUT SQL =========
    sql_lines = []
    for d in results:
        sql = f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["duration"]}',
    offshore_tuition_fee = '',
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["url"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';"""

        sql_lines.append(sql)

    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sql_lines))

    print(f"\n✅ DONE! SQL saved to {OUTPUT_SQL}")


# RUN
asyncio.run(main())
