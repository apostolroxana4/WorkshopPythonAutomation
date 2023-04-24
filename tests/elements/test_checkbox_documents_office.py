import time

import pytest
from pages.elements.methods import Elements


@pytest.mark.usefixtures("browser")
# @pytest.skip(allow_module_level = True)
class TestCheckboxSelectDownloads:

    def test_click_main_page_elements(self):
        Elements().click_main_page_elements(self.driver)
        assert self.driver.current_url == "https://demoqa.com/elements"

    def test_select_checkbox(self):
        Elements().click_checkbox(self.driver)
        assert self.driver.current_url == "https://demoqa.com/checkbox"
        assert Elements().check_home_title(self.driver)

    def test_expand_home(self):
        Elements().click_expand_home(self.driver)
        assert Elements().check_downloads_title(self.driver)

    def test_expand_documents(self):
        Elements().click_expand_documents(self.driver)
        assert Elements().check_office_title(self.driver)

    def test_click_office(self):
        Elements().click_office(self.driver)
        assert Elements().check_office_results(self.driver)

    def test_click_workspace(self):
        Elements().click_office(self.driver)
        Elements().click_workspace(self.driver)
        assert Elements().check_workspace_results(self.driver)
