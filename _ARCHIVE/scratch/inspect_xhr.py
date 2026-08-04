import sys
import json
from scrapling import fetchers

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
    print(f"Fetching {url} with scrapling...")
    page = fetchers.StealthyFetcher.fetch(url, headless=True)
    
    print("Page status:", page.status)
    print("Page title:", page.css("title::text").get())
    
    print("\n--- Inspecting Captured XHR ---")
    xhrs = page.captured_xhr
    print(f"Total XHR requests captured: {len(xhrs)}")
    for idx, xhr in enumerate(xhrs):
        print(f"[{idx}] URL: {xhr.url}")
        print(f"    Method: {xhr.method}")
        print(f"    Status: {xhr.status}")
        try:
            body = xhr.text()
            print(f"    Body snippet: {body[:300]}")
        except Exception as e:
            print(f"    Error reading body: {e}")
            
    # Also save page text/html to inspect
    html_text = str(page.text)
    print("\nLength of text content:", len(html_text))
    with open("scratch/scrapling_text.html", "w", encoding="utf-8") as f:
        f.write(html_text)
    print("Saved text to scratch/scrapling_text.html")

if __name__ == "__main__":
    main()
