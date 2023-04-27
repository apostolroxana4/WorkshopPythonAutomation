import pytest
from pages.elements.methods import Elements

# @pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestCheckboxSelectDownloads:

    def test_click_main_page_elements(self):
        Elements().click_main_page_elements(self.driver)
        assert self.driver.current_url == "https://demoqa.com/elements"

    def test_select_checkbox(self):
        Elements().click_checkbox(self.driver)
        assert self.driver.current_url == "https://demoqa.com/checkbox"
        assert Elements().check_home_title_visibility(self.driver)

    def test_expand_home(self):
        Elements().click_expand(self.driver, 0)
        assert Elements().check_downloads_title(self.driver)

    def test_click_downloads(self):
        Elements().click_downloads(self.driver)
        Elements().click_expand(self.driver, 2)
        assert Elements().check_result_length(self.driver)
        assert Elements().verify_names_in_result(self.driver)
