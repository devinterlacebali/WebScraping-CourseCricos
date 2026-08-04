import sys
from scrapling import fetchers

# Standard encoding for Windows environment
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
    print(f"Fetching {url} using scrapling.DynamicFetcher...")
    try:
        # DynamicFetcher renders JavaScript and runs in stealth mode
        page = fetchers.DynamicFetcher.fetch(
            url, 
            headless=True,
            network_idle=True,
            timeout=30000
        )
        
        text = page.get_all_text()
        print("Length of text content:", len(text))
        
        if "having trouble loading" in text.lower():
            print("❌ Still got the 'trouble loading' error.")
        else:
            print("✅ Success! No 'trouble loading' error found.")
            
        # Let's see some course details if present
        print("Page Title:", page.css("title::text").get())
        
        # Print a snippet of page text
        print("\nPage text snippet (first 1000 chars):")
        print(text[:1000])
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
