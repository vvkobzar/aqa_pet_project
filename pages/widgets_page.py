from pages.base_page import BasePage
from config.links import WidgetsPageLinks
from locators.widgets_page_locators import AccordianPageLocators


class AccordianPage(BasePage):
    PAGE_URL = WidgetsPageLinks.ACCORDIAN
    locators = AccordianPageLocators()

    def check_first_accordian_card(self):
        card_title = self.element_is_visible(self.locators.CARD_FIRST).text
        card_text = self.element_is_visible(self.locators.CARD_FIRST_TEXT).text
        before_collapse_status = self.element_is_present(
            self.locators.CARD_FIRST_COLLAPSE_STATUS).get_attribute('class')
        self.element_is_visible(self.locators.CARD_FIRST).click()
        after_collapse_status = self.element_is_present(
            self.locators.CARD_FIRST_COLLAPSE_STATUS).get_attribute('class')
        return card_title, len(card_text), before_collapse_status, after_collapse_status

    def check_second_accordian_card(self):
        text_data = []
        card_title = self.element_is_visible(self.locators.CARD_SECOND).text
        before_collapse_status = self.element_is_present(
            self.locators.CARD_SECOND_COLLAPSE_STATUS).get_attribute('class')
        self.element_is_visible(self.locators.CARD_SECOND).click()
        card_text_paragraphs = self.elements_are_visible(self.locators.CARD_SECOND_TEXT)
        for text in card_text_paragraphs:
            text_data.append(len(text.text))
        after_collapse_status = self.element_is_present(
            self.locators.CARD_SECOND_COLLAPSE_STATUS).get_attribute('class')
        return card_title, text_data, before_collapse_status, after_collapse_status

    def check_third_accordian_card(self):
        card_title = self.element_is_visible(self.locators.CARD_THIRD).text
        before_collapse_status = self.element_is_present(
            self.locators.CARD_THIRD_COLLAPSE_STATUS).get_attribute('class')
        self.element_is_visible(self.locators.CARD_THIRD).click()
        card_text = self.element_is_visible(self.locators.CARD_THIRD_TEXT).text
        after_collapse_status = self.element_is_present(
            self.locators.CARD_THIRD_COLLAPSE_STATUS).get_attribute('class')
        return card_title, len(card_text), before_collapse_status, after_collapse_status
