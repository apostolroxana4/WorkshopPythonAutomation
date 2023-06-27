import time
from selenium.webdriver.common.by import By
from gherkin.pages.elements.items import Items


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

    def check_elements_visibility(self, browser):
        return browser.find_elements(By.XPATH, self.items.section_elements)[1].is_displayed()

    def check_checkbox_visibility(self, browser):
        time.sleep(1)
        return browser.find_element(By.XPATH, self.items.subsection_check_box).is_displayed()

    def check_home_title_visibility(self, browser):
        return browser.find_element(By.XPATH, self.items.home_title).is_displayed()

    def check_documents_title(self, browser):
        return browser.find_element(By.XPATH, self.items.documents_title).is_displayed()

    def check_downloads_title(self, browser):
        return browser.find_element(By.XPATH, self.items.downloads_title).is_displayed()

    def check_office_title(self, browser):
        return browser.find_element(By.XPATH, self.items.office).is_displayed()

    def click_expand(self, browser, number):
        arrow = browser.find_elements(By.CSS_SELECTOR, self.items.arrow)
        if not arrow[number].is_selected():
            arrow[number].click()

    def check_result_length(self, browser):
        return (len(browser.find_elements(By.CSS_SELECTOR, self.items.result)) ==
                len(browser.find_elements(By.CSS_SELECTOR, self.items.clicked_checkboxes)))

    def get_name(self, browser):
        elements = (browser.find_elements(By.XPATH,
                                          "//*[name() = 'svg' and contains(@class, 'rct-icon-check')]/ancestor::label"))
        for name in elements:
            self.items.clicked_elements.append(name.get_attribute('for')[10:])
        return self.items.clicked_elements

    def verify_names_in_result(self, browser):
        for result in browser.find_elements(By.CSS_SELECTOR, self.items.result):
            if result.text not in set(self.get_name(browser)):
                return False
        return True
