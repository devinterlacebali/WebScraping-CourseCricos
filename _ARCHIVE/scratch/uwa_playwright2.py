"""Test UWA with Playwright v2."""
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
        
        # Get fee section by clicking the Fees tab
        fee_tab = await page.query_selector('button:has-text("Fees")')
        if fee_tab:
            print("Clicking Fees tab...")
            await fee_tab.click()
            await page.wait_for_timeout(2000)
        
        # Get all text from page
        text = await page.inner_text('body')
        
        # Fee info
        print("\n=== FEE SECTION ===")
        # Find "International Student Fees" and surrounding text
        idx = text.lower().find('international student fees')
        if idx >= 0:
            print(text[idx:idx+1000])
        
        # Domestic fees too
        idx2 = text.lower().find('domestic student fees')
        if idx2 >= 0:
            print("\n--- Domestic ---")
            print(text[idx2:idx2+500])
        
        # Duration
        print("\n=== QUICK DETAILS ===")
        # Look for "QUICK DETAILS" area
        idx3 = text.lower().find('quick details')
        if idx3 >= 0:
            print(text[idx3:idx3+500])
        
        # CRICOS from footer
        print("\n=== CRICOS ===")
        cricos_idx = text.lower().find('cricos')
        if cricos_idx >= 0:
            print(text[cricos_idx:cricos_idx+100])
        
        await browser.close()

asyncio.run(main())
