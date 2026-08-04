import asyncio
from playwright.async_api import async_playwright
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def main():
    async with async_playwright() as p:
        print("Launching chromium...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Navigate directly to the JSON API URL
        url = "https://www.latrobe.edu.au/courses/data/2026/international/bu/bachelor-of-business"
        print(f"Navigating directly to JSON URL: {url}...")
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            
            print("Waiting for Cloudflare verification/solving (15s)...")
            await page.wait_for_timeout(15000)
            
            content = await page.content()
            # print title to see if it's still Cloudflare or the JSON
            title = await page.title()
            print("Page Title:", title)
            
            # Print body text to see if it's the JSON content
            text = await page.evaluate("() => document.body.innerText")
            print("Response text length:", len(text))
            print("Response text snippet (first 1000 chars):")
            print(text[:1000])
            
            if "Just a moment..." not in text and ("{" in text or "course" in text.lower()):
                print("\n✅ SUCCESS! Navigating directly worked to load the JSON!")
            else:
                print("\n❌ Failed: Still showing Cloudflare challenge or empty.")
        except Exception as e:
            print("Error navigating:", e)
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
