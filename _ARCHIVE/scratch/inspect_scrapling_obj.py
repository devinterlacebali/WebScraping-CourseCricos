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
    print(f"Fetching {url}...")
    page = fetchers.StealthyFetcher.fetch(url, headless=True)
    
    print("Page object type:", type(page))
    print("Page attributes:")
    for attr in dir(page):
        if not attr.startswith("_"):
            try:
                val = getattr(page, attr)
                # Print only methods or short properties
                if callable(val):
                    print(f"  [method] {attr}")
                else:
                    print(f"  [property] {attr}: {type(val)}")
            except Exception as e:
                print(f"  [error] {attr}: {e}")

if __name__ == "__main__":
    main()
