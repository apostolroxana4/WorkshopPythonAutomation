import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

def test_open_duckduckge(browser):
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'
    browser.get(URL)

    search_input = browser.find_element('id', 'search_form_input_homepage')
    search_input.send_keys(PHRASE + Keys.RETURN)

