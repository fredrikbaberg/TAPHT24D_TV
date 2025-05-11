# import re
# from playwright.sync_api import expect
# from pages.add_book_page import AddBookPage
# from pages.base_page import BasePage
# from pages.catalog_page import CatalogPage


# @given("jag är på sidan Lägg till bok")
# def step_impl(context):
#     site = BasePage(context.page)
#     site.navigate()
#     site.go_to_page("add-book")
#     expect(context.page.get_by_test_id("add-book")).to_be_disabled()


# @when('jag lägger till boken "{title}" av "{author}"')
# def step_impl(context, title, author):
#     site = AddBookPage(context.page)
#     site.add_book(title, author)
#     # Kontrollera att fälten är tomma.
#     expect(context.page.get_by_test_id("add-input-title")).to_be_empty()
#     expect(context.page.get_by_test_id("add-input-author")).to_be_empty()


# @when("jag går till sidan Katalog")
# def step_impl(context):
#     site = AddBookPage(context.page)
#     site.go_to_page("catalog")


# # page.get_by_test_id("add-book").click()
# # page.get_by_test_id("add-input-title").click()
# # page.get_by_test_id("add-input-title").fill("Imorgon när kriget kom")
# # page.get_by_test_id("add-input-title").press("Tab")
# # page.get_by_test_id("add-input-author").fill("John Marsden")
# # page.get_by_test_id("add-input-author").press("Tab")
# # page.get_by_test_id("add-submit").press("Shift+Tab")
# # page.get_by_test_id("add-submit").click()
# # page.get_by_test_id("catalog").click()
# # page.get_by_test_id("star-Imorgon när kriget kom").click()
