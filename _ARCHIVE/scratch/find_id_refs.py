import os

search_term = "victoria-university"
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith((".py", ".json", ".sh", ".bat")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                if search_term in content and "scratch" not in path and "scrapers.json" not in path:
                    print(f"Found in {path}")
            except Exception:
                pass
