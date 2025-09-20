Feature: BookCart login
  Scenario: Login to BookCart with valid credentials
    Given I launch Google Chrome
    When I open BookCart homepage
    Then I click on the login button
    Then Enter username "<username>" and password "<password>"
    And Click on login button
    Then <expected_result>

    Examples:
      | username      | password     | expected_result                                  |
      | Teejay1       | Teejay8x     | User is successfully logged to the Shopping page |
      | invalid_user  | wrongpass123 | User sees an error message                       |
      