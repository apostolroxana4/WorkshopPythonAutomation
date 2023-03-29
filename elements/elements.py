class Items:
    elements = "//h5[contains(text(), 'Elements')]"
    radio_button = "//*[contains(text(), 'Radio Button')]"
    yes_radio = "//label[@for='yesRadio']"
    yes_radio_selected = "//label[@for='yesRadio']/../input"
    impressive_radio = "//label[@for='impressiveRadio']"
    impressive_radio_selected = "//label[@for='impressiveRadio']/../input"

items = Items()
