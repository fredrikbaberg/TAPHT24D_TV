import re

from playwright.sync_api import Page, expect


class BasePage:
    """Grundklass för att komma åt sidan."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        """Go to page"""
        self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

    def go_to_page(self, id):
        """Go to page by clicking by test id"""
        button = self.page.get_by_test_id(id)
        if button.is_visible(timeout=100) and button.is_enabled(timeout=100):
            button.click(timeout=100)

    def find_on_page(self, query):
        """Find on page"""
        expect(self.page).to_have_title(re.compile(query), timeout=100)
