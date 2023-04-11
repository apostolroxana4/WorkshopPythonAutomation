class ElementFromTextBox:
    text_box_field = "//span[contains(text(),'Text Box')]"
    text_box_text = "//div[contains(text(),'Text Box')]"
    full_name_field = "//label[@id='userName-label']"
    full_name = "//input[@id='userName']"
    email_field = "//label[@id='userEmail-label']"
    email = "//input[@id='userEmail']"
    current_address_field = "//label[@id='currentAddress-label']"
    current_address = "//textarea[@id='currentAddress']"
    permanent_address_field = "//label[@id='permanentAddress-label']"
    permanent_address = "//textarea[@id='permanentAddress']"
    submit_button = "//button[@id='submit']"
    submit_content = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[1]"
