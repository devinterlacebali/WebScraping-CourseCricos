import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import sys

# Standard encoding for Windows environment
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def main():
    async with async_playwright() as p:
        # Launch headed browser
        print("Launching headed chromium...")
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
        print(f"Navigating to {url} in headed mode...")
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        
        # Wait 10 seconds to let React load and try to fetch data
        print("Waiting for page rendering...")
        await page.wait_for_timeout(10000)
        
        content = await page.content()
        
        if "We're having trouble loading the course details" in content:
            print("❌ Headed mode STILL got the 'trouble loading' error.")
        else:
            print("✅ Success! No 'trouble loading' error found in headed mode.")
            # Let's save a snippet of the course description or requirements to verify
            soup = BeautifulSoup(content, "html.parser")
            print("Page Title:", soup.find("title").get_text(strip=True) if soup.find("title") else "No title")
            
            # Print first 500 chars of body text
            print("Body Text Preview:")
            print(soup.get_text("\n", strip=True)[:1000])
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
