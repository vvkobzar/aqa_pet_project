from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


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

        def test_alert_will_appear_after_5_seconds(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "the alert did not appear after 5 seconds"

        def test_alert_confirm_box_will_appear(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()
            chose_option = alerts_page.alert_confirm_box_appear_accept_or_dismiss()
            result = alerts_page.check_alert_confirm_box_appear()
            assert chose_option == result, "the selected result does not match"

        def test_alert_prompt_box_will_appear(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()
            input_name = alerts_page.input_alert_prompt_box_will_appear()
            result_name = alerts_page.check_alert_prompt_box_will_appear()
            assert input_name == result_name, "the name entered in the alert will not match the result"

    class TestFramesPage:
        def test_frames(self, driver):
            frames_page = FramesPage(driver)
            frames_page.open()
            result_frame1 = frames_page.check_frame('frame1')
            result_frame2 = frames_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "the frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "the frame does not exist"

    class TestNestedFramesPage:
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver)
            nested_frames_page.open()
            parent_frame_text, child_frame_text = nested_frames_page.check_nested_frame()
            assert parent_frame_text == "Parent frame", "nested frame does not exist"
            assert child_frame_text == "Child Iframe", "nested frame does not exist"
