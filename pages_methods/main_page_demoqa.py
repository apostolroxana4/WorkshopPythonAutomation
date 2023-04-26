from selenium.webdriver.common.by import By
from elements.elements import Items


class MainPageDemoQA:
    items = Items()

    def check_elements_is_visible(self, browser):
        return browser.find_elements(By.XPATH, self.items.elements)[1].is_displayed()

    def click_elements(self, browser):
        browser.find_elements(By.XPATH, self.items.elements)[1].click()
