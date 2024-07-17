import random
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


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

    class TestWebTables:
        def test_web_table_add_person(self, driver):
            web_tables = WebTablesPage(driver)
            web_tables.open()
            new_persons = web_tables.add_new_person(random.randint(1, 10))
            table_result = web_tables.check_new_added_person()
            for new_person in new_persons:
                assert new_person in table_result, f"the user's data {new_person} does not match"

        def test_web_table_search_person(self, driver):
            web_tables = WebTablesPage(driver)
            web_tables.open()
            key_word = web_tables.add_new_person()[0][random.randint(0, 5)]
            web_tables.search_some_person(key_word)
            table_result = web_tables.check_search_person()
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_tables = WebTablesPage(driver)
            web_tables.open()
            lastname = web_tables.add_new_person()[0][1]
            web_tables.search_some_person(lastname)
            old_table_result = web_tables.check_search_person()
            field_index, updated_value = web_tables.update_person_info()
            web_tables.search_some_person(updated_value)
            new_table_result = web_tables.check_search_person()
            old_data_to_compare = old_table_result[:field_index] + old_table_result[field_index + 1:]
            new_data_to_compare = new_table_result[:field_index] + new_table_result[field_index + 1:]
            assert old_data_to_compare == new_data_to_compare, (f"the user's data does not match after update, "
                                                                f"excluding field_index {field_index}")
            assert updated_value == new_table_result[field_index], "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_tables = WebTablesPage(driver)
            web_tables.open()
            email = web_tables.add_new_person()[0][3]
            web_tables.search_some_person(email)
            web_tables.delete_person()
            text = web_tables.check_deleted()
            assert text == "No rows found", "the person has not been deleted"

        def test_web_table_change_count_row(self, driver):
            web_tables = WebTablesPage(driver)
            web_tables.open()
            count = web_tables.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "the number of rows in the table has not been changed or has changed incorrectly"
