import time
import allure
import random

from selenium.webdriver import Keys
from pages.base_page import BasePage
from config.links import WidgetsPageLinks
from generator.generator import generator_color_names
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators


class AccordianPage(BasePage):
    PAGE_URL = WidgetsPageLinks.ACCORDIAN
    locators = AccordianPageLocators()

    @allure.step("Check the first accordion card")
    def check_first_accordian_card(self):
        with allure.step("Get the title of the first accordion card"):
            card_title = self.element_is_visible(self.locators.CARD_FIRST).text

        with allure.step("Get the text of the first accordion card"):
            card_text = self.element_is_visible(self.locators.CARD_FIRST_TEXT).text

        with allure.step("Get the collapse status before clicking"):
            before_collapse_status = self.element_is_present(
                self.locators.CARD_FIRST_COLLAPSE_STATUS).get_attribute('class')

        with allure.step("Click on the first accordion card"):
            self.element_is_visible(self.locators.CARD_FIRST).click()

        with allure.step("Get the collapse status after clicking"):
            after_collapse_status = self.element_is_present(
                self.locators.CARD_FIRST_COLLAPSE_STATUS).get_attribute('class')

        return card_title, len(card_text), before_collapse_status, after_collapse_status

    @allure.step("Check the second accordion card")
    def check_second_accordian_card(self):
        with allure.step("Get the title of the second accordion card"):
            card_title = self.element_is_visible(self.locators.CARD_SECOND).text

        with allure.step("Get the collapse status before clicking"):
            before_collapse_status = self.element_is_present(
                self.locators.CARD_SECOND_COLLAPSE_STATUS).get_attribute('class')

        with allure.step("Click on the second accordion card"):
            self.element_is_visible(self.locators.CARD_SECOND).click()

        with allure.step("Get the text paragraphs of the second accordion card"):
            card_text_paragraphs = self.elements_are_visible(self.locators.CARD_SECOND_TEXT)
            text_data = [(len(text.text)) for text in card_text_paragraphs]

        with allure.step("Get the collapse status after clicking"):
            after_collapse_status = self.element_is_present(
                self.locators.CARD_SECOND_COLLAPSE_STATUS).get_attribute('class')

        return card_title, text_data, before_collapse_status, after_collapse_status

    @allure.step("Check the third accordion card")
    def check_third_accordian_card(self):
        with allure.step("Get the title of the third accordion card"):
            card_title = self.element_is_visible(self.locators.CARD_THIRD).text

        with allure.step("Get the collapse status before clicking"):
            before_collapse_status = self.element_is_present(
                self.locators.CARD_THIRD_COLLAPSE_STATUS).get_attribute('class')

        with allure.step("Click on the third accordion card"):
            self.element_is_visible(self.locators.CARD_THIRD).click()

        with allure.step("Get the text of the third accordion card"):
            card_text = self.element_is_visible(self.locators.CARD_THIRD_TEXT).text

        with allure.step("Get the collapse status after clicking"):
            after_collapse_status = self.element_is_present(
                self.locators.CARD_THIRD_COLLAPSE_STATUS).get_attribute('class')

        return card_title, len(card_text), before_collapse_status, after_collapse_status


