"""Test UWA with Playwright v3 - scroll to fees section."""
import asyncio, re
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        print("Navigating...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours', 
                        timeout=60000, wait_until='networkidle')
        await page.wait_for_timeout(3000)
        
        # Scroll to fees section by clicking the Fees & Scholarships link in nav
        fees_link = await page.query_selector('a[href*="Fees"]')
        if fees_link:
            await fees_link.click()
            await page.wait_for_timeout(3000)
        
        # Get all text
        text = await page.inner_text('body')
        
        # Look for "International Student Fees"  
        print("\n=== FEE SECTION (full) ===")
        idx = text.lower().find('international student fees')
        if idx >= 0:
            print(text[max(0,idx-200):idx+1500])
        else:
            # Try broader search
            for m in re.finditer(r'International|Fees? and', text):
                start = max(0, m.start()-50)
                ctx = text[start:m.end()+500]
                print(f"  at {m.start()}: {ctx[:500]}")
                print("---")
        
        # CRICOS from body
        print("\n=== CRICOS ===")
        for m in re.finditer(r'CRICOS', text):
            print(f"  {text[m.start():m.start()+80]}")
        
        # Duration
        print("\n=== DURATION ===")
        for m in re.finditer(r'(\d+)\s*years?\s*full', text, re.I):
            start = max(0, m.start()-20)
            print(f"  {text[start:m.end()+20]}")
        
        await browser.close()

asyncio.run(main())
