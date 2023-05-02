class CheckBoxPage:
    message_element = "//span[contains(text(),'You have selected :')]/following-sibling::span"
    tree_element_part1 = "//span[text()='"
    tree_element_part2_checkbox = "']/preceding-sibling::span[@class='rct-checkbox']"
    tree_element_part2_arrow = "']/ancestor::*[@class='rct-text']/descendant::button"

