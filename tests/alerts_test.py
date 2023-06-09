import time

from pages.alerts_page import BrowserWindowsPage


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

