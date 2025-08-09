import asyncio
from playwright.async_api import async_playwright, expect
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Go to the local server URL
        await page.goto('http://localhost:8000/index.html')

        # Click the "Become a Dev" button
        await page.get_by_role("link", name="Become a Dev").click()

        # Wait for the modal to appear
        modal = page.locator("#become-a-dev-modal")
        await expect(modal).to_be_visible()

        # The new languages are added at the end, and they are sorted by year (newest first).
        # My additions were from older years, so they should appear after scrolling.
        # Let's find the modal body and scroll to the bottom.
        modal_body = page.locator("#become-a-dev-body")

        # Scroll to the bottom of the modal body to see the new languages
        await modal_body.evaluate("node => node.scrollTop = node.scrollHeight")

        # Wait a moment for scrolling to finish and content to render
        await page.wait_for_timeout(500)

        # Take a screenshot of the modal content
        await modal.locator('.modal-content').screenshot(path="jules-scratch/verification/new_languages.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
