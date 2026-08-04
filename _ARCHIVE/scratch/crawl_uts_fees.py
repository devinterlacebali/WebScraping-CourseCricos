from scrapling.fetchers import Fetcher
from bs4 import BeautifulSoup

url = "https://fees.uts.edu.au/"
print(f"Fetching {url}...")
page = Fetcher.get(url, stealthy_headers=True)
html = str(page.html_content)
print("HTML length:", len(html))

soup = BeautifulSoup(html, "html.parser")
print("Page Title:", soup.title.string.strip() if soup.title else "No Title")

forms = soup.find_all("form")
print(f"Found {len(forms)} forms:")
for idx, f in enumerate(forms):
    print(f"  Form {idx}: id={f.get('id')}, action={f.get('action')}")
    for inp in f.find_all(["input", "select"]):
        print(f"    Input: name={inp.get('name')}, type={inp.get('type')}, id={inp.get('id')}")
        if inp.name == "select":
            options = [opt.get_text(strip=True) for opt in inp.find_all("option")]
            print(f"      Options: {options[:5]}")
