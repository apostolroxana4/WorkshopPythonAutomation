import time
from selenium.webdriver.common.by import By


class Interactions:

    def scroll_down(self, browser):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1) #remove time sleep if I don't need it

    def scroll_up(self, browser):
        browser.execute_script("window.scrollTo(0,0)")
        time.sleep(1)

    def click_dropdown_interactions(self, browser):
        dropdown_interactions = browser.find_element(By.XPATH, "//*[contains(text(),'Interactions')]") #move it as a variabile
        #need to be reusable
        dropdown_interactions.click()

    def click_selectable(self, browser):
        selectable = browser.find_element(By.XPATH, "//*[contains(text(),'Selectable')]")
        selectable.click()

    def click_selectable_list_element(self, browser):
        first_box = browser.find_element(By.CSS_SELECTOR, "ul[id='verticalListContainer'] li:nth-child(1)")
        first_box.click()
        third_box = browser.find_element(By.CSS_SELECTOR, "ul[id='verticalListContainer'] li:nth-child(3)")
        third_box.click()

    def go_back(self, browser):
        browser.back()