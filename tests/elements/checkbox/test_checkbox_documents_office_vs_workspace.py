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
        assert Checkbox().check_documents_visibility(self.driver)

    def test_expand_documents(self):
        Checkbox().expand_documents(self.driver)
        time.sleep(1)
        assert Checkbox().check_workspace_visibility(self.driver)
        assert Checkbox().check_office_visibility(self.driver)

    def test_click_office(self):
        Checkbox().click_office(self.driver)
        assert Checkbox().check_result(self.driver)

    def test_check_results(self):
        assert Checkbox().check_office_results(self.driver)
        time.sleep(1)

    def test_click_workspace(self):
        Checkbox().click_workspace(self.driver)
        assert Checkbox().check_result(self.driver)

    def test_check_final_results(self):
        assert Checkbox().check_documents_results(self.driver)
