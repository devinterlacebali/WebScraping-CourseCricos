import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # Listen to console events
        page.on("console", lambda msg: print(f"CONSOLE: [{msg.type}] {msg.text}"))
        # Listen to page errors (uncaught exceptions)
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        # Listen to request failures
        page.on("requestfailed", lambda req: print(f"REQ FAILED: {req.url} - {req.failure.error_text if req.failure else ''}"))
        
        url = "https://www.latrobe.edu.au/courses/bachelor-of-business"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        
        # Wait 8 seconds to let React/Vue load and try to fetch data
        print("Waiting for page load and API calls...")
        await page.wait_for_timeout(8000)
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
