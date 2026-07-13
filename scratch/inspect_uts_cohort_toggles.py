from curl_cffi import requests
from bs4 import BeautifulSoup
import re

url = "https://www.uts.edu.au/courses/bachelor-of-business"
response = requests.get(url, impersonate="chrome120")
soup = BeautifulSoup(response.text, "html.parser")

print("--- Searching for cohort selectors / buttons / links ---")
for el in soup.find_all(["button", "a", "select"]):
    text = el.get_text(strip=True).lower()
    href = el.get("href", "")
    classes = el.get("class", [])
    classes_str = " ".join(classes) if isinstance(classes, list) else str(classes)
    
    if any(k in text or k in href or k in classes_str for k in ["international", "domestic", "cohort", "student-type", "studenttype"]):
        print(f"Tag: {el.name} | class: '{classes_str}' | href: '{href}' | text: '{el.get_text(strip=True)[:100]}'")