class AutoCompletePage(BasePage):
    PAGE_URL = WidgetsPageLinks.AUTO_COMPLETE
    locators = AutoCompletePageLocators()

    @allure.step("Add random colors to the multiple color field")
    def random_color_addition_to_multiple_color_field(self):
        colors = generator_color_names()
        multiple_color_field = self.element_is_visible(self.locators.MULTIPLE_COLOR_FIELD)
        with allure.step(f"Adding colors: {colors}"):
            for color in colors:
                multiple_color_field.send_keys(color)
                multiple_color_field.send_keys(Keys.TAB)
        return colors

    @allure.step("Check the added colors in the multiple color field")
    def check_added_colors(self):
        try:
            added_colors = self.elements_are_visible(self.locators.COLOR_NAMES)
            result_colors = [color.text for color in added_colors]
            with allure.step(f"Colors found: {result_colors}"):
                return result_colors
        except Exception as e:
            with allure.step(f"An error occurred: {str(e)}"):
                allure.attach(body=str(e), name="Exception details", attachment_type=allure.attachment_type.TEXT)
            return None

    @allure.step("Randomly remove colors from the multiple color field")
    def random_remove_colors_from_multiple_color_field(self):
        colors_remove = self.elements_are_visible(self.locators.COLOR_REMOVE_BUTTON)
        num_colors = random.randint(1, len(colors_remove))
        random_color_remove = random.sample(colors_remove, num_colors)
        with allure.step(f"Removing colors: {[color.text for color in random_color_remove]}"):
            for color in random_color_remove:
                color.click()

    @allure.step("Remove all colors from the multiple color field")
    def deleting_add_colors_from_multiple_color_field(self):
        with allure.step("Clicking the button to remove all colors"):
            self.element_is_visible(self.locators.ALL_REMOVE_COLOR_FIELD_BUTTON).click()

    @allure.step("Add colors to the single color name field")
    def added_color_to_single_color_name_field(self):
        data = []
        colors = generator_color_names()
        single_color_field = self.element_is_visible(self.locators.SINGLE_COLOR_FIELD)
        with allure.step(f"Adding colors: {colors}"):
            for color in colors:
                single_color_field.send_keys(color)
                single_color_field.send_keys(Keys.TAB)
                check_colors = self.check_added_colors_to_single_color_name_field()
                data.append(check_colors)
        return colors, data

    @allure.step("Check the added color in the single color name field")
    def check_added_colors_to_single_color_name_field(self):
        try:
            added_colors = self.element_is_visible(self.locators.SINGLE_COLOR_NAME).text
            with allure.step(f"Color found: {added_colors}"):
                return added_colors
        except Exception as e:
            with allure.step(f"An error occurred: {str(e)}"):
                allure.attach(body=str(e), name="Exception details", attachment_type=allure.attachment_type.TEXT)
            return None


class DatePickerPage(BasePage):
    PAGE_URL = WidgetsPageLinks.DATE_PICKER
    locators = DatePickerPageLocators()

    @allure.step("Select month, year, and day")
    def month_and_year_and_day_selection(self):
        self.element_is_visible(self.locators.DATE_INPUT).click()
        self.select_by_value(self.locators.DATE_SELECT_YEAR, random.randint(1900, 2100))
        self.select_by_value(self.locators.DATE_SELECT_MONTH, random.randint(0, 11))
        selected_month = self.element_is_visible(self.locators.DATE_MONTH_STATUS).text.split()[0]
        self.day_selection(selected_month)

    @allure.step("Select day for the given month")
    def day_selection(self, month):
        days_list = self.elements_are_visible(self.locators.DATE_SELECT_DAY(month))
        selected_day = random.choice(days_list)
        with allure.step(f"Day selected: {selected_day.text}"):
            selected_day.click()

    @allure.step("Get selected date value from date input")
    def return_value_date_from_date(self):
        return self.element_is_present(self.locators.DATE_INPUT).get_attribute('value')

    @allure.step("Select month and day out of date and time field")
    def select_month_and_day_from_date_and_time_field(self):
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        months_list = self.elements_are_visible(self.locators.DATE_AND_TIME_MONTH_LIST)
        selected_month = random.choice(months_list)
        selected_month_text = selected_month.text

        with allure.step(f"Month selected from date and time field: {selected_month_text}"):
            selected_month.click()

        selected_day_text = self.select_day_from_date_and_time_field(selected_month_text)
        return selected_month_text, selected_day_text

    @allure.step("Select day for the given month out of date and time field")
    def select_day_from_date_and_time_field(self, month):
        day_list = self.elements_are_visible(self.locators.DATE_SELECT_DAY(month))
        selected_day = random.choice(day_list)
        selected_day_text = selected_day.text

        with allure.step(f"Day selected: {selected_day_text}"):
            selected_day.click()

        return selected_day_text

    @allure.step("Select year out of date and time field")
    def select_year_from_date_and_time_field(self):
        self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).click()
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        year_list = self.elements_are_present(self.locators.DATE_AND_TIME_YEAR_LIST)
        selected_year = random.choice(year_list)
        selected_year_text = selected_year.text

        with allure.step(f"Year selected: {selected_year_text}"):
            selected_year.click()

        return selected_year_text

    @allure.step("Select time out of date and time field")
    def select_time_from_date_and_time_field(self):
        times_list = self.elements_are_present(self.locators.DATE_AND_TIME_TIME_LIST)
        selected_time = random.choice(times_list)
        selected_time_text = selected_time.text

        with allure.step(f"Time selected: {selected_time_text}"):
            selected_time.click()

        convert_time = self.convert_to_12_hour_format(selected_time_text)
        return convert_time

    @allure.step("Get selected date and time value")
    def return_value_date_from_date_and_time_field(self):
        date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT).get_attribute('value')
        with allure.step(f"Date and time value returned: {date.split()}"):
            return date.split()

    @staticmethod
    @allure.step("Convert time to 12-hour format")
    def convert_to_12_hour_format(time_str):
        hours, minutes = map(int, time_str.split(':'))
        hours = hours % 12
        if hours == 0:
            hours = 12
        formatted_time = f"{hours}:{minutes:02}"

        with allure.step(f"Time converted to 12-hour format: {formatted_time}"):
            return formatted_time


