import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import sys


# ======================== CLEAN HTML ========================
def clean_html(html: str) -> str:
    if not html:
        return ""
    html = html.replace("\n", " ").replace("\r", " ")
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")  # SQL safe
    return html.strip()


# ======================== EXTRACT DESCRIPTION ========================
def extract_description(soup):
    unit_code_pattern = re.compile(r"\b[A-Z]{3,4}\d{3,5}\b")

    blocks = soup.select(".elementor-widget-text-editor .elementor-widget-container")

    for block in blocks:
        first_p = block.find("p")
        if not first_p:
            continue

        txt = first_p.get_text(" ", strip=True)

        # Cari block description berdasarkan unit code
        if not unit_code_pattern.search(txt):
            continue

        desc_list = []
        paragraphs = block.find_all("p", recursive=True)

        for p in paragraphs:
            text = p.get_text(" ", strip=True)

            # Jika heading mulai muncul → STOP
            if re.search(r"Pre[- ]?Enrolment|Pre[- ]?Training|Core Subjects|Packaging Rules|Assessment|Delivery", text, re.I):
                break

            # Jika <b> atau <strong> tapi BUKAN unit code → STOP
            if (p.find("b") or p.find("strong")) and not unit_code_pattern.search(text):
                break

            desc_list.append(str(p))

        return clean_html(" ".join(desc_list))

    return ""

# ======================== EXTRACT ENTRY REQUIREMENTS ========================
def extract_entry_requirements(soup):
    table = soup.select_one(".divTable")
    if not table:
        return ""

    rows = table.select(".divTableRow")
    final_rows = []

    for row in rows:
        cells = row.find_all("div", recursive=False)
        if len(cells) != 2:
            continue

        key_html = clean_html(str(cells[0]))
        val_html = clean_html(str(cells[1]))

        final_rows.append(f"<tr><td>{key_html}</td><td>{val_html}</td></tr>")

    # Bungkus tabel
    final_table = "<table>" + "".join(final_rows) + "</table>"

    return final_table

# ======================== EXTRACT FEES ========================
def extract_fees(soup):
    offshore = ""
    onshore = ""

    fee_blocks = soup.select("div.elementor-heading-title")

    for fb in fee_blocks:
        text = fb.get_text(" ", strip=True)

        m = re.search(r"Offshore[^$]*\$([\d,]+)", text, re.I)
        if m:
            offshore = m.group(1).replace(",", "")

        m2 = re.search(r"Onshore[^$]*\$([\d,]+)", text, re.I)
        if m2:
            onshore = m2.group(1).replace(",", "")

    return offshore, onshore


# ======================== EXTRACT DURATION ========================
def extract_duration(soup):
    for span in soup.find_all("span", class_="elementor-button-text"):
        text = span.get_text().lower()
        m = re.search(r"(\d+(\.\d+)?)\s*(weeks?|months?|years?)", text)
        if m:
            return m.group(0)
    return ""


# ======================== EXTRACT CRICOS ========================
def extract_cricos(soup, cricos_hint=""):
    # 1) If CRICOS provided in file, use it
    if isinstance(cricos_hint, str) and len(cricos_hint) >= 6:
        return cricos_hint

    # 2) Detect from page
    for span in soup.find_all("span", class_="elementor-button-text"):
        if "CRICOS" in span.get_text():
            m = re.search(r"([0-9]{6,7}[A-Z])", span.get_text())
            if m:
                return m.group(1)

    return ""


# ======================== MAIN LOOP ========================
df = pd.read_csv("Brighton Pacific College/aibtglobal-2025-12-03.csv")
urls = df["url"].tolist()

sql_output = []

for idx, row in df.iterrows():
    url = str(row["url"])
    cricos_hint = row["cricos"] if "cricos" in row else ""

    print(f"\nProcessing: {url}")
    sys.stdout.flush()

    try:
        r = requests.get(url, timeout=60)
    except Exception as e:
        print(f"[ERROR REQUEST] {url}: {e}")
        continue

    soup = BeautifulSoup(r.text, "html.parser")

    cricos = extract_cricos(soup, cricos_hint)
    duration = extract_duration(soup)
    offshore_fee, onshore_fee = extract_fees(soup)
    entry_req = extract_entry_requirements(soup)
    description = extract_description(soup)

    sql = f"""
UPDATE courses SET
    course_description = '{description}',
    total_course_duration = '{duration}',
    offshore_tuition_fee = '{offshore_fee}',
    onshore_tuition_fee = '{onshore_fee}',
    entry_requirements = '{entry_req}',
    apply_form = '{url}',
    updated_at = NOW()
WHERE cricos_course_code = '{cricos}';
"""

    sql_output.append(sql)
    print(sql)
    sys.stdout.flush()


# Save to file
with open("Brighton Pacific College/aibt_courses_update.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_output))

print("\n===== DONE! SQL saved to aibt_courses_update.sql =====")
