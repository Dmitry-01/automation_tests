import time

from pages.alerts_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver,"https://demoqa.com/browser-windows")
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new()
            assert text_result == "This is a sample page", "the new tab has not opened"


        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver,"https://demoqa.com/browser-windows")
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new()
            assert text_result == "This is a sample page", "the new tab has not opened"

    class TestAlertsPage:

        def test_see_alerts(self,driver):
            alert_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            allert_text = alert_page.check_see_alert()
            assert allert_text == "You clicked a button", "Allert didn't show up "

        def test_alert_appear_5_sec(self,driver):
            alert_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            allert_text = alert_page.check_alert_appear_5_sec()
            assert allert_text == "This alert appeared after 5 seconds", "Allert didn't show up "

        def test_confirm_alert(self,driver):
            alert_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            allert_text = alert_page.check_confirm_alert()
            assert allert_text == "You selected Ok", "Allert didn't show up "

        def test_promt_alert(self,driver):
            alert_page = AlertsPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            text, allert_text = alert_page.check_promt_alert()
            assert allert_text == f"You entered {text}", "Allert didn't show up "




