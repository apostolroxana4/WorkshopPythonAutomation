from selenium.webdriver.common.by import By


class Elements:

    username_field = "//label[@id='userName-label']"
    username = "userName"
    email_field = "//label[@id='userEmail-label']"
    email = "//*[@id='userEmail']"
    current_address_field = "//label[@id='currentAddress-label']"
    current_address = "#currentAddress"
    permanent_address_field = "//label[@id='permanentAddress-label']"
    permanent_address = "permanentAddress"
    submit_button = "submit"


class StepsElements(Elements):

    def fill_credentials(self, browser, username, email, current_address, permanent_address):
        if (
                (not browser.find_element(By.ID, self.username).is_displayed())
                or (not browser.find_element(By.XPATH, self.email).is_displayed())
                or (not browser.find_element(By.CSS_SELECTOR, self.current_address).is_displayed())
                or (not browser.find_element(By.ID, self.permanent_address).is_displayed())
        ):
            raise ValueError("Fields are not visible")

        return (
                (browser.find_element(By.ID, self.username) == username)
                and (browser.find_element(By.XPATH, self.email) == email)
                and (browser.find_element(By.CSS_SELECTOR, self.current_address) == current_address)
                and (browser.find_element(By.ID, self.permanent_address) == permanent_address)
                     )
