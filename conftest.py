import pytest
from selenium.webdriver import Chrome
from driver.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope='class')
def browser(request):
    driver = Chrome()
    driver.get(Driver.URL_demoqa)
    WebDriverWait(driver, 5).until(expected_conditions.number_of_windows_to_be(1))
    driver.execute_script("document.body.style['-webkit-transform'] = \"scale(0.8)\";")
    request.cls.driver = driver

    yield driver
    driver.quit()
