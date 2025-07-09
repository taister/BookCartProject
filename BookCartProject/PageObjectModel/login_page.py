#PageObjectModel/login_page.py


class LoginPage:
    def __init__(self, page):
        self.page = page
        #Locators - called for each step of the login process
        self.login_button_home = page.get_by_role("button", name="Login").nth(0)
        self.username_input = page.locator("#mat-input-0")
        self.password_input = page.locator("#mat-input-1")
        self.login_button_card = page.locator("mat-card-actions button:has-text('Login')")
        self.wishlist_icon = page.locator(
            "//button[contains(@class,'mdc-icon-button') and contains(@class,'mat-mdc-icon-button')]//mat-icon[@role='img']"
        )



    def navigate_to_homepage(self):
        self.page.goto("https://bookcart.azurewebsites.net/")
        self.login_button_home.wait_for(state="visible", timeout=15000)


    def click_home_login_button(self):
        self.login_button_home.click()


    def enter_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button_card.wait_for(state="attached", timeout=5000)

    def submit_login(self):
        self.login_button_card.click()

    def is_login_successful(self):
        self.wishlist_icon.wait_for(state="visible", timeout=10000)
        return self.wishlist_icon.is_visible()
