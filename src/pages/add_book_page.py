from pages.base_page import BasePage


class AddBookPage(BasePage):
    """Sidan Lägg till bok"""

    # def add_book(self, title, author):
    #     """Lägg till bok. Fyll i fälten och tryck submit."""
    #     # Fill in title
    #     self.page.get_by_test_id("add-input-title").fill(title, timeout=100)
    #     # Fill in author
    #     self.page.get_by_test_id("add-input-author").fill(author, timeout=100)
    #     # Submit data
    #     self.page.get_by_test_id("add-submit").click(timeout=100)

    def fill_fields(self, title, author):
        """Fyll i fält för författare och titel"""
        # Fill in title
        self.page.get_by_test_id("add-input-title").fill(title, timeout=100)
        # Fill in author
        self.page.get_by_test_id("add-input-author").fill(author, timeout=100)

    def get_submit_key(self):
        """Hämta knapp för att lägga till ny bok"""
        return self.page.get_by_test_id("add-submit")

    def get_element_by_id(self):
        """Hämta element efter ID"""
