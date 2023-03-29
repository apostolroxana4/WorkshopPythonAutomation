import time

import pytest
from pages_methods.elements.radio_button import RadioButton
from pages_methods.main_page_demoqa import MainPageDemoQA
from driver.driver import Driver
from selenium.webdriver import Chrome


class TestRadioButton:

    @staticmethod
    def browser():
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.get(Driver.URL)
        return driver

    browser = browser()

    def test_select_elements(self):
        assert MainPageDemoQA().check_elements_is_visible(self.browser)
        MainPageDemoQA().click_elements(self.browser)

    def test_select_radio_button(self):
        assert RadioButton().check_radio_button(self.browser)
        RadioButton().click_radio_button(self.browser)

    def test_yes_radio(self):
        assert RadioButton().check_yes_radio(self.browser)
        RadioButton().click_yes_radio(self.browser)

    def test_impressive_radio(self):
        assert RadioButton().check_impressive_radio(self.browser)
        RadioButton().click_impressive_radio(self.browser)

    def test_teardown(self):
        self.browser.quit()
