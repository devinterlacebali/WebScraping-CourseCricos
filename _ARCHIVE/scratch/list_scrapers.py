import json

with open("scrapers.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for idx, item in enumerate(data):
    if item.get("id") == "victoria-university":
        print(f"Index {idx}:")
        print(json.dumps(item, indent=2))
