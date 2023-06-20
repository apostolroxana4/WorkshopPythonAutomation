from pages.Practice_Form.elements import Elements

class Methods:

    @staticmethod
    def click_element(browser, by, path):
        browser.find_element(by, path).click()

    @staticmethod
    def fill(browser, by, path, word):
        browser.find_element(by, path).send_keys(word)

    @staticmethod
    def validate_field(browser, by, path, word):
        return browser.find_element(by, path).get_attribute("value") == word
