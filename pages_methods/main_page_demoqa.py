from selenium.webdriver.common.by import By
from elements.elements import items


class MainPageDemoQA:

    @staticmethod
    def check_elements_is_visible(browser):
        return browser.find_element(By.XPATH, items.elements).is_displayed()

    @staticmethod
    def click_elements(browser):
        browser.find_element(By.XPATH, items.elements).click()
