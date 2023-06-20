import pytest
from pages.elements.methods import Elements

element = Elements()
@pytest.mark.usefixtures("browser")
@pytest.skip(allow_module_level=True)
class TestTextBox:
    def test_click_main_page_elements(self):
        element.click_main_page_elements(self.driver)
        assert self.driver.current_url == "https://demoqa.com/elements"

    def test_verify_checkbox_visibility(self):
        if element.check_checkbox_visibility(self.driver):
            pytest.skip()

        element.click_elements(self.driver)
        assert self.driver.current_url == "https://demoqa.com/elements"

    def test_select_checkbox(self):
        element.click_checkbox(self.driver)
        assert self.driver.current_url == "https://demoqa.com/checkbox"
        assert element.check_home_title_visibility(self.driver)

    def test_expand_home(self):
        element.click_expand(self.driver, 0)
        assert element.check_documents_title(self.driver)

    @pytest.mark.xfail(reason='Documents is not visible after you refresh the page')
    def test_preemptive_fail(self):
        self.driver.refresh()
        element.click_expand(self.driver, 0)

    def test_click_documents(self):
        element.click_documents(self.driver)
        element.click_expand(self.driver, 1)
        element.click_expand(self.driver, 1)
        element.click_expand(self.driver, 1)
        assert element.check_result_length(self.driver)
        assert element.verify_names_in_result(self.driver)
