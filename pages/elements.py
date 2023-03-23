from selenium.webdriver.common.by import By


class Elements:
    class Items:
        check_box = "//*[contains(text(),'Check Box')]"
        home_arrow = "svg[class='rct-icon rct-icon-expand-close']"
        documents = "span[class='rct-title']"
        result = 'result'

    items = Items()

    def click_checkbox(self, browser):
        browser.find_element(By.XPATH, self.items.check_box).click()

    def click_expand_home(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.items.home_arrow).click()

    def click_documents(self, browser):
        browser.find_elements(By.CSS_SELECTOR, self.items.documents)[2].click()

    def check_documents(self, browser):
        return browser.find_element(By.ID, self.items.result)
