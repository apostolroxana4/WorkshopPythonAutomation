from pages.elements.elements_text_box import ElementFromTextBox
from selenium.webdriver.common.by import By


class ElementsBoxPage:
    elements = ElementFromTextBox()

    @staticmethod
    def check_color(color, orginal_color):
        return color == orginal_color

    def click_test_box(self, browser):
        browser.find_element(By.XPATH, self.elements.text_box_field).click()

    def text_box_text_visibility(self, browser):
        return browser.find_element(By.XPATH, self.elements.text_box_field).is_displayed()

    def full_name_field_visibility(self, browser):
        return browser.find_element(By.XPATH, self.elements.full_name_field).is_displayed()

    def insert_full_name(self, browser):
        browser.find_element(By.XPATH, self.elements.full_name).send_keys("Jose Armando")

    def email_field_visibility(self, browser):
        return browser.find_element(By.XPATH, self.elements.email_field).is_displayed()

    def insert_email(self, browser):
        browser.find_element(By.XPATH, self.elements.email).send_keys('aaaaa@gmail.com')

    def insert_incorrect_email(self, browser):
        browser.find_element(By.XPATH, self.elements.email).send_keys('aaaaa')

    def current_address_field_visibility(self, browser):
        return browser.find_element(By.XPATH, self.elements.current_address_field).is_displayed()

    def insert_current_address(self, browser):
        browser.find_element(By.XPATH, self.elements.current_address).send_keys('str.Sorcova, nr.5')

    def permanent_address_field_visibility(self, browser):
        return browser.find_element(By.XPATH, self.elements.permanent_address_field).is_displayed()

    def insert_permanent_address(self, browser):
        browser.find_element(By.XPATH, self.elements.permanent_address).send_keys('str.Sorvoca, nr.10')

    def click_submit_button(self, browser):
        browser.find_element(By.XPATH, self.elements.submit_button).click()

    def check_submit_content(self, browser):
        return browser.find_element(By.XPATH, self.elements.submit_content).is_displayed()

