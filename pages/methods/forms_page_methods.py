from selenium.webdriver.common.by import By
from pages.elements.forms_page import FormsPage


class FormsPageMethods:
    def verify_first_name(self, browser, first_name):
        first_name_value = browser.find_element(By.ID, FormsPage.firstName_input).get_property("value")
        assert first_name_value == first_name

    def enter_first_name(self, browser, first_name):
        browser.find_element(By.ID, FormsPage.firstName_input).send_keys(first_name)

    def enter_last_name(self, browser, last_name):
        browser.find_element(By.ID, FormsPage.lastName_input).send_keys(last_name)

    def enter_email(self, browser, email):
        browser.find_element(By.ID, FormsPage.userEmail_input).send_keys(email)

    def select_gender(self, browser, gender):
        browser.find_element(By.ID, FormsPage.currentAddress_input).click() #in order to close any pop
        if gender.lower() == 'male':
            browser.find_element(By.XPATH, FormsPage.gender_radio_male).click()
        elif gender.lower() == 'female':
            browser.find_element(By.XPATH, FormsPage.gender_radio_female).click()
        else:
            browser.find_element(By.XPATH, FormsPage.gender_radio_other).click()

    def enter_mobile(self, browser, mobileNumber):
        browser.find_element(By.ID, FormsPage.userNumber_input).send_keys(mobileNumber)

    def select_date_of_birth(self, browser, date):
        browser.find_element(By.ID, FormsPage.dateOfBirthInput_input).send_keys(date)
