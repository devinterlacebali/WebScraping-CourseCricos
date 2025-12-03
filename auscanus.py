import re, asyncio, pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

CSV_FILE = "auscanus-2025-11-25.csv"
OUTPUT_SQL = "auscanus_update.sql"


def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")
    return html.strip()


def extract_duration(text: str) -> str:
    m = re.search(r"(\d{1,3})\s*weeks?", text, re.I)
    return f"{m.group(1)} weeks" if m else ""


async def scrape_one(page, url):
    print(f"🌐 Scraping: {url}")
    data = {
        "url": url,
        "cricos": "",
        "course_description": "",
        "entry_requirements": "",
        "duration": ""
    }

    try:
        await page.goto(url, timeout=120000)
        await page.wait_for_load_state("domcontentloaded")
        await page.wait_for_timeout(1500)

        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        # === CRICOS: <p>114256F</p> ===
        for p in soup.find_all("p"):
            txt = p.get_text(strip=True)
            m = re.search(r"\b([0-9]{6}[A-Za-z])\b", txt)
            if m:
                data["cricos"] = m.group(1)
                break

        # === DESCRIPTION: About the Course ===
        about_h4 = soup.find("h4", class_="main-title",
                             string=re.compile("about the course", re.I))
        if about_h4:
            desc_div = about_h4.find_next_sibling("div", class_="content")
            if desc_div:
                data["course_description"] = clean_html(str(desc_div))

        # === Duration ===
        for p in soup.find_all("p"):
            if p.get_text(strip=True).lower() == "duration":
                dur_p = p.find_next_sibling("p")
                if dur_p:
                    data["duration"] = extract_duration(dur_p.get_text())
                break

        # === ENTRY REQUIREMENTS ===
        entry_h4 = soup.find("h4", class_="main-title",
                             string=re.compile("course entry requirements", re.I))
        if entry_h4:
            cont = entry_h4.find_next_sibling("div", class_="content")
            if cont:
                data["entry_requirements"] = clean_html(str(cont))

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")

    return data


async def main():
    df = pd.read_csv(CSV_FILE)
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for i, row in df.iterrows():
            title = row["title"]
            url = row["url"]

            print(f"\n[{i+1}/{len(df)}] {title}")
            result = await scrape_one(page, url)
            results.append(result)

        await browser.close()

    # === Generate SQL ===
    sql_list = []
    for d in results:
        sql = f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '{d["duration"]}',
    offshore_tuition_fee = '',
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["url"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';"""

        sql_list.append(sql)

    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sql_list))

    print("\n✅ DONE — SQL saved to auscanus_update.sql")


asyncio.run(main())
