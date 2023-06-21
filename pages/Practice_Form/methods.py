from selenium.webdriver.common.keys import Keys


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

    @staticmethod
    def is_element_selected(browser, by, path):
        return browser.find_element(by, path).is_selected()

    @staticmethod
    def is_element_enabled(browser, by, path):
        return browser.find_element(by, path).is_enabled()

    @staticmethod
    def is_element_displayed(browser, by, path):
        return browser.find_element(by, path).is_displayed()

    @staticmethod
    def clear_field(browser, by, path):
        browser.find_element(by, path).clear()

    @staticmethod
    def clear_calendar_date(browser, by, path):
        for i in range(len(browser.find_element(by, path).get_attribute('value')) - 1):
            browser.find_element(by, path).send_keys(Keys.BACKSPACE)

    @staticmethod
    def scroll_to_the_bottom(browser):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def submit_form(browser, by, path):
        browser.find_element(by, path).submit()

    @staticmethod
    def maximize_window(browser):
        browser.fullscreen_window()

    @staticmethod
    def close_modal(browser, by, path):
        browser.find_element(by, path).click()

    @staticmethod
    def verify_url(browser, url):
        return browser.current_url == url

    @staticmethod
    def refresh_page(browser):
        browser.refresh()
