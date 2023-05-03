Feature: Select Menu
  A page where you can see and example of select menu usage

  Scenario: Select a value for groups dropdown
    Given I navigate to Select Menu page
    When I choose a Select Value dropdown value
    Then I get expected value in the Select Value dropdown