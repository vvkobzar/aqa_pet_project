import random

from config.links import AlertsFrameWindowsPageLinks
from generator.generator import generated_person
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
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
