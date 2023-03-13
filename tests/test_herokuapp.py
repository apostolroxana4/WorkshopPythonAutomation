import time
from selenium.webdriver.common.by import By
from driver.driver import Driver

def test_open_herokuapp_page(browser):
    browser.get(Driver.URL)

    buttondropdown = browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a') #relative
    buttondropdown.click()
    time.sleep(5)

    buttoncontextmenu = browser.find_element(by=By.XPATH, value='//*[@id="content"]/ul/li[7]/a')
    buttoncontextmenu.click()
    time.sleep(5)

    buttondragdrop = browser.find_element(by=By.XPATH, value='//*[@id="content"]/ul/li[10]/a')
    buttondragdrop.click()
    time.sleep(5)

    buttonforgotpassword = browser.find_element(by=By.XPATH, value='//*[@id="content"]/ul/li[20]/a')
    buttonforgotpassword.click()
    time.sleep(5)



















