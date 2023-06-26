class GeneralMethods:

    @staticmethod
    def click_element(browser, by, path):
        browser.find_element(by, path).click()

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
    def scroll_to_the_bottom(browser):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def maximize_window(browser):
        browser.fullscreen_window()

    @staticmethod
    def verify_url(browser, url):
        return browser.current_url == url

    @staticmethod
    def refresh_page(browser):
        browser.refresh()
