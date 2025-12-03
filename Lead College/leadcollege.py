import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


FILE = "Lead College/leadcollege.xlsx"
OUTPUT = "Lead College/leadcollege_courses_update.sql"


# ======================================================
# CLEAN HTML
# ======================================================
def clean_html(html):
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")
    return html.strip()


# ======================================================
# EXTRACT CRICOS
# ======================================================
def extract_cricos(soup):
    block = soup.find("p", class_="course-code")
    if not block:
        return ""

    text = block.get_text(" ", strip=True)
    m = re.search(r"CRICOS Code:\s*([0-9]{6,7}[A-Z])", text)
    return m.group(1) if m else ""


# ======================================================
# EXTRACT DURATION  (CASE 1 + CASE 2)
# ======================================================
def extract_duration(soup):

    # CASE 1 — <li>Duration<span>52 Weeks</span></li>
    for li in soup.find_all("li"):
        full_text = li.get_text(" ", strip=True)
        if "Duration" in full_text:
            span = li.find("span")
            if span:
                return span.text.strip()

    # CASE 2 — <tr><td>Course Duration</td><td>: 52 Weeks</td></tr>
    for tr in soup.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) >= 2:
            key = tds[0].get_text(strip=True)
            if "Course Duration" in key or key.strip() == "Duration":
                value = tds[1].get_text(strip=True)
                return value.replace(":", "").strip()

    return ""


# ======================================================
# GENERIC SECTION EXTRACTOR (for description & entry req)
# ======================================================
def extract_section(soup, section_id):
    start = soup.find("h2", id=section_id)
    if not start:
        return ""

    parts = []

    for sib in start.find_all_next():
        if sib.name == "h2":
            break

        if sib.name in ["p", "li"]:
            parts.append(str(sib))

    return clean_html(" ".join(parts))


# ======================================================
# MAIN LOOP
# ======================================================

df = pd.read_excel(FILE)
sql_output = []

for idx, row in df.iterrows():
    url = row["url"]

    print(f"Processing: {url}")

    try:
        res = requests.get(url, timeout=60)
    except:
        print("Request Error:", url)
        continue

    soup = BeautifulSoup(res.text, "html.parser")

    cricos = extract_cricos(soup)
    duration = extract_duration(soup)
    description = extract_section(soup, "course-description")
    entry_req = extract_section(soup, "entry-requirements")

    fee = ""  # memang tidak ada fee di website ini
    apply_form = url

    sql = f"""
UPDATE courses SET
    course_description = '{description}',
    total_course_duration = '{duration}',
    offshore_tuition_fee = '{fee}',
    entry_requirements = '{entry_req}',
    apply_form = '{apply_form}',
    updated_at = NOW()
WHERE cricos_course_code = '{cricos}';
"""
    sql_output.append(sql)


with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(sql_output))

print("\nDONE! SQL saved to:", OUTPUT)
