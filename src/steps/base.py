import re
from pages.base_page import BasePage

from playwright.sync_api import expect

# Mappning mellan rubrik och test_id för navigation.
page_to_test_id = {
    "Katalog": "catalog",
    "Lägg till bok": "add-book",
    "Mina böcker": "favorites",
}


@given("att jag är på hemsidan")
def step_impl(context):
    site = BasePage(context.page)
    site.navigate()

@given("jag är på sidan {rubrik}")
def step_impl(context, rubrik):
    site = BasePage(context.page)
    site.go_to_page(rubrik.replace('"', ""))

@when("jag är på sidan {rubrik}")
def step_impl(context, rubrik):
    site = BasePage(context.page)
    site.go_to_page(rubrik.replace('"', ""))


@then("kan jag navigera till {rubrik}")
def step_impl(context, rubrik):
    site = BasePage(context.page)
    test_id = page_to_test_id[rubrik.replace('"', "")]
    expect(site.get_by_test_id(test_id)).to_be_enabled()


@then("kan jag inte navigera till {rubrik}")
def step_impl(context, rubrik):
    site = BasePage(context.page)
    test_id = page_to_test_id[rubrik.replace('"', "")]
    expect(site.get_by_test_id(test_id)).to_be_disabled()
