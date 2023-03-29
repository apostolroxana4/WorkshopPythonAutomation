from selenium.webdriver.common.by import By
from driver.driver import Driver


class ElementsFromTextBox(Driver):
    def __init__(self, driver):
        self.driver = driver

    def click_test_box(self):
        text_box_field = self.driver.find_element(By.XPATH, "//span[contains(text(),'Text Box')]")
        text_box_field.click()

    def insert_full_name(self):
        full_name = self.driver.find_element(By.XPATH, "//input[@id='userName']")
        full_name.send_key('Petrica')

    def insert_email(self):
        email = self.driver.find_element(By.XPATH, "//input[@id='userEmail']")
        email.send_key('aaaaa@gmail.com')

    def insert_current_address(self):
        current_address = self. driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
        current_address.send_key('str. Sorcova, nr.5')

    def insert_permanent_address(self):
        permanent_address = self.driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
        permanent_address.send_key('str. Sorvoca, nr.10')

    def click_submit_button(self):
        submit_button = self.driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button.click()







