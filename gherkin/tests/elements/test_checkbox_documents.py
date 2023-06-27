import pytest
from gherkin.pages.elements.methods import Elements
from pytest_bdd import scenarios, given, when, then

element = Elements()
@pytest.skip(allow_module_level=True)
# scenarios("../../features/click_checkbox.feature")
# @scenario("../../features/click_checkbox.feature", "Select documents")
# def test_ex():
#     pass
@given("I am on elements")
def test_click_main_page_elements(browser):
    element.click_main_page_elements(browser)
    assert browser.current_url == "https://demoqa.com/elements"


@given("I selected the checkbox")
def test_select_checkbox(browser):
    element.click_checkbox(browser)
    assert browser.current_url == "https://demoqa.com/checkbox"
    assert element.check_home_title_visibility(browser)


@when("I click on office")
def test_expand_and_click_office(browser):
    element.click_office(browser)
    element.click_expand(browser, 2)
    assert element.check_result_length(browser)


@then("The correct office names are shown and number of items are displayed")
def test_check_result_office(browser):
    assert element.verify_names_in_result(browser)


@when("I click on workspace")
def test_expand_and_click_workspace(browser):
    element.click_workspace(browser)
    element.click_expand(browser, 1)
    assert element.check_result_length(browser)


@then("The correct workspace names are shown and number of items are displayed")
def test_check_result_workspace(browser):
    assert element.verify_names_in_result(browser)
