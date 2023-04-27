from selenium.webdriver.common.by import By
from elements.elements.check_box import CheckBoxItems


class Checkbox:
    CheckBoxItems = CheckBoxItems()

    def verify_check_box(self, browser):
        return browser.find_element(By.XPATH, self.CheckBoxItems.check_box).is_displayed()

    def click_checkbox(self, browser):
        browser.find_element(By.XPATH, self.CheckBoxItems.check_box).click()

    def check_home_visibility(self, browser):
        return browser.find_element(By.XPATH, self.CheckBoxItems.home).is_displayed()

    def expand_home(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.CheckBoxItems.expand_arrow).click()

    def check_documents_visibility(self, browser):
        return browser.find_element(By.XPATH, self.CheckBoxItems.documents).is_displayed()

    def check_downloads_visibility(self, browser):
        return browser.find_element(By.XPATH, self.CheckBoxItems.downloads).is_displayed()

    def check_workspace_visibility(self, browser):
        return browser.find_element(By.XPATH, self.CheckBoxItems.workspace).is_displayed()

    def check_office_visibility(self, browser):
        return browser.find_element(By.XPATH, self.CheckBoxItems.office).is_displayed()

    def click_downloads(self, browser):
        browser.find_element(By.XPATH, self.CheckBoxItems.downloads).click()

    def check_result(self, browser):
        return browser.find_element(By.ID, self.CheckBoxItems.result).is_displayed()

    def check_downloads_results(self, browser):
        return (browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[0].text == "downloads" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[1].text == "wordFile" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[2].text == "excelFile")

    def check_office_results(self, browser):
        return (browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[0].text == "office" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[1].text == "public" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[2].text == "private" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[3].text == "classified" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[4].text == "general")

    def check_documents_results(self, browser):
        return (browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[0].text == "documents" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[1].text == "workspace" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[2].text == "react" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[3].text == "angular" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[4].text == "veu" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[5].text == "office" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[6].text == "public" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[7].text == "private" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[8].text == "classified" and
                browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.choices)[9].text == "general")

    def expand_documents(self, browser):
        browser.find_elements(By.CSS_SELECTOR, self.CheckBoxItems.expand_arrow)[1].click()

    def click_office(self, browser):
        browser.find_element(By.XPATH, self.CheckBoxItems.office).click()

    def click_workspace(self, browser):
        browser.find_element(By.XPATH, self.CheckBoxItems.workspace).click()
