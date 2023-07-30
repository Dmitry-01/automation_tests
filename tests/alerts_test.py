import time

from pages.alerts_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


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

    class TestFramesPage:

        def test_frame(self, driver):
            frame_page = FramesPage(driver,"https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.check_frame("frame1")
            result_frame2 = frame_page.check_frame("frame2")
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    class TestNestedFramesPage:

            def test_nested_frames(self,driver):
                nested_frames_page = NestedFramesPage(driver,"https://demoqa.com/nestedframes")
                nested_frames_page.open()
                parent_text, child_text = nested_frames_page.check_nested_frame()
                assert parent_text == "Parent frame", "The nested frame does not exist"
                assert child_text == "Child Iframe", "The nested frame does not exist"


