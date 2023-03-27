import time
from selenium.webdriver.common.by import By
from driver.driver import Driver

def click_and_go_back(element, browser):
    element.click()
    time.sleep(3)
    browser.back()

def test_open_page(browser):
    browser.get(Driver.URL_hekokuapp)

    element = browser.find_element(By.LINK_TEXT, 'Shadow DOM') #by the text Shadow DOM
    click_and_go_back(element, browser)

    element = browser.find_element(By.CSS_SELECTOR, 'a[href="/key_presses"]') #by the anchor with a specific attribute
    click_and_go_back(element, browser)
    element.send_keys()

    element = browser.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[18]/a') #xpath
    click_and_go_back(element, browser)

    element = browser.find_element(By.CSS_SELECTOR, "li:nth-child(9) a") #the anchor in the 9th li
    click_and_go_back(element, browser)

    element = browser.find_element(By.CSS_SELECTOR, "h2 + ul > li > a") #select the anchor from the first li in the ul that's after h2
    click_and_go_back(element, browser)