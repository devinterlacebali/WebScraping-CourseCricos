"""Test UWA Playwright - just scroll and get text."""
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
        
        # Scroll to bottom to trigger lazy loading
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        await page.wait_for_timeout(2000)
        
        # Full page text
        text = await page.inner_text('body')
        
        # Search for fee
        print("\n=== International Student Fees ===")
        idx = text.lower().find('international student fees')
        if idx >= 0:
            print(text[max(0,idx-100):idx+2000])
        else:
            # search for any fee mention
            print("Not found. Searching for fee-related text...")
            for m in re.finditer(r'[Ff]ee[s]?', text):
                start = max(0, m.start() - 80)
                ctx = text[start:m.end() + 300]
                ctx_clean = re.sub(r'\s+', ' ', ctx)
                print(f"  ...{ctx_clean[:300]}...")
                print("---")
        
        # Duration
        print("\n=== DURATION ===")
        for m in re.finditer(r'(\d+)\s*year', text):
            start = max(0, m.start() - 20)
            print(f"  {text[start:m.end()+20]}")
        
        # CRICOS
        print("\n=== CRICOS ===")
        for m in re.finditer(r'CRICOS', text):
            print(f"  {text[m.start():m.start()+100]}")
        
        await browser.close()

asyncio.run(main())
