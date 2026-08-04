"""UWA Playwright - click Fees tab and extract."""
import asyncio, re
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print("Navigating...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours',
                        timeout=60000, wait_until='domcontentloaded')
        await page.wait_for_timeout(3000)

        # Click FEES & SCHOLARSHIPS button
        fee_btn = await page.query_selector('button:has-text("FEES")')
        if fee_btn:
            print("Clicking FEES & SCHOLARSHIPS...")
            try:
                await fee_btn.click(timeout=10000)
                await page.wait_for_timeout(3000)
                print("Clicked!")
            except:
                print("Force clicking...")
                await fee_btn.dispatch_event('click')
                await page.wait_for_timeout(3000)

        # Get full text
        text = await page.inner_text('body')

        print("\n=== FEE CONTENT ===")
        idx = text.lower().find('international student fees')
        if idx >= 0:
            print(text[idx:idx+2000])
        else:
            idx = text.lower().find('domestic student fees')
            if idx >= 0:
                print(text[idx:idx+2000])
            else:
                # Search $ amounts
                for m in re.finditer(r'\$[0-9,]+', text):
                    start = max(0, m.start() - 50)
                    ctx = text[start:m.end() + 50]
                    c = re.sub(r'\s+', ' ', ctx)
                    print(" ", c[:200])

        print("\n=== ENTRY REQUIREMENTS ===")
        idx = text.lower().find('entry requirements')
        if idx >= 0:
            print(text[idx:idx+500])

        await browser.close()

asyncio.run(main())
