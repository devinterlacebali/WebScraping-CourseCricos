import requests
import re

def main():
    print("Fetching robots.txt...")
    try:
        r = requests.get("https://www.latrobe.edu.au/robots.txt", timeout=15)
        print("Status code:", r.status_code)
        print("Content (first 1000 chars):")
        print(r.text[:1000])
        
        sitemaps = re.findall(r"sitemap:\s*(.*)", r.text, re.IGNORECASE)
        print("Sitemaps found in robots.txt:", sitemaps)
    except Exception as e:
        print("Error fetching robots.txt:", e)

if __name__ == "__main__":
    main()
