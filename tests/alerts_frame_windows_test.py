from pages.alerts_frame_windows_page import BrowserWindowsPage


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
