from pages.base_page import BasePage

from playwright.sync_api import expect


@then(u'finns {count} favoritmarkerade böcker')
def step_impl(context, count):    
    site = BasePage(context.page)
    number_of_favorites = site.get_by_test_id("book-list").count()
    assert number_of_favorites == int(count.replace('"',''))
