"""USQ Playwright - extract full page content including fee."""
import asyncio, re
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})

        print("Navigating to USQ course...")
        await page.goto('https://www.unisq.edu.au/study/degrees-and-courses/bachelor-of-nursing',
                        timeout=60000, wait_until='domcontentloaded')
        await page.wait_for_timeout(5000)

        # Scroll to trigger lazy sections
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        await page.wait_for_timeout(2000)

        text = await page.inner_text('body')

        print("\n=== FEE ===")
        for m in re.finditer(r'[Ff]ee[s]?\s*\$?', text):
            start = max(0, m.start() - 30)
            ctx = text[start:m.end() + 200]
            c = re.sub(r'\s+', ' ', ctx)
            print(" ", c[:250])
            print("---")

        print("\n=== DOLLAR AMOUNTS ===")
        for m in re.finditer(r'\$[0-9,]+', text):
            start = max(0, m.start() - 30)
            ctx = text[start:m.end() + 30]
            print(" ", re.sub(r'\s+', ' ', ctx)[:150])

        # Check fees link
        print("\n=== FEES LINK ===")
        fee_link = await page.query_selector('a:has-text("Fees")')
        if fee_link:
            href = await fee_link.get_attribute('href')
            print("  href:", href)
            if href:
                await page.goto(f'https://www.unisq.edu.au{href}', timeout=60000, wait_until='domcontentloaded')
                await page.wait_for_timeout(3000)
                text2 = await page.inner_text('body')
                print("  First 1000:", text2[:1000])

        await browser.close()

asyncio.run(main())
