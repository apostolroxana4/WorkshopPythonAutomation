from pytest_bdd import scenario, given, when, then
from pages.methods.home_page_methods import HomePageMethods
from pages.methods.side_menu_methods import SideMenuMethods
from pages.methods.checkbox_page_methods import CheckBoxPageMethods

@scenario('features/checkbox_page_bdd.feature', 'Click on downloads')
def test_checkbox():
    pass


@given("I navigate to checkbox page")
def navigate_to_checkbox_page(browser):
    HomePageMethods.click_elements_button(browser)
    SideMenuMethods.click_on_submenu_item(browser, "Check Box")


@when("I click on arrow Home")
def click_on_arrow(browser):
    CheckBoxPageMethods().click_arrow(browser, "Home")


@when("I click on checkbox Downloads")
def click_on_checkbox(browser):
    CheckBoxPageMethods.click_checkbox(browser, "Downloads")


@then("I get expected message")
def verify_message(browser):
    assert CheckBoxPageMethods.get_message(browser) == "downloads wordFile excelFile"
