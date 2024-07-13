from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver)
            text_box_page.open()
            full_name, email, current_address, permananet_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, \
                output_permananet_address = text_box_page.check_filled_form()
            assert full_name == output_name, "full name is not equal to output"
            assert email == output_email, "email is not equal to output"
            assert current_address == output_current_address, "current address is not equal to output"
            assert permananet_address == output_permananet_address, "permananet address is not equal to output"
