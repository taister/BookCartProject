# test_ShoppingCart.py

import pytest
from playwright.sync_api import sync_playwright
from pytest_bdd import scenario, given, when, then
from BookCartProject.PageObjectModel.shoppingCart_page import ShoppingCartPage

@scenario('../features/ShoppingCart.feature', 'Enter Shopping Cart page with product')
def test_cart_product_presence():
    pass

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.pause()  # 👈 this opens the inspector 🎭

        yield page
        browser.close()

@pytest.fixture
def shopping_cart_page(page):
    return ShoppingCartPage(page)

@given("I launch google chrome")
def launch_browser(page):
    pass  # Handled by the fixture

@when("I open BookCart homepage")
def open_homepage(shopping_cart_page):
    shopping_cart_page.navigate_to_homepage()

@then("I click on the first top-left Add to Cart button")
def add_first_item_to_cart(shopping_cart_page):
    shopping_cart_page.add_first_product_to_cart()

@then("I click on the Cart icon")
def open_cart(shopping_cart_page):
    shopping_cart_page.click_cart_icon()

@then("Verify Harry Potter and the Chamber of Secrets is in the cart")
def verify_product_in_cart(shopping_cart_page):
    try:
        assert shopping_cart_page.is_product_in_cart("Harry Potter and the Chamber of Secrets")
    except AssertionError:
        # Capture a screenshot on failure for debugging
        shopping_cart_page.page.screenshot(path="cart_failure.png")
        raise


