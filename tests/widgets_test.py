from pages.widgets_page import AccordianPage


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
