with open("The University Of Adelaide/adelaide_courses_update.sql", "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if "aviation" in line.lower():
            print(f"Line {idx}: {line[:200]}")
