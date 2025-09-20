# conftest.py

import pytest
from playwright.sync_api import sync_playwright

from PageObjectModel.login_page import LoginPage
from PageObjectModel.shoppingCart_page import ShoppingCartPage

# ------------- GLOBAL FIXTURES -------------

@pytest.fixture(scope="session")
def playwright_instance():
    """Start and yield a Playwright instance."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser_context(playwright_instance):
    """Launch a new browser context for each test function."""
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    """Create a new page object."""
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def base_url():
    return "https://bookcart.example.com"

# ------------- PAGE OBJECT FIXTURES -------------

@pytest.fixture
def login_page(page, base_url):
    """Return an instance of the LoginPage."""
    page.goto(base_url)
    return LoginPage(page)

@pytest.fixture
def shopping_cart_page(page, base_url):
    """Return an instance of the ShoppingCartPage."""
    page.goto(base_url)
    return ShoppingCartPage(page)