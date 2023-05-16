import pytest
from pages.elements.methods import Elements
from pytest_bdd import scenario, given, when, then


# @pytest.skip(allow_module_level=True)
@scenario("../../features/click_checkbox.feature", "Select downloads")
@given("I am on elements")
def test_click_main_page_elements(browser):
    Elements().click_main_page_elements(browser)
    assert browser.current_url == "https://demoqa.com/elements"


@given("I selected the checkbox")
def test_select_checkbox(browser):
    Elements().click_checkbox(browser)
    assert browser.current_url == "https://demoqa.com/checkbox"
    assert Elements().check_home_title_visibility(browser)


@given("I expanded home")
def test_expand_home(browser):
    Elements().click_expand(browser, 0)
    assert Elements().check_downloads_title(browser)


@when("I expanded home and click downloads")
def test_expand_and_click_downloads(browser):
    Elements().click_expand(browser, 2)
    Elements().click_downloads(browser)
    assert Elements().check_result_length(browser)


@then("Downloads, Word File.doc and Excel File.doc are selected")
def test_check_result_downloads(browser):
    assert Elements().verify_names_in_result(browser)
