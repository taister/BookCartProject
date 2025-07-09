#importing libraries for browser automation

import pytest
from selenium import webdriver
from pytest_bdd import scenario, given, when, then

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Load all scenarios from specified feature file
@scenario('Login.feature', 'Login to BookCart with valid credentials')
def test_logo_presence():
    pass

# Set up the Chrome WebDriver for the test and ensure it quits after execution
@pytest.fixture     #A fixture is a reusable piece of code
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#Step: launch Chrome
@given("I launch Google Chrome")
def launch_browser(driver):
    pass

#Step: open homepage
@when("I open BookCart homepage")
def open_homepage(driver):
    driver.get("https://bookcart.azurewebsites.net/")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Login']"))
    )


#Step: click on login
@then("I click on the login button")
def click_login_button(driver):
    #Wait for the login button to be clickable
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Login']")))

    # Click the login button
    login_button.click()
 # Wait for the login page to load (e.g., wait for username input field)
    wait.until(EC.presence_of_element_located((By.ID, "mat-input-0")))  # Adjust locator as needed

#Step: enter credentials
@then('Enter username "Teejay1" and password "Teejay8x"')
def enter_credentials(driver):
    driver.find_element(By.ID, "mat-input-0").send_keys("Teejay1")
    driver.find_element(By.ID, "mat-input-1").send_keys("Teejay8x")
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']//span[@class='mdc-button__label'][normalize-space()='Login']"))
    )

#Step: click login
@then("Click on login button")
def login_button(driver):
    wait = WebDriverWait(driver, 15)
    login_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@class='mdc-button mdc-button--raised mat-mdc-raised-button mat-primary mat-mdc-button-base']//span[@class='mdc-button__label'][normalize-space()='Login']")
    ))
    login_btn.click()

#Step: Confirm shopping page
@then("User is successfully logged to the Shopping page")
def shopping_page(driver):
    wait = WebDriverWait(driver, 10)
    wishlist_icon = wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//button[contains(@class,'mdc-icon-button') and contains(@class,'mat-mdc-icon-button')]//mat-icon[@role='img']"
    )))

    assert wishlist_icon.is_displayed()
