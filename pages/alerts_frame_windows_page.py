import random

from config.links import AlertsFrameWindowsPageLinks
from generator.generator import generated_person
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.BROWSER_WINDOWS
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        list_handles = self.get_list_windows_handles()
        self.switch_to_new_windows(list_handles[1])
        text_title = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return text_title

    def check_opened_new_windows(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        list_handles = self.get_list_windows_handles()
        self.switch_to_new_windows(list_handles[1])
        text_title = self.element_is_visible(self.locators.NEW_TAB_TEXT).text
        return text_title


class AlertsPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.ALERTS
    locators = AlertsPageLocators()

    def check_button_to_see_alert(self):
        self.element_is_visible(self.locators.CLICK_BUTTON_TO_SEE_ALERT).click()
        alert = self.driver.switch_to.alert
        return alert.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.ALERT_APPEAR_5_SEC_BUTTON).click()
        alert = self.alert_is_present()
        return alert.text

    def alert_confirm_box_appear_accept_or_dismiss(self):
        self.element_is_visible(self.locators.ALERT_CONFIRM_BOX_APPEAR_BUTTON).click()
        alert = self.driver.switch_to.alert
        if random.choice([True, False]):
            alert.accept()
            result = "Ok"
        else:
            alert.dismiss()
            result = "Cancel"
        return result

    def check_alert_confirm_box_appear(self):
        alert_result = self.element_is_visible(self.locators.ALERT_CONFIRM_BOX_RESULT).text
        return alert_result.split()[-1]

    def input_alert_prompt_box_will_appear(self):
        person = next(generated_person())
        self.element_is_visible(self.locators.ALERT_PROMPT_BOX_WILL_APPEAR_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(person.firstname)
        alert.accept()
        return person.firstname

    def check_alert_prompt_box_will_appear(self):
        result = self.element_is_visible(self.locators.ALERT_PROMPT_BOX_WILL_APPEAR_RESULT).text
        return result.split()[-1]


class FramesPage(BasePage):
    PAGE_URL = AlertsFrameWindowsPageLinks.FRAMES
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            text = self.element_is_visible(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == "frame2":
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

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_frame_text = self.element_is_visible(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_IFRAME)
        self.switch_to_frame(child_frame)
        child_frame_text = self.element_is_visible(self.locators.CHILD_FRAME_TEXT).text
        return parent_frame_text, child_frame_text
