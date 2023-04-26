from selenium.webdriver.common.by import By
from elements.elements import Items


class Checkbox:
    items = Items()

    def verify_check_box(self, browser):
        return browser.find_element(By.XPATH, self.items.check_box).is_displayed()

    def click_checkbox(self, browser):
        browser.find_element(By.XPATH, self.items.check_box).click()

    def check_home_visibility(self, browser):
        return browser.find_element(By.XPATH, self.items.home).is_displayed()

    def expand_home(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.items.expand_arrow).click()

    def check_documents_visibility(self, browser):
        return browser.find_element(By.XPATH, self.items.documents).is_displayed()

    def check_downloads_visibility(self, browser):
        return browser.find_element(By.XPATH, self.items.downloads).is_displayed()

    def check_workspace_visibility(self, browser):
        return browser.find_element(By.XPATH, self.items.workspace).is_displayed()

    def check_office_visibility(self, browser):
        return browser.find_element(By.XPATH, self.items.office).is_displayed()

    def click_downloads(self, browser):
        browser.find_element(By.XPATH, self.items.downloads).click()

    def check_result(self, browser):
        return browser.find_element(By.ID, self.items.result).is_displayed()

    def check_downloads_results(self, browser):
        return (browser.find_elements(By.CSS_SELECTOR, self.items.choices)[0].text == "downloads" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[1].text == "wordFile" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[2].text == "excelFile")

    def check_office_results(self, browser):
        return (browser.find_elements(By.CSS_SELECTOR, self.items.choices)[0].text == "office" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[1].text == "public" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[2].text == "private" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[3].text == "classified" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[4].text == "general")

    def check_documents_results(self, browser):
        return (browser.find_elements(By.CSS_SELECTOR, self.items.choices)[0].text == "documents" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[1].text == "workspace" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[2].text == "react" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[3].text == "angular" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[4].text == "veu" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[5].text == "office" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[6].text == "public" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[7].text == "private" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[8].text == "classified" and
                browser.find_elements(By.CSS_SELECTOR, self.items.choices)[9].text == "general")

    def expand_documents(self, browser):
        browser.find_elements(By.CSS_SELECTOR, self.items.expand_arrow)[1].click()

    def click_office(self, browser):
        browser.find_element(By.XPATH, self.items.office).click()

    def click_workspace(self, browser):
        browser.find_element(By.XPATH, self.items.workspace).click()
