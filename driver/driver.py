from selenium.webdriver import Chrome


class Driver:
    URL_textbox = 'https://demoqa.com/text-box'
    URL_demo = 'https://demoqa.com'

    @staticmethod
    def open_browser():
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.get(Driver.URL_textbox)
        driver.maximize_window()
        return driver
