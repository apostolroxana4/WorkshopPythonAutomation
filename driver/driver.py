from selenium.webdriver import Chrome


class Driver:
    URL = "https://demoqa.com/elements"

    @staticmethod
    def open_page():
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.get(Driver.URL)
        driver.maximize_window()
        return driver

