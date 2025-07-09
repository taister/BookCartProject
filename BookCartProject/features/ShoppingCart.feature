Feature: BookCart Shopping Cart
    Scenario: Enter Shopping Cart page with product
        Given I launch google chrome
        When I open BookCart homepage
        Then I click on the first top-left Add to Cart button
        Then I click on the Cart icon
        Then Verify Harry Potter and the Chamber of Secrets is in the cart


