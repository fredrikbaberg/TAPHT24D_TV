import re
from playwright.sync_api import expect, Keyboard
from pages.add_book_page import AddBookPage
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from helpers import cleanup_string

@when("jag fyller i {title} av {author}")
def step_impl(context, title, author):
    title = cleanup_string(title)
    author = cleanup_string(author)
    site = AddBookPage(context.page)
    site.fill_fields(title, author)

@then("går det inte att trycka på {button}")
def step_impl(context, button):
    site = AddBookPage(context.page)
    button = site.get_submit_key()
    expect(button).to_be_disabled()

@when(u'jag trycker på knappen {button}')
def step_impl(context, button):
    "Lägg till bok"
    site = AddBookPage(context.page)
    button = site.get_submit_key()
    button.click()

# @when('jag lägger till boken "{title}" av "{author}"')
# def step_impl(context, title, author):
#     site = AddBookPage(context.page)
#     site.fill_fields(title, author)
#     site.get_submit_key().click()

@when('jag trycker på fältet för "{field}"')
def step_impl(context, field):
    site = AddBookPage(context.page)
    site.get_by_test_id("add-input-title").click()

@when('jag trycker på tangenten "{keyboard_key}"')
def step_impl(context, keyboard_key):
    site = AddBookPage(context.page)
    site.page.keyboard.press(keyboard_key)

@then('bör fältet för "Författare" vara markerat')
def step_impl(context):
    site = AddBookPage(context.page)
    expect(site.get_by_test_id("add-input-author")).to_be_focused(timeout=100)