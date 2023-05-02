import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='function')
def browser(request):
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/')
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()
