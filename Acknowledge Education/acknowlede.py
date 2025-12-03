import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

FILE = "Acknowledge Education/acknowledgeeducation.xlsx"
OUTPUT = "Acknowledge Education/acknowledge_courses_update.sql"

# ==============================================================
# HELPER FUNCTIONS
# ==============================================================

def clean_html(html):
    if not html:
        return ""
    html = re.sub(r"\s+", " ", html)
    html = html.replace("'", "''")
    return html.strip()


# ---------------- DESCRIPTION ----------------

def extract_description(soup):
    # Overview bisa dalam h4, h5, atau h6
    overview = soup.find(["h4", "h5", "h6"], string=re.compile("Course Overview", re.I))
    if not overview:
        return ""

    parts = []

    for sib in overview.find_all_next():
        # stop ketika heading section baru
        if sib.name in ["h4", "h5", "h6"] and not re.search("Course Overview", sib.text, re.I):
            break
        if sib.name == "p" and sib.text.strip():
            parts.append(str(sib))

    return clean_html(" ".join(parts))


# ---------------- DURATION ----------------

def extract_duration(soup):
    label = soup.find("div", class_="course-summary-item__label", string=re.compile("Duration", re.I))
    if not label:
        return ""

    value = label.find_next("div", class_="col-12 col-md-6")
    if not value:
        return ""

    raw = value.text.strip()
    m = re.search(r"(\d+(\.\d+)?)\s*(-year|year|years|month|months|week|weeks)", raw, re.I)
    return m.group(0) if m else ""


# ---------------- ENTRY REQUIREMENTS ----------------

def extract_entry_requirements(soup):
    patterns = [
        r"Entry requirements",
        r"Academic and English Requirements",
        r"English Requirements",
        r"Requirements – International Students",
        r"Requirements - International Students"
    ]

    label = None

    # CASE 1: <p> heading
    for p in soup.find_all("p"):
        if p.text and any(re.search(ptn, p.text, re.I) for ptn in patterns):
            label = p
            break

    # CASE 2: <h4> / <h5> heading
    if not label:
        label = soup.find(["h4", "h5"], string=re.compile("|".join(patterns), re.I))

    if not label:
        return ""

    # Ambil accordion-body
    accordion_body = label.find_parent().find_next("div", class_="accordion-body")
    if not accordion_body:
        return ""

    parts = []

    # CASE A: list <ul><li><p>...</p></li></ul>
    for li in accordion_body.find_all("li"):
        p = li.find("p")
        if p:
            parts.append(str(p))

    # CASE B: fallback ambil semua p
    if not parts:
        for p in accordion_body.find_all("p"):
            if p.text.strip():
                parts.append(str(p))

    return clean_html(" ".join(parts))


# ---------------- FEE ----------------

def extract_fee_value(soup):
    fee_patterns = [
        r"Full tuition fee",
        r"Tuition fee",
        r"Fees",
        r"International Student"
    ]

    for p in soup.find_all("p"):
        if p.text and any(re.search(ptn, p.text, re.I) for ptn in fee_patterns):
            m = re.search(r"\$([\d,\.]+)", p.text)
            if m:
                return m.group(1).replace(",", "")
    return ""


# ==============================================================
# MAIN LOOP
# ==============================================================

df = pd.read_excel(FILE)
sql_output = []

for idx, row in df.iterrows():
    url = row["url"]
    cricos = str(row["cricos"]).strip()

    print(f"Processing: {url}")

    try:
        res = requests.get(url, timeout=60)
    except:
        print("ERROR request:", url)
        continue

    soup = BeautifulSoup(res.text, "html.parser")

    description = extract_description(soup)
    duration = extract_duration(soup)
    entry_req = extract_entry_requirements(soup)
    fee = extract_fee_value(soup)

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
