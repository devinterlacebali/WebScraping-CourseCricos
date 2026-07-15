import asyncio
from playwright.async_api import async_playwright
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def check_url(page, url):
    print(f"Navigating to {url}...")
    try:
        response = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(5000)
        text = await page.evaluate("() => document.body.innerText")
        print("Status:", response.status if response else "No response")
        print("Length:", len(text))
        print("Snippet (first 300 chars):")
        print(text[:300].strip())
    except Exception as e:
        print("Error:", e)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # 1. Test if bachelor-of-business still works
        await check_url(page, "https://www.latrobe.edu.au/courses/data/2026/international/bu/bachelor-of-business")
        
        # 2. Test one of the failed URLs
        await check_url(page, "https://www.latrobe.edu.au/courses/data/2026/international/bu/graduate-diploma-in-information-technology")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
