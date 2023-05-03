from pytest_bdd import scenario, given, when, then
from pages.methods.home_page_methods import HomePageMethods
from pages.methods.side_menu_methods import SideMenuMethods
from pages.methods.select_menu_page_methods import SelectMenuPageMethods

@scenario('features/select_menu_page_bdd.feature', 'Select a value for groups dropdown')
def test_select_menu():
    pass


@given("I navigate to Select Menu page")
def navigate_to_checkbox_page(browser):
    HomePageMethods.click_widgets_button(browser)
    SideMenuMethods.click_on_submenu_item(browser, "Select Menu")


@when("I choose a Select Value dropdown value")
def select_dropdown_value(browser):
    SelectMenuPageMethods.select_dropdown_value(browser)


@then("I get expected value in the Select Value dropdown")
def verify_selected_value(browser):
    actual_value = SelectMenuPageMethods.get_ddSelectValueText(browser)
    print(actual_value)
    assert "Group 2, option 2" == actual_value


