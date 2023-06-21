import pytest
from selenium.webdriver import Chrome
from driver.driver import Driver


@pytest.fixture(scope="class")
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get(Driver.URL_demo)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()
