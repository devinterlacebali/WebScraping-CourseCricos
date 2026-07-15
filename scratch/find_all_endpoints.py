import asyncio
from playwright.async_api import async_playwright
import json
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

async def main():
    slug = "graduate-diploma-in-information-technology"
    campuses = ["bu", "on", "sy", "be", "al", "sh"]
    years = ["2026", "2027"]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for year in years:
            for campus in campuses:
                context = await browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                page = await context.new_page()
                
                url = f"https://www.latrobe.edu.au/courses/data/{year}/international/{campus}/{slug}"
                try:
                    response = await page.goto(url, wait_until="domcontentloaded", timeout=15000)
                    status = response.status if response else 0
                    if status == 200:
                        text = await page.evaluate("() => document.body.innerText")
                        if "{" in text and "availability" in text:
                            data = json.loads(text)
                            c_data = data.get("data", {})
                            print(f"✅ FOUND: year={year}, campus={campus} | Title: {c_data.get('awardTitle')} | CRICOS: {c_data.get('cricosCourseCode')}")
                except Exception as e:
                    pass
                finally:
                    await context.close()
                    
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
