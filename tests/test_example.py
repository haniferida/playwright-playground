from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        page.wait_for_timeout(2000)
        browser.close()