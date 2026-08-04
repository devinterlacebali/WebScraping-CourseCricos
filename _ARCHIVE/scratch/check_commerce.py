import re

with open("The University of Western Australia/uwa_courses_update.sql", "r", encoding="utf-8") as f:
    sql_content = f.read()

# Split by UPDATE courses SET
blocks = sql_content.split("UPDATE courses SET")

print(f"Total blocks split: {len(blocks)}")
matched = []
for b in blocks:
    if "cricos_course_code = '083274J'" in b:
        apply_match = re.search(r"apply_form\s*=\s*'([^']+)'", b)
        url = apply_match.group(1) if apply_match else "unknown"
        matched.append(url)

for idx, url in enumerate(matched, 1):
    print(f"{idx}. URL: {url}")
