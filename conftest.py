import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://demoqa.com/')
    driver.maximize_window()
    #request.cls.driver = driver

    yield driver
    driver.quit()
