import re

with open("The University Of Adelaide/adelaide_courses_update.sql", "r", encoding="utf-8") as f:
    sql_content = f.read()

# Let's find all UPDATE blocks for CRICOS 115751E, 115753C, 115677K
target_codes = ['115751E', '115753C', '115677K']

for target in target_codes:
    print(f"\n=====================================")
    print(f"Updates for CRICOS: {target}")
    print(f"=====================================")
    matches = re.finditer(r"UPDATE courses SET(.*?)WHERE cricos_course_code = '" + target + "';", sql_content, re.DOTALL | re.IGNORECASE)
    for idx, m in enumerate(matches, 1):
        block = m.group(1)
        apply_match = re.search(r"apply_form\s*=\s*'([^']+)'", block)
        url = apply_match.group(1) if apply_match else "unknown"
        # Search for course description snippet
        desc_match = re.search(r"course_description\s*=\s*'<h4>Overview</h4><p>(.*?)</p>'", block)
        desc = desc_match.group(1)[:100] if desc_match else ""
        print(f"{idx}. URL: {url}")
        if desc:
            print(f"   Desc: {desc}...")
