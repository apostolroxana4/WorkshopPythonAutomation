import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


def open_duckduckgo_search(browser):
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'

    browser.get(URL)

    search_input = browser.find_element('id', 'search_form_input_homepage')
    search_input.send_keys(PHRASE + Keys.RETURN)
