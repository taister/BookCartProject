# test_ShoppingCart.py

import pytest
from playwright.sync_api import sync_playwright
from pytest_bdd import scenario, given, when, then
from BookCartProject.PageObjectModel.shoppingCart_page import ShoppingCartPage

@scenario('../features/RemoveProductFromCart.feature', 'Remove a product from the cart')
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
    pass

@when("I open BookCart homepage")
def open_cart(shopping_cart_page):
    shopping_cart_page.navigate_to_homepage()

@when("I click on the first top-left Add to Cart button")
def add_first_item_to_cart(shopping_cart_page):
    shopping_cart_page.add_first_product_to_cart()

@when("I open the cart")
def open_cart(shopping_cart_page):
    shopping_cart_page.click_cart_icon()

    #Verify product is in cart
    try:
        assert shopping_cart_page.is_product_in_cart("Harry Potter and the Chamber of Secrets")
    except AssertionError:
        # Capture a screenshot on failure for debugging
        shopping_cart_page.page.screenshot(path="cart_failure.png")
        raise   

@then("I remove the product from the cart")
def remove_product_from_cart(shopping_cart_page):
    shopping_cart_page.click_remove_product_from_cart()


