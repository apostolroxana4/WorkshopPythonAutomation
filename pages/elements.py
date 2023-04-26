from selenium.webdriver.common.by import By


class Elements:
    section_elements = "//*[contains(text(),'Elements')]"
    subsection_checkbox = "//*[@id='item-1']"
    home_item = "//*[contains(text(),'Home')]"
    expand_home = "svg[class='rct-icon rct-icon-expand-close']"
    downloads_item = "//*[contains(text(),'Downloads')"
    downloads_result = "span[class='text-success']"
    downloads_excel = "result"
    expand_documents = "svg[class='rct-icon rct-icon-expand-close']"
    documents_item = "//*[contains(text(),'Documents')"
    office_item = "//*[contains(text(),'Office')]"
    workspace_item = "//*[contains(text(),'Office')]"
    documents_office_result = "result"
    documents_workspace_result = "result"
    documents_office_public_result = "span[class='text-success']"
    documents_workspace_angular_result = "span[class='text-success']"
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

    def fill_credentials(self, browser, username, email, permanent_address):
        if (
                (not browser.find_element(By.ID, self.username).is_displayed())
                or (not browser.find_element(By.XPATH, self.email).is_displayed())
                #or (not browser.find_element(By.CSS_SELECTOR, self.current_address).is_displayed())
                or (not browser.find_element(By.ID, self.permanent_address).is_displayed())
        ):
            raise ValueError("Fields are not visible")

        return (
                (browser.find_element(By.ID, self.username) == username)
                and (browser.find_element(By.XPATH, self.email) == email)
                #and (browser.find_element(By.CSS_SELECTOR, self.current_address) == current_address)
                and (browser.find_element(By.ID, self.permanent_address) == permanent_address)
                     )
