from selenium.webdriver.common.keys import Keys
from pages.general_methods import GeneralMethods
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.practice_form.elements import Elements


class FormMethods(GeneralMethods):
    def __init__(self, browser):
        super().__init__(browser)

    def fill(self, by, path, word):
        self.browser.find_element(by, path).send_keys(word)

    def validate_field(self, by, path, word):
        return self.browser.find_element(by, path).get_attribute("value") == word

    def clear_field(self, by, path):
        self.browser.find_element(by, path).clear()

    def clear_calendar_date(self, by, path):
        for i in range(len(self.browser.find_element(by, path).get_attribute('value')) - 1):
            self.browser.find_element(by, path).send_keys(Keys.BACKSPACE)

    def submit_form(self, by, path):
        self.browser.find_element(by, path).submit()

    def close_modal(self, by, path):
        self.browser.find_element(by, path).click()

    def fill_and_clear_wrong_value(self, by, path, word):
        self.click_element(by, path)
        self.fill(by, path, word)
        self.clear_field(by, path)

    def validate_after_refresh(self, by, path1, path2):
        return (self.browser.find_element(by, path1).get_attribute("value") == ''
                and not self.browser.find_element(by, path2).is_selected())

    def insert_wrong_number(self, by, path):
        self.click_element(by, path)
        self.fill(by, path, 'wrong number')
        self.clear_field(by, path)

    def wait_for_refresh(self, by, path):
        WebDriverWait(self.browser, 10).until_not(expected_conditions.element_to_be_clickable((by, path)))

    def wait_for_modal(self, by, path):
        WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located((by, path)))

    def pick_date(self, by, path, by_date, month_year=Elements.date_month_year):
        self.month_year = self.browser.find_element(by_date, month_year).text
        self.browser.find_element(by, path).click()

    def convert_month(self):
        self.month = self.month_year.split()[0]
        self.year = self.month_year.split()[1]

        for key in Elements.month_dict:
            if self.month == key:
                self.month = Elements.month_dict[key]

        self.month_year = self.month + self.year

    def validate_date(self, by, path):
        self.convert_month()
        return self.browser.find_element(by, path).get_attribute('value') == "13 " + self.month_year
