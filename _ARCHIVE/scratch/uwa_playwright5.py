"""UWA - extract full HTML from Playwright to find fee data."""
import asyncio, re, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        print("Navigating...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours', 
                        timeout=60000, wait_until='networkidle')
        await page.wait_for_timeout(3000)
        
        # Get all html
        html = await page.content()
        
        # Search for fee amounts in raw html
        print("=== ALL $ AMOUNTS ===")
        for m in re.finditer(r'\$[0-9,]+', html):
            start = max(0, m.start() - 100)
            ctx = html[start:m.end() + 100]
            clean = re.sub(r'\s+', ' ', ctx)
            if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'indicative', 'annual']):
                print(f"  -> {clean[:250]}")
        
        # Check for JSON data in scripts
        print("\n=== SCRIPTS WITH DATA ===")
        for script in await page.query_selector_all('script'):
            text = await script.inner_text()
            if not text or len(text) < 100:
                continue
            if 'fee' in text.lower() or 'course' in text.lower() or 'International' in text:
                print(f"  Script ({len(text)} chars): {text[:500]}")
                print("---")
        
        # Search for tab content - maybe it's hidden initially
        print("\n=== TABS/ACCORDION ===")
        buttons = await page.query_selector_all('button, a, [role="tab"]')
        for btn in buttons:
            txt = await btn.inner_text()
            if 'fee' in txt.lower() or 'scholarship' in txt.lower() or 'international' in txt.lower():
                print(f"  Found: '{txt}'")
                # Try clicking it
                try:
                    await btn.click(timeout=5000)
                    await page.wait_for_timeout(2000)
                    # Get content after click
                    text = await page.inner_text('body')
                    idx = text.lower().find('international student fees')
                    if idx >= 0:
                        print(f"  AFTER CLICK: {text[idx:idx+1500]}")
                except:
                    print("  (not clickable)")
        
        await browser.close()

asyncio.run(main())
