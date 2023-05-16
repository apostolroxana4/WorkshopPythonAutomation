Feature: DemoQa Checkbox subsection
  This feature verifies three categories: Desktop, Documents and Downloads

  Scenario: Check word file from Downloads category
    Given I navigate to Elements section
    When I click to Checkbox subsection
    Then I should enter into Checkbox subsection
    When I expand Home button
    And I click Downloads category
    Then I get expected message for Word File

  Scenario: Check angular file from Documents category
    Given I navigate to Elements section
    When I click to Checkbox subsection
    Then I should enter into Checkbox subsection
    When I expand Home button
    When I expand Documents category
    When I click Office
    Then I get expected message for Angular File


  Scenario: Check public file from Documents category
    Given I navigate to Elements section
    When I click to Checkbox subsection
    Then I should enter into Checkbox subsection
    When I expand Home button
    And I expand Documents category
    And I click Workspace
    Then I get expected message for Public File

