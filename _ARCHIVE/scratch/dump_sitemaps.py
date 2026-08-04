import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        for url in ["https://www.latrobe.edu.au/sitemap-master.xml", "https://www.latrobe.edu.au/sitemap/latest-sitemap.xml"]:
            print(f"=== Content of {url} ===")
            try:
                await page.goto(url, wait_until="domcontentloaded")
                content = await page.content()
                print(content[:5000])
            except Exception as e:
                print("Error:", e)
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
