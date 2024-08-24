import allure
import random

from pages.base_page import BasePage
from generator.generator import generated_person
from config.links import AlertsFrameWindowsPageLinks
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators


class BrowserWindowsPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.BROWSER_WINDOWS
    locators = BrowserWindowsPageLocators()

    @allure.step("Click on the 'New Tab' button and switch to the new tab")
    def check_opened_new_tab(self):
        with allure.step("Click the 'New Tab' button"):
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        with allure.step("Switch to the new tab"):
            list_handles = self.get_list_windows_handles()
            self.switch_to_new_windows(list_handles[1])
        with allure.step("Get text title from the new tab"):
            text_title = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return text_title

    @allure.step("Click on the 'New Window' button and switch to the new window")
    def check_opened_new_windows(self):
        with allure.step("Click the 'New Window' button"):
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        with allure.step("Switch to the new window"):
            list_handles = self.get_list_windows_handles()
            self.switch_to_new_windows(list_handles[1])
        with allure.step("Get text title from the new window"):
            text_title = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return text_title


class AlertsPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.ALERTS
    locators = AlertsPageLocators()

    @allure.step("Click the button to see an alert and return the alert text")
    def check_button_to_see_alert(self):
        with allure.step("Click the button to trigger an alert"):
            self.element_is_visible(self.locators.CLICK_BUTTON_TO_SEE_ALERT).click()
        with allure.step("Switch to the alert and get the alert text"):
            alert = self.driver.switch_to.alert
            alert_text = alert.text
        return alert_text

    @allure.step("Click the button to make an alert appear after 5 seconds and return the alert text")
    def check_alert_appear_5_sec(self):
        with allure.step("Click the button to trigger alert appearance after 5 seconds"):
            self.element_is_visible(self.locators.ALERT_APPEAR_5_SEC_BUTTON).click()
        with allure.step("Wait for the alert to appear and get the alert text"):
            alert = self.alert_is_present()
            alert_text = alert.text
        return alert_text

    @allure.step("Handle the alert confirm box by either accepting or dismissing it and return the result")
    def alert_confirm_box_appear_accept_or_dismiss(self):
        with allure.step("Click the button to trigger the confirm alert box"):
            self.element_is_visible(self.locators.ALERT_CONFIRM_BOX_APPEAR_BUTTON).click()
        with allure.step("Switch to the alert and decide to accept or dismiss it"):
            alert = self.driver.switch_to.alert
            if random.choice([True, False]):
                alert.accept()
                result = "Ok"
            else:
                alert.dismiss()
                result = "Cancel"
        return result

    @allure.step("Get the result of the alert confirm box")
    def check_alert_confirm_box_appear(self):
        with allure.step("Get the result text from the alert confirm box"):
            alert_result = self.element_is_visible(self.locators.ALERT_CONFIRM_BOX_RESULT).text
        return alert_result.split()[-1]

    @allure.step("Trigger the prompt box, input text, and return the input text")
    def input_alert_prompt_box_will_appear(self):
        person = next(generated_person())
        with allure.step("Click the button to trigger the prompt alert box"):
            self.element_is_visible(self.locators.ALERT_PROMPT_BOX_WILL_APPEAR_BUTTON).click()
        with allure.step("Switch to the alert, input text, and accept it"):
            alert = self.driver.switch_to.alert
            alert.send_keys(person.firstname)
            alert.accept()
        return person.firstname

    @allure.step("Get the result of the alert prompt box")
    def check_alert_prompt_box_will_appear(self):
        with allure.step("Get the result text from the alert prompt box"):
            result = self.element_is_visible(self.locators.ALERT_PROMPT_BOX_WILL_APPEAR_RESULT).text
        return result.split()[-1]


class FramesPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.FRAMES
    locators = FramesPageLocators()

    @allure.step("Check frame by number and return its text, width, and height")
    def check_frame(self, frame_num):
        if frame_num == "frame1":
            with allure.step("Switch to the first frame and get its text, width, and height"):
                frame = self.element_is_present(self.locators.FIRST_FRAME)
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
                self.switch_to_frame(frame)
                text = self.element_is_visible(self.locators.TITLE_FRAME).text
                self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == "frame2":
            with allure.step("Switch to the second frame and get its text, width, and height"):
                frame = self.element_is_present(self.locators.SECOND_FRAME)
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
                self.switch_to_frame(frame)
                text = self.element_is_visible(self.locators.TITLE_FRAME).text
                self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.NESTED_FRAMES
    locators = NestedFramesPageLocators()

    @allure.step("Check nested frames and return the text from parent and child frames")
    def check_nested_frame(self):
        with allure.step("Switch to the parent frame and get its text"):
            parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
            self.switch_to_frame(parent_frame)
            parent_frame_text = self.element_is_visible(self.locators.PARENT_FRAME_TEXT).text
        with allure.step("Switch to the child frame and get its text"):
            child_frame = self.element_is_present(self.locators.CHILD_IFRAME)
            self.switch_to_frame(child_frame)
            child_frame_text = self.element_is_visible(self.locators.CHILD_FRAME_TEXT).text
        return parent_frame_text, child_frame_text


class ModalDialogsPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.MODAL_DIALOGS
    locators = ModalDialogsPageLocators()

    @allure.step("Get title, text, and size of the small modal dialog")
    def getting_a_small_modal_title_text_size(self):
        with allure.step("Click the button to open the small modal dialog"):
            self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        with allure.step("Get title, text, and size of the small modal dialog"):
            modal_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
            modal_text = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
            size = self.element_is_present(self.locators.SMALL_MODAL).size
        with allure.step("Close the small modal dialog"):
            self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return modal_title, modal_text, size

    @allure.step("Get title, text length, and size of the large modal dialog")
    def getting_a_large_modal_title_text_size(self):
        with allure.step("Click the button to open the large modal dialog"):
            self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        with allure.step("Get title, text length, and size of the large modal dialog"):
            modal_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
            modal_text = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
            size = self.element_is_present(self.locators.LARGE_MODAL).size
        with allure.step("Close the large modal dialog"):
            self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return modal_title, len(modal_text), size
