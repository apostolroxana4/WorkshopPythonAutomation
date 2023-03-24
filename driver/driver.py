from selenium.webdriver import Chrome


class Driver:
    URL_hekokuapp = "https://the-internet.herokuapp.com/"
    URL_demoqa = "https://demoqa.com/elements"

    @staticmethod
    def browser_initialization():
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.get(Driver.URL_demoqa)
        return driver
