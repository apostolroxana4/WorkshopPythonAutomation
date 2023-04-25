import pytest
from selenium.webdriver import Chrome
from driver.driver import Driver


@pytest.fixture(scope='function')
def browser(request):
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get(Driver.URL)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    #driver.quit()
