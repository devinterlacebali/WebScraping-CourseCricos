from scrapling import fetchers

def main():
    url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
    print(f"Fetching {url} using scrapling.StealthyFetcher...")
    try:
        # Fetch the page with stealthy settings
        page = fetchers.StealthyFetcher.fetch(url, headless=True)
        
        # Check text content
        text = page.text
        print("Length of text content:", len(text) if text else 0)
        
        # Check if the "We're having trouble loading the course details" error is present
        if "We're having trouble loading the course details" in text:
            print("❌ Found error text in the response (Cloudflare/data loading blocked).")
        else:
            print("✅ Error text NOT found in response!")
            
        # Search for some expected course text
        if "specialisation" in text.lower():
            print("Found 'specialisation' in text")
        else:
            print("Did not find 'specialisation' in text")
            
        # Check if we can find any class details
        print("Page title:", page.css("title::text").get())
        
        # Save HTML to inspect
        with open("scratch/scrapling_latrobe.html", "w", encoding="utf-8") as f:
            f.write(text)
        print("Saved HTML to scratch/scrapling_latrobe.html")
            
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
