from pytest_bdd import scenario, given, when, then
from pages.methods.home_page_methods import HomePageMethods
from pages.methods.side_menu_methods import SideMenuMethods
from pages.methods.checkbox_page_methods import CheckBoxPageMethods

@scenario('checkbox_page_bdd.feature', 'Click on downloads')
def test_checkbox():
    print("End of test run")


@given("I navigate to checkbox page")
def navigate_to_checkbox_page(self, browser):
    HomePageMethods.click_elements_button(self, browser)
    SideMenuMethods.click_on_submenu_item(self, browser, "Check Box")


@when("I click on arrow Home")
def click_on_arrow(self, browser):
    CheckBoxPageMethods.click_arrow(self, browser, "Home")


@when("I click on checkbox Downloads")
def click_on_checkbox(self, browser):
    CheckBoxPageMethods.click_checkbox(self, browser, "Downloads")


@then("I get expected message")
def verify_message(self, browser):
    assert CheckBoxPageMethods.get_message(self, browser) == "downloads wordFile excelFile"