class SliderPage(BasePage):
    PAGE_URL = WidgetsPageLinks.SLIDER
    locators = SliderPageLocators()

    @allure.step("Change slider value")
    def change_slider_value(self):
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        slider_value_after = slider_input.get_attribute('value')
        self.action_drag_and_drop_by_offset(slider_input, random.randint(-325, 325), 0)
        slider_value_before = slider_input.get_attribute('value')
        return slider_value_after, slider_value_before

    @allure.step("Get value from label range slider")
    def get_value_label_range_slider(self):
        value = self.element_is_visible(self.locators.LABEL_SLIDER_VALUE).text
        with allure.step(f"Label slider value: {value}"):
            return value

    @allure.step("Get form slider value")
    def get_form_slider_value(self):
        value = self.element_is_visible(self.locators.SLIDER_VALUE_INPUT).get_attribute('value')
        with allure.step(f"Form slider value: {value}"):
            return value


class ProgressBarPage(BasePage):
    PAGE_URL = WidgetsPageLinks.PROGRESS_BAR
    locators = ProgressBarPageLocators()

    @allure.step("Check if reset button appears after reaching 100% in the progress bar")
    def check_appears_reset_button_after_reaching_100_percent_in_the_process_bar(self):
        self.element_is_visible(self.locators.START_BUTTON).click()

        with allure.step("Waiting for progress bar to reach 100%"):
            while True:
                progress_value = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
                with allure.step(f"Current progress value: {progress_value}"):
                    if progress_value == '100%':
                        time.sleep(0.1)
                        reset_button = self.element_is_visible(self.locators.RESET_BUTTON).text
                        with allure.step(f"Reset button appears with text: {reset_button}"):
                            self.element_is_visible(self.locators.RESET_BUTTON).click()
                        break
        return reset_button

    @allure.step("Check if stop and start buttons appear correctly during the progress bar process")
    def check_appears_stop_and_start_button(self):
        self.element_is_visible(self.locators.START_BUTTON).click()

        with allure.step("Monitoring progress bar value for random stop"):
            while True:
                progress_value = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
                random_stop_value = f"{random.randint(1, 99)}%"
                with allure.step(f"Current progress value: {progress_value}"):
                    if progress_value == random_stop_value:
                        stop_button = self.element_is_visible(self.locators.START_BUTTON).text
                        with allure.step(f"Stop button appears with text: {stop_button}"):
                            self.element_is_visible(self.locators.START_BUTTON).click()

                        start_button = self.element_is_visible(self.locators.START_BUTTON).text
                        with allure.step(f"Start button appears with text: {start_button}"):
                            break
        return stop_button, start_button


