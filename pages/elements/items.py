class Items:
    main_page_elements = "div[class='card mt-4 top-card']"
    section_elements = "//*[contains(text(),'Elements')]"
    subsection_check_box = "//*[contains(text(),'Check Box')]"

    home_title = "//*[contains(text(),'Home')]"
    home_arrow = "svg[class='rct-icon rct-icon-expand-close']"

    documents_title = "//*[contains(text(),'Documents')]"
    documents = "span[class='rct-title']"
    documents_results = "span[class='text-success']"
    documents_arrow = "svg[class='rct-icon rct-icon-expand-close']"

    office = "//*[contains(text(),'Office')]"
    office_result = "span[class='text-success']"
    result = 'result'

    workspace = "//*[contains(text(),'WorkSpace')]"
    workspace_result = "span[class='text-success']"

    downloads_title = "//*[contains(text(),'Downloads')]"
    downloads_result = "span[class='text-success']"
