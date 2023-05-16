import pytest
from pages.elements.methods import Elements
from pytest_bdd import scenario, given, when, then


# @pytest.skip(allow_module_level=True)
@scenario("../../features/click_checkbox.feature", "Select documents")
@given("I am on elements")
def test_click_main_page_elements(browser):
    Elements().click_main_page_elements(browser)
    assert browser.current_url == "https://demoqa.com/elements"


@given("I selected the checkbox")
def test_select_checkbox(browser):
    Elements().click_checkbox(browser)
    assert browser.current_url == "https://demoqa.com/checkbox"
    assert Elements().check_home_title_visibility(browser)


@given("I expand home")
def test_expand_home(browser):
    Elements().click_expand(browser, 0)
    assert Elements().check_downloads_title(browser)


@given("I expand documents")
def test_expand_documents(browser):
    Elements().click_expand(browser, 1)
    assert Elements().check_office_title(browser)


@when("I click on office")
def test_expand_and_click_office(browser):
    Elements().click_office(browser)
    Elements().click_expand(browser, 2)
    assert Elements().check_result_length(browser)


@then("The correct office names are shown and number of items are displayed")
def test_check_result_office(browser):
    assert Elements().verify_names_in_result(browser)


@when("I click on workspace")
def test_expand_and_click_workspace(browser):
    Elements().click_workspace(browser)
    Elements().click_expand(browser, 1)
    assert Elements().check_result_length(browser)


@then("The correct workspace names are shown and number of items are displayed")
def test_check_result_workspace(browser):
    assert Elements().verify_names_in_result(browser)
