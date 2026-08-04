import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py") and "scratch" not in root and "venv" not in root:
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "fixed" in content or "dedup" in content or "duplicate" in content:
                    print(f"File: {path}")
            except Exception:
                pass
