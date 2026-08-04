"""UWA Playwright - proper tab click."""
import asyncio, re
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})

        print("Navigating...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours',
                        timeout=60000, wait_until='domcontentloaded')
        await page.wait_for_timeout(3000)

        # Scroll down a bit to show the sticky nav
        await page.evaluate('window.scrollTo(0, 800)')
        await page.wait_for_timeout(1000)

        # Look for FEES & SCHOLARSHIPS in the sticky nav tabs
        fee_tab = await page.query_selector('button[data-tab*="fee" i], button[data-tab*="FEE" i]')
        if not fee_tab:
            fee_tab = await page.query_selector('//button[contains(text(), "FEES")]')
        if not fee_tab:
            fee_tab = await page.query_selector('text=FEES & SCHOLARSHIPS')
        if not fee_tab:
            # Check all elements with "FEES" text
            els = await page.query_selector_all('*')
            for el in els:
                txt = await el.inner_text()
                if 'FEES' in txt and 'SCHOLARSHIPS' in txt:
                    print(f"Found element with text: {txt}")
                    tag = await el.evaluate('e => e.tagName')
                    print(f"Tag: {tag}")
                    # Try to click its parent button
                    parent = await el.evaluate('e => e.closest("button")')
                    if parent:
                        print("Has button parent")
                    break

        if fee_tab:
            print("Clicking FEES tab...")
            await fee_tab.click()
            await page.wait_for_timeout(3000)

        # Get the full text
        text = await page.inner_text('body')

        # Search for fee content
        print("\n=== INTERNATIONAL STUDENT FEES ===")
        idx = text.lower().find('international student fees')
        if idx >= 0:
            print(text[idx:idx+3000])
        else:
            print("NOT FOUND in text")
            # Try getting HTML to find fee content
            html = await page.content()
            for m in re.finditer(r'(International|Domestic).{0,30}Fee[^.]*\.', html):
                print("HTML:", m.group())
            # Dump all h2/h3
            for h in ['h2', 'h3', 'h4']:
                els = await page.query_selector_all(h)
                for el in els:
                    t = await el.inner_text()
                    if t.strip():
                        print(f"  {h}: {t.strip()[:80]}")

        # Also get $ amounts
        print("\n=== $ AMOUNTS ===")
        html = await page.content()
        for m in re.finditer(r'\$[0-9,]+\.?\d*', html):
            start = max(0, m.start() - 80)
            ctx = html[start:m.end() + 80]
            c = re.sub(r'\s+', ' ', ctx)
            if any(kw in c.lower() for kw in ['fee', 'tuition', 'international', 'indicative']):
                print(f"  {c[:250]}")

        await browser.close()

asyncio.run(main())
