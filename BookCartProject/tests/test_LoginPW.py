# test_LoginPW.py

import pytest
from playwright.sync_api import sync_playwright
from pytest_bdd import scenario, given, when, then
from BookCartProject.PageObjectModel.login_page import LoginPage  # Import the P.O.M
  

@scenario('../features/Login.feature', 'Login to BookCart with valid credentials')
def test_logo_presence():
    pass

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@given("I launch Google Chrome")
def launch_browser(page):
    pass  # Handled by the fixture

@when("I open BookCart homepage")
def open_homepage(login_page):
    login_page.navigate_to_homepage()

@then("I click on the login button")
def click_login_button(login_page):
    login_page.click_home_login_button()

@then('Enter username "Teejay1" and password "Teejay8x"')
def enter_credentials(login_page):
    login_page.enter_credentials("Teejay1", "Teejay8x")

@then("Click on login button")
def login_button(login_page):
    login_page.submit_login()

@then("User is successfully logged to the Shopping page")
def shopping_page(login_page):
    assert login_page.is_login_successful()
