import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

@pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestSelectMenu:

    def test_click_first_dropdown(self):
        self.driver.find_elements(By.CSS_SELECTOR, "div[class='card mt-4 top-card']")[0].click()
        self.driver.find_elements(By.XPATH, "//*[contains(text(),'Elements')]")[1].click()

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[contains(text(),'Widgets')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[contains(text(),'Select Menu')]").click()
        time.sleep(1)
        self.driver.find_elements(By.CSS_SELECTOR, "div[class=' css-yk16xz-control']")[0].click()
        self.driver.find_elements(By.CSS_SELECTOR, "div[class=' css-1s9izoc']")[1].click()

    def test_click_second_dropdown(self):
        self.driver.find_elements(By.CSS_SELECTOR, "div[class=' css-2b097c-container']")[1].click()
        self.driver.find_elements(By.CSS_SELECTOR, "div[class=' css-1s9izoc']")[0].click()

    def test_click_third_dropdown(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "option[value ='7']").click()

    def test_click_fourth_dropdown(self):
        time.sleep(1)
        self.driver.find_elements(By.CSS_SELECTOR, "div[class=' css-2b097c-container']")[2].click()
        self.driver.find_element(By.ID, 'react-select-4-input').send_keys('bl', Keys.ENTER)
        self.driver.find_element(By.ID, 'react-select-4-input').send_keys('bl', Keys.ENTER)


    def test_click_fifth_dropdown(self):
        ActionChains(self.driver).key_down(Keys.CONTROL)
        self.driver.find_element(By.CSS_SELECTOR, "option[value ='volvo']").click()
        self.driver.find_element(By.CSS_SELECTOR, "option[value ='audi']").click()
        ActionChains(self.driver).key_up(Keys.CONTROL)
        time.sleep(3)