import re
from urllib.parse import parse_qs, quote_plus, unquote, urlparse

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    URL = "https://www.google.com"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_input: Locator = page.locator("textarea[name='q'], input[name='q']").first
        self.google_search_button: Locator = page.locator("input[name='btnK']").first
        self.im_feeling_lucky_button: Locator = page.locator("input[name='btnI']").first
        self.results_container: Locator = page.locator("#search")
        self.sorry_page_hint: Locator = page.locator("text=unusual traffic").first

    def goto(self) -> None:
        self.open(self.URL)

    def assert_home_loaded(self) -> None:
        expect(self.page).to_have_title("Google")
        expect(self.search_input).to_be_visible()
        expect(self.google_search_button).to_be_attached()
        expect(self.im_feeling_lucky_button).to_be_attached()

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_input.press("Enter")

    def assert_results_loaded(self) -> None:
        expect(self.results_container).to_be_visible()
        expect(self.page).to_have_title(r".+ - Google Search")

    def assert_search_navigated(self, query: str) -> None:
        expect(self.page).to_have_url(re.compile(r"https://www\.google\..*(search|sorry).*"))
        current_url = self.page.url
        encoded_query = quote_plus(query)
        parsed_url = urlparse(current_url)

        if parsed_url.path.startswith("/search"):
            assert f"q={encoded_query}" in current_url, f"Expected search query in URL. URL: {current_url}"
            return

        continue_param = parse_qs(parsed_url.query).get("continue", [""])[0]
        decoded_continue = unquote(continue_param)
        assert f"q={encoded_query}" in decoded_continue, (
            "Expected encoded query in Google continue URL when challenge page is shown. "
            f"URL: {current_url}"
        )

    def assert_search_outcome(self, query: str) -> None:
        self.assert_search_navigated(query)
        if self.results_container.is_visible():
            expect(self.page).to_have_title(r".+ - Google Search")
            return

        # Google may challenge automated traffic in some environments.
        expect(self.sorry_page_hint).to_be_visible()
