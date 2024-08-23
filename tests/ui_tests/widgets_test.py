import allure
import pytest

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


@allure.epic("UI Tests")
@allure.feature("Widgets")
class TestWidgets:

    @allure.story("Accordian")
    class TestAccordianPage:

        @allure.title("First accordian card")
        def test_first_accordian_card(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open()

            (card_title, card_text,
             before_collapse_status, after_collapse_status) = accordian_page.check_first_accordian_card()

            with allure.step("Checking that the card title matches the expected value"):
                assert card_title == "What is Lorem Ipsum?", (
                    "the title card doesn't match"
                )
            with allure.step("Checking that the number of characters in the card text matches the expected value"):
                assert card_text == 574, (
                    "the characters in the text don't match"
                )
            with allure.step("Checking that the accordion card is deployed by default"):
                assert before_collapse_status == "collapse show", (
                    "accordian card is not deployed by default"
                )
            with allure.step("Checking that the accordion card collapses after clicking"):
                assert after_collapse_status == "collapsing", (
                    "accordian card does not collapse after clicking"
                )

        @allure.title("second accordian card")
        def test_second_accordian_card(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open()

            (card_title, card_text,
             before_collapse_status, after_collapse_status) = accordian_page.check_second_accordian_card()

            with allure.step("Checking that the card title matches the expected value"):
                assert card_title == "Where does it come from?", (
                    "the title card doesn't match"
                )
            with allure.step("Checking that the number of characters in the card text matches the expected values"):
                assert card_text == [763, 295], (
                    "the characters in the text don't match"
                )
            with allure.step("Checking that the accordion card is minimized by default"):
                assert before_collapse_status == "collapse", (
                    "accordian card is not minimized by default"
                )
            with allure.step("Checking that the accordion card expands after clicking"):
                assert after_collapse_status == "collapse show", (
                    "accordian card does does not expand after clicking"
                )

        @allure.title("Third accordian card")
        def test_third_accordian_card(self, driver):
            accordian_page = AccordianPage(driver)
            accordian_page.open()

            (card_title, card_text,
             before_collapse_status, after_collapse_status) = accordian_page.check_third_accordian_card()

            with allure.step("Checking that the card title matches the expected value"):
                assert card_title == "Why do we use it?", (
                    "the title card doesn't match"
                )
            with allure.step("Checking that the number of characters in the card text matches the expected value"):
                assert card_text == 613, (
                    "the characters in the text don't match"
                )
            with allure.step("Checking that the accordion card is minimized by default"):
                assert before_collapse_status == "collapse", (
                    "accordian card is not minimized by default"
                )
            with allure.step("Checking that the accordion card expands after clicking"):
                assert after_collapse_status == "collapse show", (
                    "accordian card does does not expand after clicking"
                )

    @allure.story("Auto Complete")
    class TestAutoCompletePage:

        @allure.title("Addition and deletion colors from multiple color names field")
        def test_addition_and_deletion_colors_from_multiple_color_names_field(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open()

            selected_colors = auto_complete_page.random_color_addition_to_multiple_color_field()
            result_colors = auto_complete_page.check_added_colors()
            auto_complete_page.random_remove_colors_from_multiple_color_field()
            after_removal_colors = auto_complete_page.check_added_colors()

            with allure.step("Checking that the added colors match the result"):
                assert selected_colors == result_colors, (
                    "added colors do not match the result"
                )
            with allure.step("Checking that the colors have been removed"):
                assert result_colors != after_removal_colors, (
                    "the colors have not been removed"
                )

        @allure.title("Deleting all added colors from multiple color names field")
        def test_deleting_all_added_colors_from_multiple_color_names_field(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open()

            added_colors = auto_complete_page.random_color_addition_to_multiple_color_field()
            before_color_delite = auto_complete_page.check_added_colors()
            auto_complete_page.deleting_add_colors_from_multiple_color_field()
            after_color_delite = auto_complete_page.check_added_colors()

            with allure.step("Checking that the added colors match the colors before deletion"):
                assert added_colors == before_color_delite, (
                    "added colors do not match the result"
                )
            with allure.step("Checking that all colors have been removed after deletion"):
                assert after_color_delite is None, (
                    "all the colors have not been removed"
                )

        @allure.story("Single color name field")
        def test_single_color_name_field(self, driver):
            auto_complete_page = AutoCompletePage(driver)
            auto_complete_page.open()

            adding_color, result_colors = auto_complete_page.added_color_to_single_color_name_field()
            last_added_color = auto_complete_page.check_added_colors_to_single_color_name_field()

            with allure.step("Checking that the added color matches the result colors"):
                assert adding_color == result_colors, (
                    "added colors do not match the result"
                )
            with allure.step("Checking that the last added color is included in the result colors"):
                assert last_added_color in result_colors, (
                    "the last added color is not in the results"
                )

    @allure.story("Date Picker")
    class TestDatePickerPage:

        @allure.title("Change date")
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open()

            date_result_after = date_picker_page.return_value_date_from_date()
            date_picker_page.month_and_year_and_day_selection()
            date_result_before = date_picker_page.return_value_date_from_date()

            with allure.step("Checking that the date has changed after selection"):
                assert date_result_after != date_result_before, (
                    "the date has not changed"
                )

        @allure.title("Change date and time")
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver)
            date_picker_page.open()

            selected_year = date_picker_page.select_year_from_date_and_time_field()
            selected_month, selected_day = date_picker_page.select_month_and_day_from_date_and_time_field()
            selected_time = date_picker_page.select_time_from_date_and_time_field()
            date_result = date_picker_page.return_value_date_from_date_and_time_field()

            with allure.step("Checking that the selected month matches the result"):
                assert selected_month == date_result[0], (
                    "the selected month does not match the result"
                )
            with allure.step("Checking that the selected day matches the result"):
                assert selected_day == date_result[1].replace(",", ""), (
                    "the selected day does not match the result"
                )
            with allure.step("Checking that the selected year matches the result"):
                assert selected_year == date_result[2], (
                    "the selected year does not match the result"
                )
            with allure.step("Checking that the selected time matches the result"):
                assert selected_time == date_result[3], (
                    "the selected time does not match the result"
                )

    @allure.story("Slider")
    class TestSliderPage:

        @allure.title("Slider value change")
        def test_slider_value_change(self, driver):
            slider_page = SliderPage(driver)
            slider_page.open()

            form_slider_after = slider_page.get_form_slider_value()
            slider_value_after, slider_value_before = slider_page.change_slider_value()
            slider_label_before = slider_page.get_value_label_range_slider()
            form_slider_before = slider_page.get_form_slider_value()

            with allure.step("Checking that the slider value matches the form slider value after change"):
                assert slider_value_after == form_slider_after, (
                    "slider value is not the same as the slider form value"
                )
            with allure.step(
                    "Checking that the slider value before change matches the slider label and form slider value"
            ):
                assert slider_value_before == slider_label_before == form_slider_before, (
                    "slider value is not the same as the slider form value"
                )

    @allure.story("Progress Bar")
    class TestProgressBarPage:

        @allure.title("Appearance reset stop start button in progress bar")
        def test_appearance_reset_stop_start_button_in_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver)
            progress_bar_page.open()

            restart_button = (
                progress_bar_page.check_appears_reset_button_after_reaching_100_percent_in_the_process_bar()
            )
            stop_button, start_button = progress_bar_page.check_appears_stop_and_start_button()

            with allure.step("Checking that the reset button appears after reaching 100% progress bar"):
                assert restart_button == "Reset", (
                    "reset button does not appear when 100% progress bar is reached"
                )
            with allure.step("Checking that the stop button appears after reaching 100% progress bar"):
                assert stop_button == "Stop", (
                    "the stop button did not appear"
                )
            with allure.step("Checking that the start button appears after reaching 100% progress bar"):
                assert start_button == "Start", (
                    "the start button did not appear"
                )

    @allure.story("Tabs")
    class TestTabsPage:

        @allure.title("Status change opening tabs and text tab")
        @pytest.mark.xfail(reason="'More' tab non-clickable, doesn't open")
        def test_status_change_opening_tabs_and_text_tab(self, driver):
            tabs_page = TabsPage(driver)
            tabs_page.open()

            after_what_tab_status, before_what_tab_status, what_tab_text = tabs_page.check_tabs('What')
            after_origin_tab_status, before_origin_tab_status, origin_tab_text = tabs_page.check_tabs('Origin')
            after_use_tab_status, before_use_tab_status, use_tab_text = tabs_page.check_tabs('Use')
            after_more_tab_status, before_more_tab_status, more_tab_text = tabs_page.check_tabs('More')

            with allure.step(
                    "Checking that the 'What' tab is open by default and the number of characters matches"
            ):
                assert (after_what_tab_status == 'true' and
                        before_what_tab_status == 'true' and
                        what_tab_text == [574]), (
                    "tab what is not open by default and the number of characters does not match"
                )

            with allure.step(
                    "Checking that the 'Origin' tab has switched correctly and the number of characters matches"
            ):
                assert (after_origin_tab_status == 'false' and
                        before_origin_tab_status == 'true' and
                        origin_tab_text == [763, 295]), (
                    "tab origin has not switched and the number of characters in the text does not match"
                )

            with allure.step(
                    "Checking that the 'Use' tab has switched correctly and the number of characters matches"
            ):
                assert (after_use_tab_status == 'false' and
                        before_use_tab_status == 'true' and
                        use_tab_text == [613]), (
                    "tab use has not switched and the number of characters in the text does not match"
                )

            with allure.step(
                    "Checking that the 'More' tab has switched correctly and the number of characters matches"
            ):
                assert (after_more_tab_status == 'false' and
                        before_more_tab_status == 'true' and
                        more_tab_text == []), (
                    "tab more has not switched and the number of characters in the text does not match"
                )

    @allure.story("Tool Tips")
    class TestToolTipsPage:

        @allure.title("Appearance tool tips")
        def test_appearance_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver)
            tool_tips_page.open()

            (tool_tip_text_button, tool_tip_text_field,
             tool_tip_text_contrary, tool_tip_text_section) = tool_tips_page.check_tool_tips()

            with allure.step("Checking that the tooltip for the button shows the correct text"):
                assert tool_tip_text_button == "You hovered over the Button", (
                    "the tool tips button didn't show up"
                )
            with allure.step("Checking that the tooltip for the text field shows the correct text"):
                assert tool_tip_text_field == "You hovered over the text field", (
                    "the tool tips field didn't show up "
                )
            with allure.step("Checking that the tooltip for the contrary shows the correct text"):
                assert tool_tip_text_contrary == "You hovered over the Contrary", (
                    "the tool tips contrary didn't show up "
                )
            with allure.step("Checking that the tooltip for the section shows the correct text"):
                assert tool_tip_text_section == "You hovered over the 1.10.32", (
                    "the tool tips section didn't show up "
                )

    @allure.story("Menu")
    class TestMenuPage:

        @allure.title("Contents of the menu on the page")
        def test_contents_of_the_menu_on_the_page(self, driver):
            menu_page = MenuPage(driver)
            menu_page.open()

            actual_menu_items = menu_page.check_menu()
            expected_menu_items = [
                'Main Item 1',
                'Main Item 2',
                'Sub Item',
                'Sub Item',
                'SUB SUB LIST »',
                'Sub Sub Item 1',
                'Sub Sub Item 2',
                'Main Item 3'
            ]

            with allure.step("Checking that the actual menu items match the expected menu items"):
                assert actual_menu_items == expected_menu_items, "Menu items do not match the expected values"

    @allure.story("Select Menu")
    class TestSelectMenuPage:

        @allure.title("Selecting items via click and keyboard in the select value menu")
        def test_selecting_items_via_click_and_keyboard_in_the_select_value_menu(self, driver):
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open()

            click_selected_option, click_result_option = (
                select_menu_page.check_if_options_can_be_added_by_clicking_to_select_value_field()
            )
            keypad_selected_option, keypad_result_option = (
                select_menu_page.checking_the_selection_of_options_from_the_keypad_to_select_value_field()
            )

            with allure.step("Checking that the clicked items match the result items"):
                assert click_selected_option == click_result_option, "the clicked items do not match "

            with allure.step("Checking that the entered items via keypad match the result items"):
                assert keypad_selected_option == keypad_result_option, "entered items do not match"

        @allure.title("Color selected form old style select menu")
        def test_color_selected_from_old_style_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open()

            actual_colors_menu, expected_colors_menu = (
                select_menu_page.check_item_selection_from_old_style_select_menu()
            )

            with allure.step("Checking that the actual colors menu matches the expected colors menu"):
                assert actual_colors_menu == expected_colors_menu, "actual colors doesn't match expected colors menu"

        @allure.title("Click to select items from multiselect drop down")
        def test_click_to_select_items_from_multiselect_drop_down(self, driver):
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open()

            added_element = select_menu_page.click_to_select_items_from_multiselect_drop_down()
            field_items = select_menu_page.check_items_in_the_multiselect_drop_down()
            empty_field = select_menu_page.remove_selected_items_from_multiselect_drop_down()

            with allure.step("Checking that the added items match the items in the field"):
                assert added_element == field_items, (
                    "added items do not match the items in the field"
                )
            with allure.step("Checking that the field is empty after removing selected items"):
                assert empty_field == "Select...", (
                    "items in the form are not deleted"
                )

        @allure.title("Selection of elements from standard multi-select")
        def test_selection_of_elements_from_standard_multi_select(self, driver):
            select_menu_page = SelectMenuPage(driver)
            select_menu_page.open()

            selected_items, check_added_items = select_menu_page.select_items_from_standard_multi_select()

            with allure.step(
                    "Checking that the selected items match the items that are added to the multi-select field"
            ):
                assert selected_items == check_added_items, "the selected items do not match "
