from pages.elements import Elements
from selenium.webdriver.common.by import By


class Actions(Elements):
    def elements_from_main_page(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.elements_from_main).click()

    def check_elements_section(self, browser):
        return browser.find_element(By.XPATH, self.elements_item).is_displayed()

    def click_elements_section(self, browser):
        browser.find_element(By.XPATH, self.elements_item).click()

    def check_checkbox_subsection(self, browser):
        return browser.find_element(By.XPATH, self.subsection_checkbox).is_displayed()

    def click_checkbox_subsection(self, browser):
        browser.find_element(By.XPATH, self.subsection_checkbox).click()

    def check_home_item(self, browser):
        return browser.find_element(By.XPATH, self.home_item).is_displayed()

    def expand_home_item(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.expand_home).click()

    def check_downloads_item(self, browser):
        return browser.find_element(By.XPATH, self.downloads_item).is_displayed()

    def click_downloads_item(self, browser):
        browser.find_element(By.XPATH, self.downloads_item).click()

    def check_downloads_word_file(self, browser):
        return "wordFile" in browser.find_element(By.ID, self.downloads_word).text

    def expand_documents_item(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.expand_documents).click()

    def check_documents_item(self, browser):
        return browser.find_element(By.XPATH, self.documents_item).is_displayed()

    def click_documents_item(self, browser):
        browser.find_element(By.XPATH, self.documents_item).click()

    def check_office(self, browser):
        return browser.find_element(By.XPATH, self.office_item).is_displayed()

    def click_office(self, browser):
        browser.find_element(By.XPATH, self.office_item).click()

    def check_workspace(self, browser):
        return browser.find_element(By.XPATH, self.workspace_item).is_displayed()

    def click_workspace(self, browser):
        browser.find_element(By.XPATH, self.workspace_item).click()

    def check_documents_office_public(self, browser):
        return "public" in browser.find_element(By.ID, self.documents_office_result).text

    def check_documents_workspace_angular(self, browser):
        return "angular" in browser.find_element(By.ID, self.documents_workspace_result).text

    def username_field_visibility(self, browser):
        return browser.find_element(By.XPATH, self.username_field).is_displayed()

    def insert_value_for_username_field(self, browser, username):
        browser.find_element(By.ID, self.username).send_keys(username)

    def email_field_visibility(self, browser):
        return browser.find_element(By.XPATH, self.email_field).is_displayed()

    def insert_value_for_email_field(self, browser, email):
        browser.find_element(By.XPATH, self.email).send_keys(email)

    def current_address_visibility(self, browser):
        return browser.find_element(By.XPATH, self.current_address_field).is_displayed()

    def insert_value_for_current_address(self, browser, current_address):
        browser.find_element(By.CSS_SELECTOR, self.current_address).send_keys(current_address)

    def permanent_address_visibility(self, browser):
        browser.find_element(By.XPATH, self.permanent_address_field).is_displayed()

    def insert_value_for_permanent_address(self, browser, permanent_address):
        browser.find_element(By.ID, self.permanent_address).send_keys(permanent_address)

    def click_submit_button(self, browser):
        browser.find_element(By.ID, self.submit_button).click()



