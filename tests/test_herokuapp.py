import time
from selenium.webdriver.common.by import By
from driver.driver import Driver
from pages import elements

def test_open_herokuapp_page(browser):
    browser.get(Driver.URL)

    buttondropdown = browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a') #relative
    buttondropdown.click()
    time.sleep(5)
    browser.back()

    buttoncontextmenu = browser.find_element(by=By.XPATH, value='//*[@id="content"]/ul/li[7]/a')
    buttoncontextmenu.click()
    time.sleep(5)
    browser.back()

    buttondragdrop = browser.find_element(by=By.XPATH, value='//*[@id="content"]/ul/li[10]/a')
    buttondragdrop.click()
    time.sleep(5)
    browser.back()

    buttonforgotpassword = browser.find_element(by=By.XPATH, value='//*[@id="content"]/ul/li[20]/a')
    buttonforgotpassword.click()
    time.sleep(5)
    browser.back()

    drag_and_drop_with_css_selector = browser.find_element(By.CSS_SELECTOR, 'li:nth-child(10) a')
    drag_and_drop_with_css_selector.click()
    time.sleep(5)
    browser.back()




















