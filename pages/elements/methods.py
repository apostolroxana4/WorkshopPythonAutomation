import time
from selenium.webdriver.common.by import By
from pages.elements.items import Items


class Elements:
    items = Items()

    def click_main_page_elements(self, browser):
        browser.find_elements(By.CSS_SELECTOR, self.items.main_page_elements)[0].click()

    def click_elements(self, browser):
        browser.find_elements(By.XPATH, self.items.section_elements)[1].click()

    def click_checkbox(self, browser):
        browser.find_element(By.XPATH, self.items.subsection_check_box).click()

    def click_documents(self, browser):
        browser.find_elements(By.CSS_SELECTOR, self.items.documents)[2].click()

    def click_downloads(self, browser):
        browser.find_element(By.XPATH, self.items.downloads_title).click()

    def click_office(self, browser):
        browser.find_element(By.XPATH, self.items.office).click()

    def click_workspace(self, browser):
        browser.find_element(By.XPATH, self.items.workspace).click()

    def click_expand_home(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.items.home_arrow).click()

    def click_expand_documents(self, browser):
        browser.find_elements(By.CSS_SELECTOR, self.items.documents_arrow)[1].click()

    def check_elements(self, browser):
        return browser.find_elements(By.XPATH, self.items.section_elements)[1].is_displayed()

    def check_checkbox(self, browser):
        time.sleep(1)
        return browser.find_element(By.XPATH, self.items.subsection_check_box).is_displayed()

    def check_home_title(self, browser):
        return browser.find_element(By.XPATH, self.items.home_title).is_displayed()

    def check_documents_title(self, browser):
        return browser.find_element(By.XPATH, self.items.documents_title).is_displayed()

    def check_documents_result(self, browser):
        return (browser.find_element(By.ID, self.items.result).is_displayed() and
                browser.find_elements(By.CSS_SELECTOR, self.items.documents_results)[-1].text == 'general')

    def check_downloads_title(self, browser):
        return browser.find_element(By.XPATH, self.items.downloads_title).is_displayed()

    def check_downloads_result(self, browser):
        return (browser.find_element(By.ID, self.items.result).is_displayed() and
                browser.find_elements(By.CSS_SELECTOR, self.items.downloads_result)[2].text == 'excelFile')

    def check_office_title(self, browser):
        return browser.find_element(By.XPATH, self.items.office).is_displayed()

    def check_office_results(self, browser):
        return (browser.find_element(By.ID, self.items.result).is_displayed() and
                browser.find_elements(By.CSS_SELECTOR, self.items.office_result)[-1].text == 'general')

    def check_workspace_results(self, browser):
        return (browser.find_element(By.ID, self.items.result).is_displayed() and
                browser.find_elements(By.CSS_SELECTOR, self.items.workspace_result)[-1].text == 'veu')