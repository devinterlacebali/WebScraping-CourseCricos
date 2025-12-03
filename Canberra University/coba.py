import re

input_file = "Canberra University/canbera_cleaned.sql"
output_file = "fee_only_updates.sql"

pattern = re.compile(
    r"UPDATE courses SET(.*?)WHERE cricos_course_code = '([^']+)';",
    re.DOTALL
)

fee_pattern = re.compile(r"offshore_tuition_fee\s*=\s*'([^']*)'")

results = []

with open(input_file, "r", encoding="utf8") as f:
    content = f.read()

matches = pattern.findall(content)

for block, cricos in matches:
    fee_match = fee_pattern.search(block)
    if fee_match:
        fee_value = fee_match.group(1)
    else:
        fee_value = ""

    new_sql = (
        f"UPDATE courses SET\n"
        f"    offshore_tuition_fee = '{fee_value}',\n"
        f"    updated_at = NOW()\n"
        f"WHERE cricos_course_code = '{cricos}';\n"
    )
    results.append(new_sql)

with open(output_file, "w", encoding="utf8") as f:
    f.write("\n".join(results))

print("Done! Output saved to:", output_file)
