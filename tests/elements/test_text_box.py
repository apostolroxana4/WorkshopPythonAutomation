import pytest
from pages.elements.methods import Elements


@pytest.mark.usefixtures("browser")
class TestTextBox:

    def test_verify_checkbox_visibility(self):
        assert Elements().check_elements(self.driver)

        if Elements().check_checkbox(self.driver):
            pytest.skip()

        Elements().click_elements(self.driver)

    def test_select_checkbox(self):
        assert Elements().check_checkbox(self.driver)
        Elements().click_checkbox(self.driver)

    def test_expand_home(self):
        assert Elements().check_home_title(self.driver)
        Elements().click_expand_home(self.driver)

    @pytest.mark.xfail(reason='Documents is not visible after you refresh the page')
    def test_preemptive_fail(self):
        self.driver.refresh()
        Elements().click_expand_home(self.driver)

    def test_click_documents(self):
        assert Elements().check_documents_title(self.driver)
        Elements().click_documents(self.driver)

    def test_check_results(self):
        assert Elements().check_documents(self.driver)
