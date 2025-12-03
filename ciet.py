import re, asyncio, pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

CSV_FILE = "ciet-2025-11-25.csv"
OUTPUT_SQL = "ciet_update.sql"


def clean_html(html: str) -> str:
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")
    return html.strip()


async def scrape_ciet_course(page, url):
    print(f"🌐 Scraping: {url}")
    data = {
        "url": url,
        "cricos": "",
        "course_description": "",
        "entry_requirements": ""
    }

    try:
        await page.goto(url, timeout=120000)
        await page.wait_for_load_state("domcontentloaded")
        await page.wait_for_timeout(1500)

        # Klik Entry Requirements
        try:
            await page.click("button:has-text('Entry Requirements')", timeout=5000)
            await page.wait_for_timeout(1000)
        except:
            print("⚠️ Entry Requirements button not clickable")

        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        # ===== CRICOS =====
        cricos_el = soup.find("h3", string=re.compile("CIRCOS Code", re.I))
        if cricos_el:
            m = re.search(r"([0-9A-Za-z]+)$", cricos_el.get_text())
            data["cricos"] = m.group(1) if m else ""

        # ===== COURSE DESCRIPTION =====
        h2 = soup.find("h2", string=re.compile("Course Overview", re.I))
        if h2:
            parts = []
            for sib in h2.next_siblings:
                if isinstance(sib, str):
                    continue
                if sib.name == "div" and "kb-row-layout-wrap" in sib.get("class", []):
                    break
                if sib.name == "p":
                    parts.append(str(sib))
            data["course_description"] = clean_html(" ".join(parts))

        # ===== ENTRY REQUIREMENTS =====
        for btn in soup.find_all("button"):
            if "entry requirements" in btn.get_text(strip=True).lower():
                panel_id = btn.get("aria-controls")
                if panel_id:
                    panel = soup.find("div", id=panel_id)
                    if panel:
                        inner = panel.find("div", class_="kt-accordion-panel-inner")
                        data["entry_requirements"] = clean_html(str(inner or panel))
                break

    except Exception as e:
        print(f"❌ Error while scraping {url}: {e}")

    return data


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

            data = await scrape_ciet_course(page, url)
            results.append(data)

        await browser.close()

    # ===== SQL OUTPUT =====
    sql_list = []
    for d in results:
        sql = f"""UPDATE courses SET
    course_description = '{d["course_description"]}',
    total_course_duration = '',
    offshore_tuition_fee = '',
    entry_requirements = '{d["entry_requirements"]}',
    apply_form = '{d["url"]}',
    updated_at = NOW()
WHERE cricos_course_code = '{d["cricos"]}';"""

        sql_list.append(sql)

    with open(OUTPUT_SQL, "w", encoding="utf-8") as f:
        f.write("\n\n".join(sql_list))

    print("\n✅ DONE! SQL saved to ciet_update.sql")


# RUN
asyncio.run(main())
