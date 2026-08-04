import re

with open("Victoria University/vu_courses_update.sql", "r", encoding="utf-8") as f:
    sql_content = f.read()

# Find all courses that are updated with offshore_tuition_fee and course_duration_per_week
matches = re.finditer(r"UPDATE courses SET(.*?)WHERE cricos_course_code = '([^']+)';", sql_content, re.DOTALL | re.IGNORECASE)

anomalies = []
for m in matches:
    block = m.group(1)
    cricos = m.group(2)
    
    fee_match = re.search(r"offshore_tuition_fee\s*=\s*(\d+|NULL)", block)
    duration_match = re.search(r"course_duration_per_week\s*=\s*(\d+|NULL)", block)
    
    if fee_match and duration_match:
        fee_str = fee_match.group(1)
        dur_str = duration_match.group(1)
        if fee_str != "NULL" and dur_str != "NULL":
            fee = int(fee_str)
            dur = int(dur_str)
            if dur > 0:
                annual = fee / dur * 52
                if annual > 100000 or annual < 5000:
                    anomalies.append((cricos, fee, dur, annual, block))

print(f"Found {len(anomalies)} anomalies in SQL file:")
for cricos, fee, dur, annual, block in anomalies:
    start_pos = sql_content.find(block)
    comment = ""
    if start_pos != -1:
        prev_lines = sql_content[:start_pos].split('\n')[-5:]
        comment_lines = [l for l in prev_lines if l.strip().startswith('--')]
        if comment_lines:
            comment = comment_lines[-1]
    
    # Extract the apply_form URL
    apply_match = re.search(r"apply_form\s*=\s*'([^']+)'", block)
    url = apply_match.group(1) if apply_match else "unknown"
    print(f"URL: {url} | CRICOS: {cricos} | Fee: {fee} | Dur: {dur}w | Annual: {annual:.2f}")
