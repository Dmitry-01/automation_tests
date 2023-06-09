from locators.alerts_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

        locators = BrowserWindowsPageLocators()

        def check_opened_new(self):
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
            #Переключи свое внимание на окно с индексом 1
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title = self.element_is_present(self.locators.TITLE_NEW).text
            return text_title

        def check_opened_new(self):
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
            #Переключи свое внимание на окно с индексом 1
            self.driver.switch_to.window(self.driver.window_handles[1])
            text_title = self.element_is_present(self.locators.TITLE_NEW).text
            return text_title
