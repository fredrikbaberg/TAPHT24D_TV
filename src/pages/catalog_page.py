from pages.base_page import BasePage


class CatalogPage(BasePage):
    """Sidan Katalog"""

    def mark_as_favorite(self, title):
        """Favoritmarkera"""
        self.page.get_by_test_id(f"star-{title}").click()
