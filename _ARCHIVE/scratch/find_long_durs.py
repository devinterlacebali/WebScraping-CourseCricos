import re

with open("The University Of Adelaide/adelaide_courses_update.sql", "r", encoding="utf-8") as f:
    sql_content = f.read()

matches = re.finditer(r"UPDATE courses SET(.*?)WHERE cricos_course_code = '([^']+)';", sql_content, re.DOTALL | re.IGNORECASE)

long_durs = []
for m in matches:
    block = m.group(1)
    cricos = m.group(2)
    duration_match = re.search(r"course_duration_per_week\s*=\s*(\d+|NULL)", block)
    if duration_match:
        dur_str = duration_match.group(1)
        if dur_str != "NULL":
            dur = int(dur_str)
            if dur > 312:  # > 6 years
                long_durs.append((cricos, dur))

print(f"Found {len(long_durs)} updates with duration > 6 years:")
for cricos, dur in long_durs:
    print(f"CRICOS: {cricos} | Duration: {dur}w")
