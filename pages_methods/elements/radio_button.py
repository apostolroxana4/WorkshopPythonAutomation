from selenium.webdriver.common.by import By
from elements.elements.radio_button import RadioButtonItems


class RadioButton:
    RadioButtonItems = RadioButtonItems()

    def check_radio_button(self, browser):
        return browser.find_element(By.XPATH, self.RadioButtonItems.radio_button).is_displayed()

    def click_radio_button(self, browser):
        browser.find_element(By.XPATH, self.RadioButtonItems.radio_button).click()

    def check_yes_radio(self, browser):
        return browser.find_element(By.XPATH, self.RadioButtonItems.yes_radio).is_displayed()

    def click_yes_radio(self, browser):
        browser.find_element(By.XPATH, self.RadioButtonItems.yes_radio).click()

    def check_impressive_radio(self, browser):
        return browser.find_element(By.XPATH, self.RadioButtonItems.impressive_radio).is_displayed()

    def click_impressive_radio(self, browser):
        browser.find_element(By.XPATH, self.RadioButtonItems.impressive_radio).click()
