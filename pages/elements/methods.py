from selenium.webdriver.common.by import By
from pages.elements.items import items


class Elements:

    @staticmethod
    def click_checkbox(browser):
        browser.find_element(By.XPATH, items.check_box).click()

    @staticmethod
    def click_expand_home(browser):
        browser.find_element(By.CSS_SELECTOR, items.home_arrow).click()

    @staticmethod
    def click_documents(browser):
        browser.find_elements(By.CSS_SELECTOR, items.documents)[2].click()

    @staticmethod
    def check_documents(browser):
        return browser.find_element(By.ID, items.result).is_displayed()
