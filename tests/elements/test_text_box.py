import pytest
from pages.elements.methods import Elements


@pytest.mark.usefixtures("browser")
@pytest.skip(allow_module_level=True)
class TestTextBox:
    def test_click_main_page_elements(self):
        Elements().click_main_page_elements(self.driver)
        assert self.driver.current_url == "https://demoqa.com/elements"

    def test_verify_checkbox_visibility(self):
        if Elements().check_checkbox(self.driver):
            pytest.skip()

        Elements().click_elements(self.driver)
        assert self.driver.current_url == "https://demoqa.com/elements"

    def test_select_checkbox(self):
        Elements().click_checkbox(self.driver)
        assert self.driver.current_url == "https://demoqa.com/checkbox"
        assert Elements().check_home_title(self.driver)

    def test_expand_home(self):
        Elements().click_expand_home(self.driver)
        assert Elements().check_documents_title(self.driver)

    @pytest.mark.xfail(reason='Documents is not visible after you refresh the page')
    def test_preemptive_fail(self):
        self.driver.refresh()
        Elements().click_expand_home(self.driver)

    def test_click_documents(self):
        Elements().click_documents(self.driver)
        assert Elements().check_documents_result(self.driver)
