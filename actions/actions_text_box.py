from pages.elements import Elements
from selenium.webdriver.common.by import By


class Actions(Elements):

    def insert_value_for_username_field(self, browser, username):
        browser.find_element(By.ID, self.username).send_keys(username)
        #assert browser.find_element(By.ID, self.username).text == username

    def insert_value_for_email_field(self, browser, email):
        browser.find_element(By.XPATH, self.email).send_keys(email)

    def insert_value_for_current_address(self, browser, current_address):
        browser.find_element(By.CSS_SELECTOR, self.current_address).send_keys(current_address)

    def insert_value_for_permanent_address(self, browser, permanent_address):
        browser.find_element(By.ID, self.permanent_address).send_keys(permanent_address)

    def click_submit_button(self,browser):
        browser.find_element(By.ID, self.submit_button).click()



