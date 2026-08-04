import json

with open("scrapers.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for idx, item in enumerate(data):
    name = item.get("name", "").lower()
    id_val = item.get("id", "").lower()
    if "western australia" in name or "uwa" in id_val:
        print(f"Index {idx}:")
        print(json.dumps(item, indent=2))
