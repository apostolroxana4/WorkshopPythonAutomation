import pytest
from selenium.webdriver import Chrome
from driver.driver import Driver


@pytest.fixture(scope="class")
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    #driver.get(Driver.URL_textbox)
    yield driver
    driver.quit()
