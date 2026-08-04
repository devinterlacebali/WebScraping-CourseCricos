"""Test UWA with Playwright."""
import asyncio
from playwright.async_api import async_playwright
import re, json

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        print("Navigating to UWA course...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours', 
                        timeout=60000, wait_until='networkidle')
        await page.wait_for_timeout(3000)
        
        # Get rendered content
        html = await page.content()
        text = await page.inner_text('body')
        
        print("=== PAGE TEXT (first 2000) ===")
        print(text[:2000])
        
        # Look for fee
        print("\n=== FEE INFO ===")
        fee_text = await page.inner_text('text=International Student Fees')
        if fee_text:
            parent = await page.evaluate('''() => {
                const el = document.querySelector('h3:contains(\"International Student Fees\")');
                if (!el) return '';
                let p = el.nextElementSibling;
                let texts = [];
                while(p && p.tagName !== 'H3') {
                    if(p.innerText) texts.push(p.innerText);
                    p = p.nextElementSibling;
                }
                return texts.join('\\n');
            }''')
            print(parent[:1000])
        
        # CRICOS
        print("\n=== CRICOS ===")
        cricos = await page.inner_text('text=CRICOS')
        print(cricos[:200])
        
        # Duration
        print("\n=== DURATION ===")
        dur = await page.inner_text('.course-quick-details') if await page.query_selector('.course-quick-details') else ''
        if not dur:
            dur = await page.inner_text('text=full time')
        print(dur[:500])
        
        await browser.close()

asyncio.run(main())
