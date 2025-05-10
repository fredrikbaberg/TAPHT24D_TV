class CatalogPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
