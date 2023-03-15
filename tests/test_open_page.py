import time
# from selenium.webdriver.common.by import By
from driver.driver import Driver


def test_open_heroku_page(browser):
    browser.get(Driver.URL)

    btnDropDrown1 = browser.find_element('xpath', "//a[contains(text(),'A/B Testing')]")
    btnDropDrown1.click()
    time.sleep(10)


def test_reopen_heroku_page(browser):
    browser.get(Driver.URL)

    btnDropDrown2 = browser.find_element('xpath', "//a[contains(text(),'Checkboxes')]")
    btnDropDrown2.click()
    time.sleep(10)


def test_reopen_heroku_page_again(browser):
    browser.get(Driver.URL)

    btnDropDrown3 = browser.find_element('xpath', "//a[contains(text(),'Elemental Selenium')]")
    btnDropDrown3.click()
    time.sleep(10)







