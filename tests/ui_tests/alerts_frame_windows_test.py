import allure
import pytest

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.epic("UI Tests")
@allure.feature("Alerts, Frame & Windows")
class TestAlertsFrameWindows:

    @allure.story("Browser Windows")
    class TestBrowserWindowsPage:

        @allure.title("New tab")
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver)
            browser_windows_page.open()

            new_tab_title_text = browser_windows_page.check_opened_new_tab()

            with allure.step("Checking that tab is open"):
                assert new_tab_title_text == "This is a sample page", (
                    "new tab didn't open"
                )

        @allure.title("New windows")
        def test_new_windows(self, driver):
            browser_windows_page = BrowserWindowsPage(driver)
            browser_windows_page.open()

            new_windows_title_text = browser_windows_page.check_opened_new_windows()

            with allure.step("Checking that tab is open"):
                assert new_windows_title_text == "This is a sample page", (
                    "new window didn't open"
                )

    @allure.story("Alerts")
    class TestAlertsPage:

        @allure.title("Click button to see alert")
        def test_click_button_to_see_alert(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()

            alert_text = alerts_page.check_button_to_see_alert()

            with allure.step("Checking that alert is visible"):
                assert alert_text == "You clicked a button", (
                    "the alert is not visible"
                )

        @allure.title("Alert will appear after 5 seconds")
        def test_alert_will_appear_after_5_seconds(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()

            alert_text = alerts_page.check_alert_appear_5_sec()

            with allure.step("Checking that alert appear after 5 seconds"):
                assert alert_text == "This alert appeared after 5 seconds", (
                    "the alert did not appear after 5 seconds"
                )

        @allure.title("Alert confirm box will appear")
        def test_alert_confirm_box_will_appear(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()

            chose_option = alerts_page.alert_confirm_box_appear_accept_or_dismiss()
            result = alerts_page.check_alert_confirm_box_appear()

            with allure.step("Checking that confirm box will appear"):
                assert chose_option == result, "the selected result does not match"

        @allure.title("Alert prompt box will appear")
        def test_alert_prompt_box_will_appear(self, driver):
            alerts_page = AlertsPage(driver)
            alerts_page.open()

            input_name = alerts_page.input_alert_prompt_box_will_appear()
            result_name = alerts_page.check_alert_prompt_box_will_appear()

            with allure.step("Checking that prompt box will appear"):
                assert input_name == result_name, "the name entered in the alert will not match the result"

    @allure.story("Frames")
    class TestFramesPage:

        @allure.title("Frames")
        def test_frames(self, driver):
            frames_page = FramesPage(driver)
            frames_page.open()

            result_frame1 = frames_page.check_frame('frame1')
            result_frame2 = frames_page.check_frame('frame2')

            with allure.step("Checking that big frame size 500px x 350px"):
                assert result_frame1 == ['This is a sample page', '500px', '350px'], (
                    "the frame does not exist"
                )
            with allure.step("Checking that small frame size 500px x 350px"):
                assert result_frame2 == ['This is a sample page', '100px', '100px'], (
                    "the frame does not exist"
                )

    @allure.story("Nested Frames")
    class TestNestedFramesPage:

        @allure.title("Nested frames")
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver)
            nested_frames_page.open()

            parent_frame_text, child_frame_text = nested_frames_page.check_nested_frame()

            with allure.step("Checking that the parent frame is present"):
                assert parent_frame_text == "Parent frame", (
                    "nested frame does not exist"
                )
            with allure.step("Checking that the child frame is present"):
                assert child_frame_text == "Child Iframe", (
                    "nested frame does not exist"
                )

    @allure.story("Modal Dialogs")
    class TestModalDialogsPage:

        @allure.title("Small modal")
        def test_small_modal(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver)
            modal_dialogs_page.open()

            modal_title, modal_text, modal_size = modal_dialogs_page.getting_a_small_modal_title_text_size()

            with allure.step("Checking that right name small modal"):
                assert modal_title == "Small Modal", (
                    "wrong title of a small modal"
                )
            with allure.step("Checking that right text in the small modal"):
                assert modal_text == "This is a small modal. It has very less content", (
                    "wrong text in the small modal"
                )
            with allure.step("Checking that right size small modal"):
                assert modal_size == {'height': 222, 'width': 300}, (
                    "wrong size for a small modal"
                )

        @allure.title("Large modal")
        @pytest.mark.xfail(reason="wrong size large modal")
        def test_large_modal(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver)
            modal_dialogs_page.open()

            modal_title, modal_len_text, modal_size = modal_dialogs_page.getting_a_large_modal_title_text_size()

            with allure.step("Checking that right name large modal"):
                assert modal_title == "Large Modal", (
                    "wrong title of a large modal"
                )
            with allure.step("Checking that right text in the large modal"):
                assert modal_len_text == 574, (
                    "wrong text in the large modal"
                )
            with allure.step("Checking that right size large modal"):
                assert modal_size == {'height': 430, 'width': 500}, (
                    "wrong size for a large modal"
                )
