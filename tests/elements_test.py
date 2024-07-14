from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            checked_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert checked_checkboxes == output_result, "checkboxes have not been selected"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button = RadioButtonPage(driver)
            radio_button.open()
            radio_button.click_yes_radio_button()
            yes_radio_status = radio_button.check_status_yes_radio_button()
            radio_button.click_impressive_radio_button()
            impressive_radio_status = radio_button.check_status_impressive_radio_button()
            radio_button.click_no_radio_button()
            no_radio_status = radio_button.check_status_no_radio_button()
            assert yes_radio_status, "'Yes' radio button is not selected"
            assert impressive_radio_status, "'Impressive' radio button is not selected"
            assert no_radio_status, "'No' radio button is not selected"
