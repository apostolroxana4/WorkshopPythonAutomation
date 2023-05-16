Feature: Click on checkboxes

  Scenario: Select downloads
    Given I am on elements
    And I selected the checkbox
    When I expanded home and click downloads
    Then Downloads, Word File.doc and Excel File.doc are selected

  Scenario: Select documents
    Given I am on elements
    And I selected the checkbox
    And I expand home
    And I expand documents
    When I click on office
    Then The correct office names are shown and number of items are displayed
    When I click on workspace
    Then The correct workspace names are shown and number of items are displayed