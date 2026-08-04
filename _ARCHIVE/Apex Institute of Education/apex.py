import re, asyncio, pandas as pd, sys
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout


# ===============================================================
# CLEAN HTML
# ===============================================================
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = html.replace("\n", " ").replace("\r", " ")
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")  # SQL safe
    return html.strip()


# ===============================================================
# SCRAPER FUNCTION
# ===============================================================
async def scrape_apex(url, browser, retry=3):

    for attempt in range(retry):
        try:
            data = {
                "url": url,
                "course_description": "",
                "total_course_duration": "",
                "offshore_tuition_fee": "",
                "entry_requirements": "",
                "cricos_course_code": "",
                "apply_form": url
            }

            page = await browser.new_page()
            await page.goto(url, timeout=90000)
            await page.wait_for_load_state("load")

            html = await page.content()
            soup = BeautifulSoup(html, "html.parser")

            # =====================================================
            # VET COURSE DESCRIPTION (#desBlock)
            # =====================================================
            desc_start = soup.select_one("#desBlock")
            if desc_start:
                desc_html = []
                for sib in desc_start.find_all_next():
                    if sib.name == "h2" and sib.get("id") != "desBlock":
                        break
                    if sib.name == "p":
                        desc_html.append(str(sib))
                data["course_description"] = clean_html(" ".join(desc_html))

            # =====================================================
            # VET DURATION
            # =====================================================
            dur_block = soup.find("h3", string=re.compile("Duration", re.I))
            if dur_block and dur_block.find_parent("div", class_="det-box"):
                box = dur_block.find_parent("div", class_="det-box").get_text(" ", strip=True)
                dur_match = re.search(r"(\d+(\.\d+)?\s*(weeks?|years?|months?))", box, re.I)
                if dur_match:
                    data["total_course_duration"] = clean_html(dur_match.group(1))

            # =====================================================
            # VET FEES
            # =====================================================
            fee_block = soup.find("h3", string=re.compile("Fee", re.I))
            if fee_block and fee_block.find_parent("div", class_="det-box"):
                box = fee_block.find_parent("div", class_="det-box").get_text(" ", strip=True)
                fees = [int(f.replace(",", "")) for f in re.findall(r"\$([\d,]+)", box)]
                if fees:
                    data["offshore_tuition_fee"] = str(max(fees))

            # =====================================================
            # VET ENTRY REQUIREMENTS
            # =====================================================
            entry_h2 = soup.select_one("#entryRequirements")
            if entry_h2:
                entry_html = []
                for sib in entry_h2.find_all_next():
                    if sib.name == "h2":
                        break
                    if sib.name == "p":
                        entry_html.append(str(sib))
                data["entry_requirements"] = clean_html(" ".join(entry_html))

            # =====================================================
            # VET CRICOS
            # =====================================================
            crs = soup.select_one(".crcsCode span")
            if crs:
                data["cricos_course_code"] = crs.get_text(strip=True)

            # =====================================================
            # HE FALLBACKS (Bachelor / Master)
            # =====================================================

            # ---- CRICOS FROM <h1> ----
            if not data["cricos_course_code"]:
                h1 = soup.find("h1")
                if h1:
                    m = re.search(r"([0-9]{6,7}[A-Z])", h1.get_text(strip=True))
                    if m:
                        data["cricos_course_code"] = m.group(1)

            # ---- DURATION FROM <p>Duration<strong>3 Years</strong></p> ----
            # === HE DURATION FALLBACK (durationBlock) ===
            if not data["total_course_duration"]:
                dur_h2 = soup.find("h2", id="durationBlock")
                if dur_h2:
                    # Ambil paragraf pertama setelah heading
                    for sib in dur_h2.find_all_next():
                        if sib.name == "p":
                            text = sib.get_text(" ", strip=True)
                            # Cari pola "3 years", "6 Years", "1.5 years"
                            m = re.search(r"(\d+(\.\d+)?)\s*(years?|year|months?|month)", text, re.I)
                            if m:
                                data["total_course_duration"] = clean_html(m.group(0))
                            break

            # ---- DESCRIPTION FROM descriptionBlock ----
            if not data["course_description"]:
                desc_h2 = soup.find("h2", id="descriptionBlock")
                if desc_h2:
                    parts = []
                    for sib in desc_h2.find_all_next():
                        if sib.name == "h2":
                            break
                        if sib.name == "p":
                            parts.append(str(sib))
                    data["course_description"] = clean_html(" ".join(parts))

            # ---- ENTRY REQUIREMENTS FROM admissionBlock ----
            if not data["entry_requirements"]:
                adm_h2 = soup.find("h2", id="admissionBlock")
                if adm_h2:
                    parts = []
                    for sib in adm_h2.find_all_next():
                        if sib.name == "h2":
                            break
                        if sib.name == "p":
                            parts.append(str(sib))
                    data["entry_requirements"] = clean_html(" ".join(parts))

            # ---- FEE FROM HE Block ----
            if not data["offshore_tuition_fee"]:
                text = soup.get_text(" ", strip=True)
                m = re.search(r"Tuition Fee[:\sA-Za-z]*\$([\d,]+)", text)
                if m:
                    data["offshore_tuition_fee"] = m.group(1).replace(",", "")

            # =====================================================
            # FINAL CRICOS CHECK
            # =====================================================
            if not data["cricos_course_code"]:
                data["cricos_course_code"] = "UNKNOWN"

            await page.close()

            # =====================================================
            # SQL OUTPUT
            # =====================================================
            sql = f"""
UPDATE courses SET
    course_description = '{data["course_description"]}',
    total_course_duration = '{data["total_course_duration"]}',
    offshore_tuition_fee = '{data["offshore_tuition_fee"]}',
    entry_requirements = '{data["entry_requirements"]}',
    created_at = NOW(),
    updated_at = NOW(),
    apply_form = '{data["apply_form"]}'
WHERE cricos_course_code = '{data["cricos_course_code"]}';
"""

            print(f"\n--- {url} ---\n{sql}\n")
            sys.stdout.flush()

            return sql, data

        except PlaywrightTimeout:
            print(f"[TIMEOUT] Retrying {url} ({attempt+1}/{retry})")
            await asyncio.sleep(2)

        except Exception as e:
            print(f"[ERROR] {url}: {e}")
            await asyncio.sleep(1)

    return None, None  # failed after retries


# ===============================================================
# MAIN LOOP WITH SQL FILE OUTPUT
# ===============================================================
async def main():
    df = pd.read_excel("Apex Institute of Education/apex.xlsx")
    urls = df["url"].dropna().tolist()

    out_file = "apex_courses_update.sql"
    sql_out = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for url in urls:
            sql, data = await scrape_apex(url, browser)
            if sql:
                sql_out.append(sql)
        await browser.close()

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_out))

    print(f"\n=== DONE! SQL saved to {out_file} ===")


if __name__ == "__main__":
    asyncio.run(main())
