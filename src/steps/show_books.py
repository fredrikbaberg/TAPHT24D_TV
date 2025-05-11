import re
from playwright.sync_api import expect
from pages.catalog_page import CatalogPage


# @when("jag är på sidan Katalog")
# def step_impl(context):
#     site = CatalogPage(context.page)
#     site.go_to_page("catalog")
#     expect(context.page.get_by_test_id("catalog")).to_be_disabled()


# @given("jag är på sidan Katalog")
# def step_impl(context):
#     site = CatalogPage(context.page)
#     site.go_to_page("catalog")


@then("bör jag se minst {count} sökresultat")
def step_impl(context, count):
    site = CatalogPage(context.page)
    site.navigate()
    number_of_books = site.page.locator(".book").count()
    assert number_of_books >= int(count.replace('"',''))


@then('bör boken "{title}" av "{author}" synas i katalogen')
def step_impl(context, title, author):
    site = CatalogPage(context.page)
    # Matcha författare
    books = site.find_on_page_by_text(author)
    # Matcha titel, räcker egentligen med delar av
    matches_title = books.get_by_text(re.compile(title))
    expect(matches_title).not_to_be_empty(timeout=100)

# @when(u'jag trycker på "{title}" "{count}" gång(er)')
# def step_impl(context, title, count):
#     raise NotImplementedError(u'STEP: When jag trycker på "Kaffekokaren som visste för mycket" "1" gång(er)')

# @then(u'bör den vara favoritmarkerad')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then bör den vara favoritmarkerad')

# @then(u'bör den inte vara favoritmarkerad')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then bör den inte vara favoritmarkerad')
