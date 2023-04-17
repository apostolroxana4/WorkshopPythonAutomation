import pytest
from selenium.webdriver import Chrome
from driver.driver import Driver


@pytest.mark.usefixtures(scope="class")
def setup():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get(Driver.URL)
    driver.maximize_window()
    return driver
