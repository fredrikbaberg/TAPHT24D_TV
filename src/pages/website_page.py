import re
import playwright

from playwright.sync_api import Page, expect


class Website:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        """Go to page"""
        self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")


def find_on_page(self, query):
    """Find on page"""
    expect(self.page).to_have_title(re.compile(query))
