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
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        slug = "graduate-diploma-in-information-technology"
        campuses = ["bu", "on", "sy", "be", "al", "sh"]
        years = ["2026", "2027"]
        student_types = ["international", "domestic"]
        
        found = False
        for y in years:
            for s_type in student_types:
                for campus in campuses:
                    url = f"https://www.latrobe.edu.au/courses/data/{y}/{s_type}/{campus}/{slug}"
                    try:
                        response = await page.goto(url, wait_until="domcontentloaded", timeout=15000)
                        if response and response.status == 200:
                            text = await page.evaluate("() => document.body.innerText")
                            if "{" in text and "availability" in text:
                                print(f"✅ FOUND: year={y}, student_type={s_type}, campus={campus} -> {url}")
                                found = True
                                break
                    except Exception as e:
                        pass
                if found:
                    break
            if found:
                break
                
        if not found:
            print("❌ NOT FOUND for any combination!")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
