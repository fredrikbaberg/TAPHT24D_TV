import re

import playwright.sync_api
from playwright.sync_api import Page, expect

from pages.website_page import Website

# from pages.catalog_page import CatalogPage

@given(u'att jag är på hemsidan')
def step_impl(context):
    site = Website(context.page)
    site.navigate()

# @when("jag är på sidan Katalog")
# def step_impl(context):
#     catalog_page = CatalogPage(context.page)
#     catalog_page.navigate()


# @then("bör jag se minst 7 sökresultat")
# def step_impl(context):
#     raise NotImplementedError("STEP: Then bör jag se minst 7 sökresultat")


# @then('en titel är "Min katt är min chef"')
# def step_impl(context):
#     raise NotImplementedError('STEP: Then en titel är "Min katt är min chef"')
