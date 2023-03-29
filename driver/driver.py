# Here we will add the driver
# https://the-internet.herokuapp.com/
import pytest
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By


class Driver:
    # URL_HEROKU = 'https://the-internet.herokuapp.com/'
    URL = "https://demoqa.com/elements"

    @staticmethod
    def open_page():
        driver = Chrome()
        driver.implicitly_wait(10)
        driver.get(Driver.URL)
        driver.maximize_window()
        return driver

