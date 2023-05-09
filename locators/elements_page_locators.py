from selenium.webdriver.common.by import By



class TextBoxPageLocators:

    # FIRST_NAME = (By.NAME, "firstName")
    # LAST_NAME = (By.NAME, "lastName")
    # EMAIL = (By.NAME, "email")
    # PHONE = (By.ID,"phone-form-control")
    # CHECK_BOX = (By.NAME, "checkbox")
    # BUTTON_CREATE_ACCAUNT = (By.TAG_NAME, "button")


    #form fields

    FULL_NAME = (By.CSS_SELECTOR,"input[id='userName']")
    EMAIL = (By.CSS_SELECTOR,"input[id='userEmail']" )
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR,"button[id='submit']" )

    #create form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR,"#output #currentAddress")
    PERMANENT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title = 'Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class = 'rct-title']")

    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")

    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")

    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")