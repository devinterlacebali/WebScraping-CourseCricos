import re
from collections import Counter

with open("Victoria University/vu_courses_update.sql", "r", encoding="utf-8") as f:
    sql_content = f.read()

cricos_codes = re.findall(r"WHERE cricos_course_code = '([^']+)';", sql_content, re.IGNORECASE)

counts = Counter(cricos_codes)
dup_cricos = {k: v for k, v in counts.items() if v > 1}

print(f"Total unique CRICOS codes updated: {len(counts)}")
print(f"Total duplicate CRICOS code updates: {len(dup_cricos)}")
for k, v in sorted(dup_cricos.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f"CRICOS: {k} is updated {v} times")
