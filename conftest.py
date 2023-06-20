import pytest
from selenium.webdriver import Chrome
from driver.driver import Driver


@pytest.fixture(scope='module')
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get(Driver.URL_demoqa)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    yield driver
    driver.quit()
