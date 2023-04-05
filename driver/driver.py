from selenium.webdriver import Chrome


class Driver:
    URL = 'https://demoqa.com/text-box'

    @staticmethod
    def open_browser():
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.get(Driver.URL)
        driver.maximize_window()
        return driver

