import re

from playwright.sync_api import Page


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
        if button.is_enabled(timeout=1000):
            button.click(timeout=1000)

    def find_on_page_by_text(self, query):
        """Find on page"""
        return self.page.get_by_text(re.compile(query))

    def get_by_test_id(self, id):
        """Get object by test id"""
        return self.page.get_by_test_id(id)
