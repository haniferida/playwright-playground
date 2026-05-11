from playwright.sync_api import Page, expect

from pages.google_search_page import GoogleSearchPage


def test_google_search_shows_results(page: Page) -> None:
    google_search_page = GoogleSearchPage(page)

    google_search_page.goto()
    google_search_page.assert_home_loaded()

    query = "Playwright Python pytest"
    google_search_page.search(query)
    google_search_page.assert_search_outcome(query)
    if page.locator("#search").is_visible():
        expect(page.locator("#search")).to_contain_text("Playwright")