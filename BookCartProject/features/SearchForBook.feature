Feature: BookCart search for book
    Scenario: Search for a book by title
        Given I launch Google Chrome
        When I search for "Harry Potter and the Prisoner of Azkaban"
        Then I click on "Harry Potter and the Prisoner of Azkaban"
        Then I see "Harry Potter and the Prisoner of Azkaban" in Shopping page
    