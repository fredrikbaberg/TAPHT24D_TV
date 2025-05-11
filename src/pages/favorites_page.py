from pages.base_page import BasePage


class MyBooksPage(BasePage):
    """Sidan Mina böcker"""

    def count_favorites(self):
        """Hämta antal böcker i listan"""
        return self.get_by_test_id("book-list").locator("li").count()
