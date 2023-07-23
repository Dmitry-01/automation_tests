import random
import time

from locators.alerts_locators import BrowserWindowsPageLocators
from locators.elements_page_locators import AlertsPageLocators
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
class AlertsPage(BasePage):

        locators = AlertsPageLocators()

        def check_see_alert(self):
            self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
            alert_window = self.driver.switch_to.alert
            return alert_window.text

        def check_alert_appear_5_sec(self):
            self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
            time.sleep(5)
            alert_window = self.driver.switch_to.alert
            return alert_window.text

        def check_confirm_alert(self):
            self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
            alert_window = self.driver.switch_to.alert
            alert_window.accept()
            text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
            return text_result

        def check_promt_alert(self):
            text = f"Autotest{random.randint(0,999)}"
            self.element_is_visible(self.locators.PROMT_BOX_ALERT_BUTTON).click()
            alert_window = self.driver.switch_to.alert
            alert_window.send_keys(text)
            alert_window.accept()
            text_result = self.element_is_present(self.locators.PROMT_RESULT).text
            return text, text_result
