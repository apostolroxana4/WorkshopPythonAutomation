import pytest

from pages_methods.elements.radio_button import RadioButton
from pages_methods.main_page_demoqa import MainPageDemoQA


@pytest.mark.usefixtures
class TestRadioButton:

    def test_select_elements(self):
        assert MainPageDemoQA().check_elements_is_visible(self.driver)
        MainPageDemoQA().click_elements(self.driver)

    def test_select_radio_button(self):
        assert RadioButton().check_radio_button(self.driver)
        RadioButton().click_radio_button(self.driver)

    def test_yes_radio(self):
        assert RadioButton().check_yes_radio(self.driver)
        RadioButton().click_yes_radio(self.driver)

    def test_impressive_radio(self):
        assert RadioButton().check_impressive_radio(self.driver)
        RadioButton().click_impressive_radio(self.driver)

    def test_teardown(self):
        self.driver.quit()
