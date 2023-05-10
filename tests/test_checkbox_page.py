import pytest

from pages.methods.home_page_methods import HomePageMethods
from pages.methods.side_menu_methods import SideMenuMethods
from pages.methods.checkbox_page_methods import CheckBoxPageMethods

@pytest.skip(allow_module_level = True)
@pytest.mark.usefixtures("browser")
class TestCheckbox:
    def test_checkbox_downloads(self, browser):
        HomePageMethods.click_elements_button(self, browser)
        SideMenuMethods.click_on_submenu_item(self, browser, "Check Box")

        CheckBoxPageMethods.click_arrow(self, browser, "Home")
        CheckBoxPageMethods.click_checkbox(self, browser, "Downloads")
        assert CheckBoxPageMethods.get_message(self, browser) == "downloads wordFile excelFile"

    def test_checkbox_office_workspace(self, browser):
        HomePageMethods.click_elements_button(self, browser)
        SideMenuMethods.click_on_submenu_item(self, browser, "Check Box")

        CheckBoxPageMethods.click_arrow(self, browser, "Home")
        CheckBoxPageMethods.click_arrow(self, browser, "Documents")
        CheckBoxPageMethods.click_checkbox(self, browser, "Office")

        assert CheckBoxPageMethods.get_message(self, browser) \
               == "office public private classified general"

        CheckBoxPageMethods.click_checkbox(self, browser, "WorkSpace")
        assert CheckBoxPageMethods.get_message(self, browser) \
               == "documents workspace react angular veu office public private classified general"
