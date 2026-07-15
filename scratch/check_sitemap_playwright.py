import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        try:
            print("Navigating to robots.txt with Playwright...")
            response = await page.goto("https://www.latrobe.edu.au/robots.txt", wait_until="domcontentloaded", timeout=30000)
            print("Status:", response.status if response else "No response")
            content = await page.content()
            # extract text
            text = await page.evaluate("() => document.body.innerText")
            print("Content (first 1000 chars):")
            print(text[:1000])
        except Exception as e:
            print("Error:", e)
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
