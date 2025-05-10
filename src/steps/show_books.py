from playwright.sync_api import expect
from pages.catalog_page import CatalogPage


@given("att jag är på hemsidan")
def step_impl(context):
    site = CatalogPage(context.page)
    site.navigate()

@when(u'jag är på sidan Katalog')
def step_impl(context):
    site = CatalogPage(context.page)
    site.navigate()
    site.go_to_page('catalog')

@then(u'bör jag se minst 7 sökresultat')
def step_impl(context):
    site = CatalogPage(context.page)
    site.navigate()
    number_of_books = site.page.locator('.book').count()
    assert number_of_books >= 7

@then(u'bör boken "{title:s}" av "{author:s}" synas i katalogen')
def step_impl(context, title, author):
    site = CatalogPage(context.page)
    site.navigate()
