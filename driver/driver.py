# Here ww will add the driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver_chrome = webdriver.Chrome(ChromeDriverManager().install())
driver_edge = webdriver.Edge(EdgeChromiumDriverManager().install())


class Driver:

    @staticmethod
    def open_browser():
        driver_chrome.get('https://demoqa.com/')
        driver_chrome.implicitly_wait(10)
        print(driver_chrome.title)
