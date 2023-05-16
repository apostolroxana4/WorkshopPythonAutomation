import pytest
from pytest_bdd import scenario, when, then, given
from actions.actions_elements import Actions


@scenario('..//myfeatures/checkbox.feature', 'Check angular file from Documents category')
@given("I navigate to Elements section")
def test_navigate_on_elements_section(browser):
    Actions().elements_from_main_page(browser)
    assert browser.current_url == "https://demoqa.com/elements"


@when("I click to Checkbox subsection")
def test_click_on_checkbox_subsection(browser):
    Actions().click_checkbox_subsection(browser)


@then("I should enter into Checkbox subsection")
def test_check_on_checkbox_subsection(browser):
    assert Actions().check_checkbox_subsection(browser)


@when("I expand Home button")
def test_expand_home_item(browser):
    Actions().expand_home_item(browser)
    assert Actions().check_home_item(browser)


@when("I expand Documents category")
def test_expand_documents_item(browser):
    Actions().expand_documents_item(browser)


@when("I click Office")
def test_click_on_workspace(browser):
    Actions().click_office(browser)
    Actions().click_workspace(browser)
    assert Actions().check_workspace(browser)


@then("I get expected message for Angular file")
def test_check_angular_file_from_workspace(browser):
    assert Actions().check_documents_workspace_angular(browser)