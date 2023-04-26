from selenium.webdriver.common.by import By
from elements.elements import Items


class RadioButton:
    items = Items()

    def check_radio_button(self, browser):
        return browser.find_element(By.XPATH, self.items.radio_button).is_displayed()

    def click_radio_button(self, browser):
        browser.find_element(By.XPATH, self.items.radio_button).click()

    def check_yes_radio(self, browser):
        return browser.find_element(By.XPATH, self.items.yes_radio).is_displayed()

    def click_yes_radio(self, browser):
        browser.find_element(By.XPATH, self.items.yes_radio).click()

    def check_impressive_radio(self, browser):
        return browser.find_element(By.XPATH, self.items.impressive_radio).is_displayed()

    def click_impressive_radio(self, browser):
        browser.find_element(By.XPATH, self.items.impressive_radio).click()