class TabsPage(BasePage):
    PAGE_URL = WidgetsPageLinks.TABS
    locators = TabsPageLocators()

    @allure.step("Check the status and content of the '{name_tab}' tab")
    def check_tabs(self, name_tab):
        tabs = {
            'What':
                {'tab_status': self.locators.WHAT_TAB,
                 'tab_text': self.locators.WHAT_TAB_TEXT},
            'Origin':
                {'tab_status': self.locators.ORIGIN_TAB,
                 'tab_text': self.locators.ORIGIN_TAB_TEXT},
            'Use':
                {'tab_status': self.locators.USE_TAB,
                 'tab_text': self.locators.USE_TAB_TEXT},
            'More':
                {'tab_status': self.locators.MORE_TAB,
                 'tab_text': self.locators.MORE_TAB_TEXT}
        }
        with allure.step(f"Locate the '{name_tab}' tab and check initial status"):
            button = self.element_is_visible(tabs[name_tab]['tab_status'])
            after_tab_status = self.element_is_present(tabs[name_tab]['tab_status']).get_attribute('aria-selected')

        with allure.step(f"Click on the '{name_tab}' tab and check status after click"):
            button.click()
            before_tab_status = self.element_is_present(tabs[name_tab]['tab_status']).get_attribute('aria-selected')

        with allure.step(f"Retrieve text content from the '{name_tab}' tab"):
            tab_text = self.elements_are_visible(tabs[name_tab]['tab_text'])
            tabs_text = [len(text.text) for text in tab_text]
        return after_tab_status, before_tab_status, tabs_text


class ToolTipsPage(BasePage):
    PAGE_URL = WidgetsPageLinks.TOOL_TIPS
    locators = ToolTipsPageLocators()

    @allure.step("Retrieve text from tooltip")
    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        with allure.step("Hover over element to trigger tooltip"):
            element = self.element_is_present(hover_elem)
            self.action_move_to_element(element)
            self.element_is_visible(wait_elem)
            self.action_move_to_element(element)

        with allure.step("Extract tooltip text"):
            tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
            text = tool_tip_text.text

        allure.attach(text, name="Tooltip Text", attachment_type=allure.attachment_type.TEXT)
        return text

    @allure.step("Check all tooltips on the page")
    def check_tool_tips(self):
        with allure.step("Check tooltip for the 'Hover me to see' button"):
            tool_tip_text_button = self.get_text_from_tool_tips(
                self.locators.HOVER_ME_TO_SEE_BUTTON, self.locators.TOOL_TIPS_BUTTON)

        with allure.step("Check tooltip for the 'Hover me to see' field"):
            tool_tip_text_field = self.get_text_from_tool_tips(
                self.locators.HOVER_ME_TO_SEE_FIELD, self.locators.TOOL_TIPS_FIELD)

        with allure.step("Check tooltip for the 'Contrary' link"):
            tool_tip_text_contrary = self.get_text_from_tool_tips(
                self.locators.CONTRARY_LINK, self.locators.TOOL_TIPS_CONTRARY)

        with allure.step("Check tooltip for the 'Section' link"):
            tool_tip_text_section = self.get_text_from_tool_tips(
                self.locators.SECTION_LINK, self.locators.TOOL_TIPS_SECTION)

        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):
    PAGE_URL = WidgetsPageLinks.MENU
    locators = MenuPageLocators()

    @allure.step("Check and retrieve text from all menu items")
    def check_menu(self):
        with allure.step("Locate menu items"):
            menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
            data = []

        for item in menu_item_list:
            with allure.step(f"Hover over menu item '{item.text}' and collect text"):
                self.action_move_to_element(item)
                data.append(item.text)
                allure.attach(
                    item.text, name=f"Menu Item Text: {item.text}", attachment_type=allure.attachment_type.TEXT
                )
        return data


