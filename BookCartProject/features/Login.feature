Feature: BookCart login
  Scenario: Login to BookCart with valid credentials
    Given I launch Google Chrome
    When I open BookCart homepage
    Then I click on the login button
    Then Enter username "Teejay1" and password "Teejay8x"
    And Click on login button
    Then User is successfully logged to the Shopping page
