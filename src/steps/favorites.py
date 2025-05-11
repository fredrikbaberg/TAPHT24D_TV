from pages.favorites_page import MyBooksPage

from playwright.sync_api import expect


@then("finns {count} favoritmarkerade böcker")
def step_impl(context, count):
    site = MyBooksPage(context.page)
    number_of_favorites = site.count_favorites()
    count = int(count.replace('"', ""))
    assert number_of_favorites == count
