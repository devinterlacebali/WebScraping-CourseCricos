import re

with open("The University of Western Australia/uwa_courses_update.sql", "r", encoding="utf-8") as f:
    sql_content = f.read()

# Find all course updates
matches = re.finditer(r"UPDATE courses SET(.*?)WHERE cricos_course_code = '([^']+)';", sql_content, re.DOTALL | re.IGNORECASE)

total = 0
non_null_dur = 0
for m in matches:
    block = m.group(1)
    total += 1
    duration_match = re.search(r"course_duration_per_week\s*=\s*(\d+|NULL)", block)
    if duration_match:
        dur_str = duration_match.group(1)
        if dur_str != "NULL":
            non_null_dur += 1

print(f"Total UWA updates: {total}")
print(f"Updates with non-null duration: {non_null_dur}")
