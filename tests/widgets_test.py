import time

import pytest

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage


class TestWidgets:
    class TestAccordianPage:
        def test_first_accordian_card(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open()
            card_title, card_text, \
                before_collapse_status, after_collapse_status = accordian_page.check_first_accordian_card()
            assert card_title == "What is Lorem Ipsum?", "the title card doesn't match"
            assert card_text == 574, "the characters in the text don't match"
            assert before_collapse_status == "collapse show", "accordian card is not deployed by default"
            assert after_collapse_status == "collapsing", "accordian card does not collapse after clicking"

        def test_second_accordian_card(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open()
            card_title, card_text, \
                before_collapse_status, after_collapse_status = accordian_page.check_second_accordian_card()
            assert card_title == "Where does it come from?", "the title card doesn't match"
            assert card_text == [763, 295], "the characters in the text don't match"
            assert before_collapse_status == "collapse", "accordian card is not minimized by default"
            assert after_collapse_status == "collapse show", "accordian card does does not expand after clicking"

        def test_third_accordian_card(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open()
            card_title, card_text, \
                before_collapse_status, after_collapse_status = accordian_page.check_third_accordian_card()
            assert card_title == "Why do we use it?", "the title card doesn't match"
            assert card_text == 613, "the characters in the text don't match"
            assert before_collapse_status == "collapse", "accordian card is not minimized by default"
            assert after_collapse_status == "collapse show", "accordian card does does not expand after clicking"

    class TestAutoCompletePage:
        def test_addition_and_deletion_colors_from_multiple_color_names_field(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open()
            selected_colors = auto_complete_page.random_color_addition_to_multiple_color_field()
            result_colors = auto_complete_page.check_added_colors()
            auto_complete_page.random_remove_colors_from_multiple_color_field()
            after_removal_colors = auto_complete_page.check_added_colors()
            assert selected_colors == result_colors, "added colors do not match the result"
            assert result_colors != after_removal_colors, "the colors have not been removed"

        def test_deleting_all_added_colors_from_multiple_color_names_field(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open()
            added_colors = auto_complete_page.random_color_addition_to_multiple_color_field()
            before_color_delite = auto_complete_page.check_added_colors()
            auto_complete_page.deleting_add_colors_from_multiple_color_field()
            after_color_delite = auto_complete_page.check_added_colors()
            assert added_colors == before_color_delite, "added colors do not match the result"
            assert after_color_delite is None, "all the colors have not been removed"

        def test_single_color_name_field(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open()
            adding_color, result_colors = auto_complete_page.added_color_to_single_color_name_field()
            last_added_color = auto_complete_page.check_added_colors_to_single_color_name_field()
            assert adding_color == result_colors, "added colors do not match the result"
            assert last_added_color in result_colors, "the last added color is not in the results"

    class TestDatePickerPage:
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open()
            date_result_after = date_picker_page.return_value_date_from_date()
            date_picker_page.month_and_year_and_day_selection()
            date_result_before = date_picker_page.return_value_date_from_date()
            assert date_result_after != date_result_before, "the date has not changed"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open()
            selected_year = date_picker_page.select_year_from_date_and_time_field()
            selected_month, selected_day = date_picker_page.select_month_and_day_from_date_and_time_field()
            selected_time = date_picker_page.select_time_from_date_and_time_field()
            date_result = date_picker_page.return_value_date_from_date_and_time_field()
            assert selected_month == date_result[0], "the selected month does not match the result"
            assert selected_day == date_result[1].replace(",", ""), "the selected day does not match the result"
            assert selected_year == date_result[2], "the selected year does not match the result"
            assert selected_time == date_result[3], "the selected time does not match the result"

    class TestSliderPage:
        def test_slider_value_change(self, driver):
            slider_page = SliderPage(driver)
            slider_page.open()
            form_slider_after = slider_page.get_form_slider_value()
            slider_value_after, slider_value_before = slider_page.change_slider_value()
            slider_label_before = slider_page.get_value_label_range_slider()
            form_slider_before = slider_page.get_form_slider_value()
            assert slider_value_after == form_slider_after
            assert slider_value_before == slider_label_before == form_slider_before

    class TestProgressBarPage:
        def test_appearance_reset_stop_start_button_in_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open()
            restart_button = progress_bar_page.check_appears_reset_button_after_reaching_100_percent_in_the_process_bar()
            stop_button, start_button = progress_bar_page.check_appears_stop_and_start_button()
            assert restart_button == "Reset", "reset button does not appear when 100% progress bar is reached"
            assert stop_button == "Stop", "the stop button did not appear"
            assert start_button == "Start", "the start button did not appear"

    class TestTabsPage:
        @pytest.mark.xfail(reason="'More' tab non-clickable, doesn't open")
        def test_status_change_opening_tabs_and_text_tab(self, driver):
            tabs_page = TabsPage(driver)
            tabs_page.open()
            after_what_tab_status, before_what_tab_status, what_tab_text = tabs_page.check_tabs('What')
            after_origin_tab_status, before_origin_tab_status, origin_tab_text = tabs_page.check_tabs('Origin')
            after_use_tab_status, before_use_tab_status, use_tab_text = tabs_page.check_tabs('Use')
            after_more_tab_status, before_more_tab_status, more_tab_text = tabs_page.check_tabs('More')
            assert after_what_tab_status == 'true' and before_what_tab_status == 'true' and what_tab_text == [574]
            assert after_origin_tab_status == 'false' and before_origin_tab_status == 'true' and origin_tab_text == [763, 295]
            assert after_use_tab_status == 'false' and before_use_tab_status == 'true' and use_tab_text == [613]
            assert after_more_tab_status == 'false' and before_more_tab_status == 'true' and more_tab_text == []
