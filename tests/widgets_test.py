from pages.widgets_page import AccordianPage, AutoCompletePage


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
