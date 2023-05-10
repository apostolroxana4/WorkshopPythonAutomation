

Feature: DemoQa Checkbox subsection
  This feature verifies three categories: Desktop, Documents and Downloads

  Background:
    Given the DemoQa page is displayed

  Scenario: Check word file from Downloads category
    When I click to Elements section
    Then I should enter into Elements section
    When I click Checkbox subsection
    Then I should enter into Checkbox subsection
    When I expand Home button
    Then I should enter into Home
    When I click Downloads category
    Then check word file from Downloads category

  Scenario: Check angular file and public file from Documents category
    When I click to Elements section
    And I should enter into Elements section
    When I click Checkbox subsection
    Then I should enter into Checkbox subsection
    When I expand Home button
    Then I should enter into Home
    When I expand Documents category
    Then I should enter into Documents category
    When I click Office
    Then check public file from Office
    When I click Workspace
    Then check angular file from Workspace

