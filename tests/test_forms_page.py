import pytest
from pages.methods.forms_page_methods import FormsPageMethods
from pages.methods.home_page_methods import HomePageMethods
from pages.methods.side_menu_methods import SideMenuMethods


@pytest.skip(allow_module_level = True)
@pytest.mark.usefixtures("browser")
class TestCheckbox:
    def test_complete_form(self, browser):
        HomePageMethods.click_forms_button(self, browser)
        SideMenuMethods.click_on_submenu_item(self, browser, "Practice Form")

        FormsPageMethods.enter_first_name(self, browser, "John")
        FormsPageMethods.enter_last_name(self, browser, "Wick")
        FormsPageMethods.enter_email(self, browser, "john.wick@movies.io")
        FormsPageMethods.select_gender(self, browser, "male")
        FormsPageMethods.enter_mobile(self, browser, "0748901611")
        FormsPageMethods.select_date_of_birth(self, browser, "25 Apr 1990")

        #TODO Solve gender radio button element click intercepted

