"""UWA Playwright - find fee data."""
import asyncio, re
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print("Navigating...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours',
                        timeout=60000, wait_until='domcontentloaded')
        await page.wait_for_timeout(5000)

        html = await page.content()

        # Find all fee amounts
        print("=== FEE AMOUNTS ===")
        for m in re.finditer(r'\$[0-9,]+', html):
            start = max(0, m.start() - 100)
            ctx = html[start:m.end() + 100]
            clean = re.sub(r'\s+', ' ', ctx)
            if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'indicative', 'annual']):
                print(f"  {clean[:250]}")

        # Dump all sections in page
        text = await page.inner_text('body')

        print("\n=== FEE TEXT ===")
        for m in re.finditer(r'[Ff]ee[s]?\s*[:$]', text):
            start = max(0, m.start() - 50)
            ctx = text[start:m.end() + 300]
            clean = re.sub(r'\s+', ' ', ctx)
            print(f"  {clean[:300]}")
            print("---")

        # Check if fee data is in a hidden tab
        print("\n=== ALL BUTTONS LINKS ===")
        els = await page.query_selector_all('button, [role="tab"], a.sticky-nav-link')
        for el in els:
            txt = await el.inner_text()
            if txt.strip():
                print(f"  '{txt.strip()}'")

        await browser.close()

asyncio.run(main())
