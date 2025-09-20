Feature: Remove product from cart
    Scenario: Remove a product from the cart
    Given I launch google chrome
    When I open BookCart homepage
    When I click on the first top-left Add to Cart button
    And I open the cart
    Then I remove the product from the cart
    
