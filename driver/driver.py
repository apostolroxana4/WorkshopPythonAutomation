import pytest
from selenium.webdriver import Chrome
# Here ww will add the driver
# https://the-internet.herokuapp.com/

#class Driver:
    #URL = 'https://the-internet.herokuapp.com/'


class Driver:
    URL = 'https://demoqa.com/text-box'

    @staticmethod
    def open_browser():
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.get(Driver.URL)
        return driver

