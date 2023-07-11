from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.items import ItemsFormsSection
from selenium.webdriver.common.by import By
from actions.general_actions import GeneralActions


class Actions(ItemsFormsSection):
    general_actions = GeneralActions()

    def click_forms_section(self, browser):
        wait_value = WebDriverWait(browser, 3)
        wait_value.until(
            expected_conditions.presence_of_element_located((By.XPATH, self.forms_from_main))).click()

    def check_subsection_practice_form(self, browser):
        return browser.find_element(By.XPATH, self.forms_subsection).is_displayed()

    def click_subsection_practice_form(self, browser):
        WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH, self.forms_subsection))).click()

    def first_name_field_visibility(self, browser):
        return browser.find_element(By.ID, self.first_name_item).is_displayed()

    def enter_first_name(self, browser):
        browser.find_element(By.ID, self.first_name_item).send_keys(self.first_name_value)

    def enter_wrong_last_name(self, browser):
        browser.find_element(By.ID, self.last_name_item).send_keys(self.last_name_value_wrong)
        self.general_actions.clear_one_field(browser, By.ID, self.last_name_item)

    def enter_correctly_last_name(self, browser):
        browser.find_element(By.ID, self.last_name_item).send_keys(self.last_name_value_correctly)

    def email_visibility(self, browser):
        return browser.find_element(By.ID, self.email_item).is_displayed()

    def enter_email(self, browser):
        browser.find_element(By.ID, self.email_item).send_keys(self.email_value)

    def select_gender_female(self, browser):
        browser.find_element(By.XPATH, self.gender_female_radio_button).click()



