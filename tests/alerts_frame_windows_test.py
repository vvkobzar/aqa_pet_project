from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindowsPage:
    class TestBrowserWindowsPage:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver)
            browser_windows_page.open()
            new_tab_title_text = browser_windows_page.check_opened_new_tab()
            assert new_tab_title_text == "This is a sample page", "new tab didn't open"

        def test_new_windows(self, driver):
            browser_windows_page = BrowserWindowsPage(driver)
            browser_windows_page.open()
            new_windows_title_text = browser_windows_page.check_opened_new_windows()
            assert new_windows_title_text == "This is a sample page", "new window didn't open"

    class TestAlertsPage:
        def test_click_button_to_see_alert(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()
            alert_text = alerts_page.check_button_to_see_alert()
            assert alert_text == "You clicked a button", "the alert is not visible"
            