import asyncio
import json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        api_url = "https://www.latrobe.edu.au/courses/data/2026/international/bu/graduate-certificate-in-international-business"
        try:
            response = await page.goto(api_url, wait_until="domcontentloaded", timeout=20000)
            status = response.status if response else 0
            print("Status:", status)
            if status == 403:
                await page.wait_for_timeout(5000)
            text = await page.evaluate("() => document.body.innerText")
            if "{" in text:
                data = json.loads(text)
                c_data = data.get("data", {})
                print("cricosCourseCode:", repr(c_data.get("cricosCourseCode")))
            else:
                print("Text content:", repr(text[:200]))
        except Exception as e:
            print("Error:", e)
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
