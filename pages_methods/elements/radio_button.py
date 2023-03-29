from selenium.webdriver.common.by import By
from elements.elements import items


class RadioButton:

    @staticmethod
    def check_radio_button(browser):
        return browser.find_element(By.XPATH, items.radio_button).is_displayed()

    @staticmethod
    def click_radio_button(browser):
        browser.find_element(By.XPATH, items.radio_button).click()

    @staticmethod
    def check_yes_radio(browser):
        return browser.find_element(By.XPATH, items.yes_radio).is_displayed()

    @staticmethod
    def click_yes_radio(browser):
        browser.find_element(By.XPATH, items.yes_radio).click()

    @staticmethod
    def check_impressive_radio(browser):
        return browser.find_element(By.XPATH, items.impressive_radio).is_displayed()

    @staticmethod
    def click_impressive_radio(browser):
        browser.find_element(By.XPATH, items.impressive_radio).click()
