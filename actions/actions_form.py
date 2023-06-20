from pages.items import ItemsFormsSection
from selenium.webdriver.common.by import By


class Actions(ItemsFormsSection):
    def forms_from_main_page(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.forms_from_main).click()

    def check_forms_section(self, browser):
        return browser.find_element(By.XPATH, self.forms_section).is_displayed()

    def click_forms_section(self, browser):
        browser.find_element(By.XPATH, self.forms_section).click()

    def check_subsection_practice_form(self, browser):
        return browser.find_element(By.XPATH, self.subsection_practice_form).is_displayed()

    def click_subsection_practice_form(self, browser):
        browser.find_element(By.XPATH, self.subsection_practice_form).click()

    def first_name_field_visibility(self, browser):
        return browser.find_element(By.ID, self.first_name_item).is_displayed()

    def enter_first_name(self, browser):
        browser.find_element(By.ID, self.first_name_item).send_keys("Jack")

    def enter_wrong_last_name(self, browser):
        element_wrong_last_name = browser.find_element(By.ID, self.last_name_item).send_keys("Taylor")
        element_wrong_last_name.clear()

    def enter_correctly_last_name(self, browser):
        browser.find_element(By.ID, self.last_name_item).send_keys("Maylor")
        assert browser.find_element(By.ID, self.last_name_item).get_attribute("value") == "Maylor"

    def email_visibility(self, browser):
        return browser.find_element(By.ID, self.email_item).is_displayed()

    def enter_email(self, browser):
        browser.find_element(By.ID, self.email_item).send_keys("jackmaylor@gmail.com")

    def select_gender_female(self, browser):
        radio_options = browser.find_element(By.XPATH, self.radio_button_options)
        radio_options.get(0).click()
        assert browser.find_element(By.ID, self.female_item).is_selected()
        assert not browser.find_element(By.ID, self.male_item).is_selected()
        assert not browser.find_element(By.ID, self.other_item).is_selected()

