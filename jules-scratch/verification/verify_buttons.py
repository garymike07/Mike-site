import asyncio
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        file_path = os.path.abspath('index.html')

        page.goto(f'file://{file_path}')

        # Use a simple, hardcoded wait. This is less ideal but more robust
        # if the environment has issues with more complex waiting strategies.
        page.wait_for_timeout(5000)

        # Scroll the container into view
        scroll_container = page.locator('#projects-scroll')
        scroll_container.scroll_into_view_if_needed()

        # Give a bit of time for any final rendering/animations after scroll
        page.wait_for_timeout(1000)

        # Screenshot just the scroll container
        scroll_container.screenshot(path='jules-scratch/verification/project_cards.png')

        browser.close()

if __name__ == '__main__':
    run()
