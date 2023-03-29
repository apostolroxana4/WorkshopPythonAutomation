from pages.elements import Elements
from selenium.webdriver.common.by import By


class Actions(Elements):

    def insert_value_for_username_field(self,browser):
        browser.find_element(By.ID,self.username_field_after_id).send_keys("user")

    def insert_value_for_email_field(self,browser):
        browser.find_element(By.XPATH,self.email_field_after_xpath).send_keys("user@yahoo.com")

    def insert_value_for_current_address(self,browser):
        browser.find_element(By.CSS_SELECTOR, self.current_address_field_after_css_selector).send_keys("Bd.Chimiei")

    def insert_value_for_permanent_address(self,browser):
        browser.find_element(By.ID, self.permanent_address_field_after_id).send_keys("Bd. Stefan cel Mare")

    def click_submit_button(self,browser):
        browser.find_element(By.ID, self.submit_button_after_id).click()