class SelectMenuPage(BasePage):
    PAGE_URL = WidgetsPageLinks.SELECT_MENU
    locators = SelectMenuPageLocators()

    @allure.step("Check if options can be added by clicking to select value field")
    def check_if_options_can_be_added_by_clicking_to_select_value_field(self):
        selected_option = []
        result_option = []
        index = 0
        with allure.step("Click on select value field to show options"):
            select_value = self.element_is_visible(self.locators.SELECT_VALUE_SPAN)
            select_value.click()

        while index < 6:
            with allure.step(f"Select option tab {index + 1} and check the result"):
                tab_list = self.elements_are_visible(self.locators.SELECT_VALUE_TAB)
                tab = tab_list[index]
                selected_option.append(tab.text)
                tab.click()
                result_option.append(self.element_is_visible(self.locators.SELECT_VALUE_SELECTED_OPTION).text)
                select_value.click()
                index += 1

        return selected_option, result_option

    @allure.step("Checking the selection of options from the keypad to select value field")
    def checking_the_selection_of_options_from_the_keypad_to_select_value_field(self):
        selected_option = []
        result_option = []
        groups = [
            'Group 1, option 1', 'Group 1, option 2', 'Group 2, option 1', 'Group 2, option 2', 'A root option',
            'Another root option'
        ]
        menu_input = self.element_is_visible(self.locators.SELECT_VALUE_INPUT)
        for group in groups:
            with allure.step(f"Selection option '{group}' from the keypad"):
                selected_option.append(group)
                menu_input.send_keys(group)
                menu_input.send_keys(Keys.TAB)
                result_option.append(self.element_is_visible(self.locators.SELECT_VALUE_SELECTED_OPTION).text)

        return selected_option, result_option

    @allure.step("Check item selection from old-style select menu")
    def check_item_selection_from_old_style_select_menu(self):
        actual_colors_menu = []
        expected_colors_menu = [
            'Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Voilet', 'Indigo', 'Magenta', 'Aqua'
        ]
        for color in expected_colors_menu:
            with allure.step(f"Selection color '{color}' from old-style select menu"):
                self.select_by_text(self.locators.OLD_STYLE_SELECT_MENU, color)
                actual_colors_menu.append(color)

        return actual_colors_menu, expected_colors_menu

    @allure.step("Click to select items from multi-select drop-down")
    def click_to_select_items_from_multiselect_drop_down(self):
        added_element = []

        with allure.step("Open multi-select drop-down and click on each item"):
            self.element_is_visible(self.locators.MULTISELECT_BUTTON).click()
            items_list = self.elements_are_visible(self.locators.MULTISELECT_LIST_ITEM_TEXT)
            for item in items_list:
                added_element.append(item.text)
                item.click()

        return added_element

    @allure.step("Check items in the multi-select drop-down")
    def check_items_in_the_multiselect_drop_down(self):
        with allure.step("Check items in the multi-select drop-down"):
            check_item_field = self.elements_are_visible(self.locators.MULTISELECT_ADDED_ITEM_TEXT)
            field_items = [item.text for item in check_item_field]

        return field_items

    @allure.step("Remove selected items from multi-select drop-down")
    def remove_selected_items_from_multiselect_drop_down(self):
        with allure.step("Remove all selected items from multi-select drop-down"):
            items_list = self.elements_are_visible(self.locators.MULTISELECT_ITEM_CLOSE)
            for item in items_list:
                item.click()
            check_empty_field = self.element_is_visible(self.locators.MULTISELECT_EMPTY_FIELD).text

        return check_empty_field

    @allure.step("Select items out of standard multi-select")
    def select_items_from_standard_multi_select(self):
        selected_items = []
        expected_items = ['Volvo', 'Saab', 'Opel', 'Audi']
        num_subjects = random.randint(1, len(expected_items))
        random_items = random.sample(expected_items, num_subjects)

        with allure.step("Selection random items from the standard multi-select"):
            for item in random_items:
                self.select_by_text(self.locators.MULTI_SELECT, item)
                selected_items.append(item)

        with allure.step("Verify selected items"):
            check_selected_items = self.get_all_selected_options(self.locators.MULTI_SELECT)
            check_added_items = [item.text for item in check_selected_items]

        return set(selected_items), set(check_added_items)
