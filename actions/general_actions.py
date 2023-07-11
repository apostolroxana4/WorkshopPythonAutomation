class GeneralActions:
    @staticmethod
    def scroll_down(browser):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    @staticmethod
    def maximize_window(browser):
        browser.fullscreen_window()

    @staticmethod
    def check_url(browser, url):
        return browser.current_url == url

    @staticmethod
    def clear_one_field(browser, type_web_element, path_web_element):
        browser.find_element(type_web_element, path_web_element).clear()




