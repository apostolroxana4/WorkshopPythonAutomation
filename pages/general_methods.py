class GeneralMethods:
    def __init__(self, browser):
        self.browser = browser

    def click_element(self, by, path):
        self.browser.find_element(by, path).click()

    def is_element_selected(self, by, path):
        return self.browser.find_element(by, path).is_selected()

    def is_element_enabled(self, by, path):
        return self.browser.find_element(by, path).is_enabled()

    def is_element_displayed(self, by, path):
        return self.browser.find_element(by, path).is_displayed()

    def scroll_to_the_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def maximize_window(self):
        self.browser.fullscreen_window()

    def verify_url(self, url):
        return self.browser.current_url == url

    def refresh_page(self):
        self.browser.refresh()
