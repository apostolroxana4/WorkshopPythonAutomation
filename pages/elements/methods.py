from selenium.webdriver.common.by import By
from pages.elements.items import Items


class Elements:
    items = Items()

    def check_elements(self, browser):
        return browser.find_elements(By.XPATH, self.items.section_elements)[1].is_displayed()

    def click_elements(self, browser):
        browser.find_elementss(By.XPATH, self.items.section_elements)[1].click()

    def check_checkbox(self, browser):
        return browser.find_element(By.XPATH, self.items.subsection_check_box).is_displayed()

    def click_checkbox(self, browser):
        browser.find_element(By.XPATH, self.items.subsection_check_box).click()

    def check_home_title(self, browser):
        return browser.find_element(By.XPATH, self.items.home_title).is_displayed()

    def click_expand_home(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.items.home_arrow).click()

    def check_documents_title(self, browser):
        return browser.find_element(By.XPATH, self.items.documents_title).is_displayed()

    def click_documents(self, browser):
        browser.find_elements(By.CSS_SELECTOR, self.items.documents)[2].click()

    def check_documents(self, browser):
        return browser.find_element(By.ID, self.items.result).is_displayed()
