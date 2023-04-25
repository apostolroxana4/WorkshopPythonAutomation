from selenium.webdriver.common.by import By


class SideMenuMethods:
    def click_on_submenu_item(self, browser, name):
        item = browser.find_element(By.XPATH, "//*[@class='menu-list']//*[@class='text'][contains(text(), '" + name + "')]")
        browser.execute_script("arguments[0].scrollIntoView();", item)
        item.click()

    def click_on_menu_and_submenu_item(self, browser, menu_name, submenu_name):
        menu_item = browser.find_element(By.XPATH, "//*[@class='menu-list']//*[@class='text'][contains(text(), '" + menu_name + "')]")
        browser.execute_script("arguments[0].scrollIntoView();", menu_item)
        menu_item.click()

        sub_item = browser.find_element(By.XPATH, "//*[@class='menu-list']//*[@class='text'][contains(text(), '" + submenu_name + "')]")
        browser.execute_script("arguments[0].scrollIntoView();", sub_item)
        sub_item.click()