from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # create form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    PERMANENT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title = 'Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class = 'rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonsPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTableLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id = "addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id = "firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id = "lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id = "userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id = "age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id = "salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id = "department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id = "submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = (".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "div select[aria-label='rows per page']")

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "div span[title='Edit']")


class ButtonsPageLocators:
    DOUBLE_BUTTON_CLICK = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    ALL_BUTTON = (By.CSS_SELECTOR, "div[class='col-12 mt-4 col-md-6']")
    CLICK_ME_BUTTON = ("//*[text()='Click Me']")

    #result

    SUCCESS_DOUBLE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    SUCCESS_RIGHT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")

class UploadAndDownloadLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")

    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")

class DynamicPropertiesLocators:
    COLOR_CHANGE_BOTTON =(By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER_FIVE_SEC_BOTTON =(By.CSS_SELECTOR, "button[id='visibleAfter']")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")

