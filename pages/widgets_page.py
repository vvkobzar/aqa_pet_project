import random
import time

from generator.generator import generator_color_names
from pages.base_page import BasePage
from config.links import WidgetsPageLinks
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from selenium.webdriver import Keys


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


class AutoCompletePage(BasePage):
    PAGE_URL = WidgetsPageLinks.AUTO_COMPLETE
    locators = AutoCompletePageLocators()

    def random_color_addition_to_multiple_color_field(self):
        colors = generator_color_names()
        multiple_color_field = self.element_is_visible(self.locators.MULTIPLE_COLOR_FIELD)
        for color in colors:
            multiple_color_field.send_keys(color)
            multiple_color_field.send_keys(Keys.TAB)
        return colors

    def check_added_colors(self):
        result_colors = []
        try:
            added_colors = self.elements_are_visible(self.locators.COLOR_NAMES)
            for color in added_colors:
                result_colors.append(color.text)
            return result_colors
        except Exception as e:
            return None

    def random_remove_colors_from_multiple_color_field(self):
        colors_remove = self.elements_are_visible(self.locators.COLOR_REMOVE_BUTTON)
        num_colors = random.randint(1, len(colors_remove))
        random_color_remove = random.sample(colors_remove, num_colors)
        for color in random_color_remove:
            color.click()

    def deleting_add_colors_from_multiple_color_field(self):
        self.element_is_visible(self.locators.ALL_REMOVE_COLOR_FIELD_BUTTON).click()

    def added_color_to_single_color_name_field(self):
        data = []
        colors = generator_color_names()
        single_color_field = self.element_is_visible(self.locators.SINGLE_COLOR_FIELD)
        for color in colors:
            single_color_field.send_keys(color)
            single_color_field.send_keys(Keys.TAB)
            check_colors = self.check_added_colors_to_single_color_name_field()
            data.append(check_colors)
        return colors, data

    def check_added_colors_to_single_color_name_field(self):
        try:
            added_colors = self.element_is_visible(self.locators.SINGLE_COLOR_NAME).text
            return added_colors
        except Exception as e:
            return None


class DatePickerPage(BasePage):
    PAGE_URL = WidgetsPageLinks.DATE_PICKER
    locators = DatePickerPageLocators()

    def month_and_year_selection(self):
        self.element_is_visible(self.locators.DATE_INPUT).click()
        self.select_by_value(self.locators.DATE_SELECT_MONTH, random.randint(0, 11))
        self.select_by_value(self.locators.DATE_SELECT_YEAR, random.randint(1900, 2100))

    def day_selection(self):
        self.element_is_visible(self.locators.DATE_INPUT).click()
        days = self.elements_are_visible(self.locators.DATE_SELECT_DAY)
        day = random.choice(days)
        day.click()

    def return_date(self):
        return self.element_is_visible(self.locators.DATE_INPUT).get_attribute('value')
