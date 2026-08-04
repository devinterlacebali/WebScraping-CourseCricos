from bs4 import BeautifulSoup
import re

with open("scratch/uts_business.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("Total HTML length:", len(html))

# Let's search for any text containing "$"
dollar_texts = []
for node in soup.find_all(text=True):
    val = node.strip()
    if "$" in val:
        dollar_texts.append(val)

print(f"Found {len(dollar_texts)} elements containing '$':")
for d in list(set(dollar_texts))[:30]:
    print("  ", d)
