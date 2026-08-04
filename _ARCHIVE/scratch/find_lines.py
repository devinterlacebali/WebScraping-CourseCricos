import json

with open("scrapers.json", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if '"id": "victoria-university"' in line:
        print(f"Line {idx}: {line.strip()}")
