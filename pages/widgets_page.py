import random
import time

from generator.generator import generator_color_names
from pages.base_page import BasePage
from config.links import WidgetsPageLinks
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators
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

    def month_and_year_and_day_selection(self):
        self.element_is_visible(self.locators.DATE_INPUT).click()
        self.select_by_value(self.locators.DATE_SELECT_YEAR, random.randint(1900, 2100))
        self.select_by_value(self.locators.DATE_SELECT_MONTH, random.randint(0, 11))
        selected_month = self.element_is_visible(self.locators.DATE_MONTH_STATUS).text.split()[0]
        self.day_selection(selected_month)

    def day_selection(self, month):
        days_list = self.elements_are_visible(self.locators.DATE_SELECT_DAY(month))
        selected_day = random.choice(days_list)
        selected_day.click()

    def return_value_date_from_date(self):
        return self.element_is_present(self.locators.DATE_INPUT).get_attribute('value')

    def select_month_and_day_from_date_and_time_field(self):
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        months_list = self.elements_are_visible(self.locators.DATE_AND_TIME_MONTH_LIST)
        selected_month = random.choice(months_list)
        selected_month_text = selected_month.text
        selected_month.click()
        selected_day_text = self.select_day_from_date_and_time_field(selected_month_text)
        return selected_month_text, selected_day_text

    def select_day_from_date_and_time_field(self, month):
        day_list = self.elements_are_visible(self.locators.DATE_SELECT_DAY(month))
        selected_day = random.choice(day_list)
        selected_day_text = selected_day.text
        selected_day.click()
        return selected_day_text

    def select_year_from_date_and_time_field(self):
        self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).click()
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        year_list = self.elements_are_present(self.locators.DATE_AND_TIME_YEAR_LIST)
        selected_year = random.choice(year_list)
        selected_year_text = selected_year.text
        selected_year.click()
        return selected_year_text

    def select_time_from_date_and_time_field(self):
        times_list = self.elements_are_present(self.locators.DATE_AND_TIME_TIME_LIST)
        selected_time = random.choice(times_list)
        selected_time_text = selected_time.text
        selected_time.click()
        convert_time = self.convert_to_12_hour_format(selected_time_text)
        return convert_time

    def return_value_date_from_date_and_time_field(self):
        date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).get_attribute('value')
        return date.split()

    @staticmethod
    def convert_to_12_hour_format(time_str):
        hours, minutes = map(int, time_str.split(':'))
        hours = hours % 12
        if hours == 0:
            hours = 12
        formatted_time = f"{hours}:{minutes:02}"
        return formatted_time


class SliderPage(BasePage):
    PAGE_URL = WidgetsPageLinks.SLIDER
    locators = SliderPageLocators()

    def change_slider_value(self):
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        slider_value_after = slider_input.get_attribute('value')
        self.action_drag_and_drop_by_offset(slider_input, random.randint(-325, 325), 0)
        slider_value_before = slider_input.get_attribute('value')
        return slider_value_after, slider_value_before

    def get_value_label_range_slider(self):
        return self.element_is_visible(self.locators.LABEL_SLIDER_VALUE).text

    def get_form_slider_value(self):
        return self.element_is_visible(self.locators.SLIDER_VALUE_INPUT).get_attribute('value')


class ProgressBarPage(BasePage):
    PAGE_URL = WidgetsPageLinks.PROGRESS_BAR
    locators = ProgressBarPageLocators()

    def check_appears_reset_button_after_reaching_100_percent_in_the_process_bar(self):
        self.element_is_visible(self.locators.START_BUTTON).click()
        while True:
            progress_value = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
            if progress_value == '100%':
                time.sleep(0.1)
                reset_button = self.element_is_visible(self.locators.RESET_BUTTON).text
                self.element_is_visible(self.locators.RESET_BUTTON).click()
                break
        return reset_button

    def check_appears_stop_and_start_button(self):
        self.element_is_visible(self.locators.START_BUTTON).click()
        while True:
            progress_value = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
            if progress_value == f"{random.randint(1, 99)}%":
                stop_button = self.element_is_visible(self.locators.START_BUTTON).text
                self.element_is_visible(self.locators.START_BUTTON).click()
                start_button = self.element_is_visible(self.locators.START_BUTTON).text
                break
        return stop_button, start_button
