import time
import pytest
from pages_methods.elements.check_box import Checkbox
from pages_methods.main_page_demoqa import MainPageDemoQA


@pytest.mark.usefixtures
class TestCheckboxDownloads:

    def test_select_elements(self):
        assert MainPageDemoQA().check_elements_is_visible(self.driver)
        MainPageDemoQA().click_elements(self.driver)

    def test_select_checkbox(self):
        assert Checkbox().verify_check_box(self.driver)
        Checkbox().click_checkbox(self.driver)
        assert Checkbox().check_home_visibility(self.driver)

    def test_expand_home(self):
        Checkbox().expand_home(self.driver)
        assert Checkbox().check_downloads_visibility(self.driver)

    def test_click_downloads(self):
        Checkbox().click_downloads(self.driver)
        assert Checkbox().check_result(self.driver)

    def test_check_results(self):
        assert Checkbox().check_downloads_results(self.driver)
        time.sleep(1)
