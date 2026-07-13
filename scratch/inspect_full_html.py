from curl_cffi import requests

url = "https://www.uts.edu.au/courses/bachelor-of-business"
print(f"Fetching {url}...")
r = requests.get(url, impersonate="chrome120")
with open("scratch/uts_business.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Saved HTML successfully.")
