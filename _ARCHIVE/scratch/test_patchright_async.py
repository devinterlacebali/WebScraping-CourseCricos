import asyncio
import sys
from bs4 import BeautifulSoup

# Standard encoding for Windows environment
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def main():
    print("Importing async_playwright from patchright.async_api...")
    try:
        from patchright.async_api import async_playwright
    except Exception as e:
        print("Import failed:", e)
        return
        
    async with async_playwright() as p:
        print("Launching patchright chromium...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # We need the international hash route that fetches the international course data
        url = "https://www.latrobe.edu.au/courses/bachelor-of-business#/overview?location=BU&studentType=int&year=2026"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        
        print("Waiting for page load and API calls...")
        await page.wait_for_timeout(10000)
        
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        text = soup.get_text(" ", strip=True)
        
        if "trouble loading" in text.lower():
            print("❌ Patchright STILL got the 'trouble loading' error.")
        else:
            print("✅ SUCCESS! Patchright loaded the page successfully without errors.")
            print("Snippet of page text:")
            print(text[:800])
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
