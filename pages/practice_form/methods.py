from selenium.webdriver.common.keys import Keys
from pages.general_methods import GeneralMethods


class FormMethods(GeneralMethods):

    @staticmethod
    def fill(browser, by, path, word):
        browser.find_element(by, path).send_keys(word)

    @staticmethod
    def validate_field(browser, by, path, word):
        return browser.find_element(by, path).get_attribute("value") == word

    @staticmethod
    def clear_field(browser, by, path):
        browser.find_element(by, path).clear()

    @staticmethod
    def clear_calendar_date(browser, by, path):
        for i in range(len(browser.find_element(by, path).get_attribute('value')) - 1):
            browser.find_element(by, path).send_keys(Keys.BACKSPACE)

    @staticmethod
    def submit_form(browser, by, path):
        browser.find_element(by, path).submit()

    @staticmethod
    def close_modal(browser, by, path):
        browser.find_element(by, path).click()

    def fill_and_clear_wrong_value(self, browser, by, path, word):
        self.click_element(browser, by, path)
        self.fill(browser, by, path, word)
        self.clear_field(browser, by, path)
