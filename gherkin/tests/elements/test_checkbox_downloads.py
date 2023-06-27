import pytest
from gherkin.pages.elements.methods import Elements
from pytest_bdd import scenarios, given, when, then

element = Elements()
@pytest.skip(allow_module_level=True)
# scenarios("../../features/click_checkbox.feature")
# @scenario("../../features/click_checkbox.feature", "Select downloads")

@given("I am on elements")
def click_main_page_elements(browser):
    element.click_main_page_elements(browser)
    assert browser.current_url == "https://demoqa.com/elements"


@given("I selected the checkbox")
def select_checkbox(browser):
    element.click_checkbox(browser)
    assert browser.current_url == "https://demoqa.com/checkbox"
    assert element.check_home_title_visibility(browser)


@when("I expanded home and click downloads")
def expand_and_click_downloads(browser):
    element.click_expand(browser, 0)
    assert element.check_downloads_title(browser)
    element.click_expand(browser, 2)
    element.click_downloads(browser)
    assert element.check_result_length(browser)


@then("Downloads, Word File.doc and Excel File.doc are selected")
def check_result_downloads(browser):
    assert element.verify_names_in_result(browser)
