import re
from playwright.sync_api import expect
from pages.catalog_page import CatalogPage


@then("bör jag se minst {count} sökresultat")
def step_impl(context, count):
    site = CatalogPage(context.page)
    number_of_books = site.count_books()
    assert number_of_books >= int(count.replace('"', ""))


@then('bör boken "{title}" av "{author}" synas i katalogen')
def step_impl(context, title, author):
    site = CatalogPage(context.page)
    # Matcha författare
    books = site.find_on_page_by_text(author)
    # Matcha titel, använder hela titeln.
    matches_title = books.get_by_text(re.compile(title))
    expect(matches_title).not_to_be_empty(timeout=1000)


@when('jag trycker {count} gånger på favoritmarkera "{title}"')
def step_impl(context, title, count):
    title = title.replace('"', "")
    count = int(count.replace('"', ""))
    page = CatalogPage(context.page)
    presses = 0
    while presses < count:
        page.mark_as_favorite(title)
        presses += 1


@then('bör "{title}" vara favoritmarkerad')
def step_impl(context, title):
    page = CatalogPage(context.page)
    item = page.get_by_test_id(f"star-{title}")
    expect(item).to_have_class("star selected", timeout=1000)


@then('bör inte "{title}" vara favoritmarkerad')
def step_impl(context, title):
    title = title.replace('"', "")
    page = CatalogPage(context.page)
    item = page.get_by_test_id(f"star-{title}")
    expect(item).not_to_have_class("star selected", timeout=1000)
