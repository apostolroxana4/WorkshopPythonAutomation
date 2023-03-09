import time

from selenium.webdriver.common.by import By

from driver.driver import Driver

def test_open_page(browser):
    browser.get(Driver.URL)

    # element = browser.find_element(By.LINK_TEXT, 'Shadow DOM') #by the text Shadow DOM
    # element = browser.find_element(By.CSS_SELECTOR, 'a[href="/key_presses"]') #by the anchor with a specific attribute
    # element = browser.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[18]/a') #xpath
    element = browser.find_element(By.CSS_SELECTOR, "li:nth-child(9) a") #the anchor in the 9th li
    element.click()


    time.sleep(5)