import re

# ====== LOAD SQL FILE ======
sql_text = open("Notre Dame University/notredame.sql", "r", encoding="utf8").read()

# ====== DISCIPLINE → FEE MAPPING ======
fees = {
    "business": ("32199", "34356"),
    "nursing": ("38818", "39618"),
    "education": ("33806", "36401"),
    "law": ("40785", "42695"),
    "health": ("38222", "38863"),
    "science": ("41421", "46023"),
    "physio": ("45523", "44640"),
    "rehab": ("45523", "44640"),
    "counsell": ("34860", "37764"),
    "society": ("33589", "34078"),
    "culture": ("33589", "34078"),
    "philosophy": ("32849", "34078"),
    "theology": ("32849", "34078"),
    "architecture": ("36871", "41471"),
}

# ====== REGEX EXTRACTOR ======
apply_form_regex = re.compile(r"apply_form\s*=\s*'([^']+)'", re.IGNORECASE)
cricos_regex = re.compile(r"WHERE\s+cricos_course_code\s*=\s*'([^']+)'", re.IGNORECASE)

# ====== FEE DETECTOR ======
def detect_fee(url):
    url = url.lower()
    is_ug = "undergraduate" in url
    is_pg = "postgraduate" in url

    for key, (ug_fee, pg_fee) in fees.items():
        if key in url:
            return pg_fee if is_pg else ug_fee

    return None  # discipline tidak terdeteksi


# ====== PROCESS BLOCKS ======
blocks = sql_text.split("UPDATE courses SET")
results = []

for block in blocks:
    apply_match = apply_form_regex.search(block)
    cricos_match = cricos_regex.search(block)

    if not apply_match or not cricos_match:
        continue

    url = apply_match.group(1)
    cricos = cricos_match.group(1)

    fee = detect_fee(url)

    if fee:
        results.append(
f"UPDATE courses SET offshore_tuition_fee = '{fee}', updated_at = NOW() "
f"WHERE cricos_course_code = '{cricos}';"
        )

# ====== SAVE OUTPUT ======
open("Notre Dame University/update_fee_output.sql", "w").write("\n".join(results))

print("Generated", len(results), "fee update queries.")
