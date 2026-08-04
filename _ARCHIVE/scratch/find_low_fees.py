import re

with open("The University Of Adelaide/adelaide_courses_update.sql", "r", encoding="utf-8") as f:
    sql_content = f.read()

# Find all courses that are updated with offshore_tuition_fee
matches = re.finditer(r"UPDATE courses SET(.*?)WHERE cricos_course_code = '([^']+)';", sql_content, re.DOTALL | re.IGNORECASE)

low_fee_updates = []
for m in matches:
    block = m.group(1)
    cricos = m.group(2)
    # Find offshore_tuition_fee
    fee_match = re.search(r"offshore_tuition_fee\s*=\s*(\d+|NULL)", block)
    duration_match = re.search(r"course_duration_per_week\s*=\s*(\d+|NULL)", block)
    
    if fee_match:
        fee_str = fee_match.group(1)
        if fee_str != "NULL":
            fee = int(fee_str)
            if fee < 1000:
                low_fee_updates.append((cricos, fee, block))

print(f"Found {len(low_fee_updates)} updates with fee < 1000:")
for cricos, fee, block in low_fee_updates:
    # get course name from comments before it
    print(f"CRICOS: {cricos} | Fee: {fee}")
