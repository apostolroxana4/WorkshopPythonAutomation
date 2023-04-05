from selenium.webdriver.common.by import By


class Elements:

    username = 'userName'
    email = '//*[@id="userEmail"]'
    current_address = '#currentAddress'
    permanent_address = 'permanentAddress'
    submit_button = 'submit'


class StepsElements(Elements):

    def fill_credentials(self, browser, username, email, current_address, permanent_address):
        if (
                (not browser.find_element(By.ID, self.username).visible())
                or (not browser.find_element(By.XPATH, self.email).visible())
                or (not browser.find_element(By.CSS_SELECTOR, self.current_address).visible())
                or (browser.find_element(By.ID, self.permanent_address).visible())
        ):
            raise ValueError("Fields are not visible")

        return (
                browser.find_element(By.ID, self.username) == username
                and browser.find_element(By.XPATH, self.email) == email
                and browser.find_element(By.CSS_SELECTOR, self.current_address) == current_address
                and browser.find_element(By.ID, self.permanent_address == permanent_address
        ))

