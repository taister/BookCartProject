# PageObjectModel/shoppingCart_page.py

class ShoppingCartPage:
    def __init__(self, page):
        self.page = page      #creating an instance so I can call it later

        # Locators
        self.login_button_home = page.get_by_role("button", name="Login").nth(0)
        self.add_to_cart_first_item = page.locator(
            "(//button[.//span[contains(text(), 'Add to Cart')]])[1]"
        )
        self.cart_icon = self.page.locator("mat-toolbar button:has(mat-icon:text('shopping_cart'))").first

        # Cart container and product title links inside the cart
        self.cart_container = self.page.locator("mat-card-content table")
        self.cart_item_links = self.cart_container.locator("a[href^='/books/details']")

        # Locator to remove product from cart
        self.cart_remove_item = page.get_by_role("row", name="Harry Potter and the Chamber").get_by_role("button").nth(2)




    def navigate_to_homepage(self):
        self.page.goto("https://bookcart.azurewebsites.net/")
        self.page.wait_for_load_state("networkidle")
        self.login_button_home = self.page.get_by_role("button", name="Login").nth(0)
        self.login_button_home.wait_for(state="visible", timeout=15000)

    def add_first_product_to_cart(self):
        self.add_to_cart_first_item.wait_for(state="visible", timeout=5000)
        self.add_to_cart_first_item.click()

    def click_cart_icon(self):
        self.page.wait_for_load_state("networkidle")
        self.cart_icon.wait_for(state="attached", timeout=10000)  # Avoid waiting for "visible" if slow
        self.cart_icon.click()
        # Wait for cart container to appear after clicking cart icon
        self.cart_container.wait_for(state="visible", timeout=10000)

    def is_product_in_cart(self, expected_title):
        # Wait for cart container to be visible
        self.cart_container.wait_for(state="visible", timeout=5000)

        # Get all product titles from cart links
        product_titles = self.cart_item_links.all_text_contents()
        print(f"🛒 Cart items currently found: {product_titles}")

        # Check if expected title is found in any product title (case-insensitive)
        return any(expected_title.lower() in title.lower() for title in product_titles)

    def click_remove_product_from_cart(self):
        # Remove product from cart
        self.page.wait_for_load_state("networkidle")
        self.cart_remove_item.wait_for(state="visible", timeout=5000)
        self.cart_remove_item.click()


