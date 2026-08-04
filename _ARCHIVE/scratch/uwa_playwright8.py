"""UWA Playwright - scroll to fees, get all content."""
import asyncio, re
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("Navigating...")
        await page.goto('https://www.uwa.edu.au/study/courses/bachelor-of-nursing-honours',
                        timeout=60000, wait_until='domcontentloaded')
        await page.wait_for_timeout(3000)

        # Scroll gradually
        for i in range(8):
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight * %d/8)' % i)
            await page.wait_for_timeout(1000)

        # Bottom
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        await page.wait_for_timeout(2000)

        html = await page.content()

        # Fee amounts
        print("=== FEE AMOUNTS ===")
        for m in re.finditer(r'\$[0-9,]+', html):
            start = max(0, m.start() - 150)
            ctx = html[start:m.end() + 150]
            clean = re.sub(r'\s+', ' ', ctx)
            if any(kw in clean.lower() for kw in ['fee', 'tuition', 'international', 'indicative', 'annual', 'visa']):
                print(" ", clean[:300])

        # Get text
        text = await page.inner_text('body')

        print("\n=== SEARCH FEE ===")
        for m in re.finditer(r'[Ff]ee', text):
            start = max(0, m.start() - 30)
            ctx = text[start:m.end() + 200]
            c = re.sub(r'\s+', ' ', ctx)
            print(" ", c[:200])
            print("---")
            if 'international' in ctx.lower():
                print("^^^^^ INTERNATIONAL FEE FOUND ^^^^^")

        # Evaluate JS to find fee content
        print("\n=== EVALUATED ===")
        content = await page.evaluate("""() => {
            const allText = document.body.innerText;
            let idx = allText.toLowerCase().indexOf('international student fees');
            if (idx >= 0) return allText.substring(idx, idx + 3000);
            idx = allText.toLowerCase().indexOf('domestic student fees');
            if (idx >= 0) return allText.substring(idx, idx + 3000);
            return 'NOT FOUND';
        }""")
        print(content[:3000])

        print("\n=== BOTTOM 2000 ===")
        print(text[-2000:])

        await browser.close()

asyncio.run(main())
