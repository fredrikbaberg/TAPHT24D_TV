from pages.base_page import BasePage


class AddBookPage(BasePage):
    """Sidan Lägg till bok"""

    def fill_fields(self, title, author):
        """Fyll i fält för författare och titel"""
        # Fill in title
        self.page.get_by_test_id("add-input-title").fill(title, timeout=1000)
        # Fill in author
        self.page.get_by_test_id("add-input-author").fill(author, timeout=1000)

    def get_submit_key(self):
        """Hämta knapp för att lägga till ny bok"""
        return self.page.get_by_test_id("add-submit")
