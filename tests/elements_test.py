import random
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


class TestElementsPage:
    class TestTextBoxPage:
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

    class TestCheckBoxPage:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            checked_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert checked_checkboxes == output_result, "checkboxes have not been selected"

    class TestRadioButtonPage:
        def test_yes_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver)
            radio_button_page.open()
            radio_button_page.click_yes_radio_button()
            yes_radio_status = radio_button_page.check_status_yes_radio_button()
            assert yes_radio_status, "'Yes' radio button is not selected"

        def test_impressive_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver)
            radio_button_page.open()
            radio_button_page.click_impressive_radio_button()
            impressive_radio_status = radio_button_page.check_status_impressive_radio_button()
            assert impressive_radio_status, "'Impressive' radio button is not selected"

        def test_no_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver)
            radio_button_page.open()
            radio_button_page.click_no_radio_button()
            no_radio_status = radio_button_page.check_status_no_radio_button()
            assert no_radio_status, "'No' radio button is not selected"

    class TestWebTablesPage:
        def test_web_table_add_person(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()
            new_persons = web_tables_page.add_new_person(random.randint(1, 10))
            table_result = web_tables_page.check_new_added_person()
            for new_person in new_persons:
                assert new_person in table_result, f"the user's data {new_person} does not match"

        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()
            key_word = web_tables_page.add_new_person()[0][random.randint(0, 5)]
            web_tables_page.search_some_person(key_word)
            table_result = web_tables_page.check_search_person()
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()
            lastname = web_tables_page.add_new_person()[0][1]
            web_tables_page.search_some_person(lastname)
            old_table_result = web_tables_page.check_search_person()
            field_index, updated_value = web_tables_page.update_person_info()
            web_tables_page.search_some_person(updated_value)
            new_table_result = web_tables_page.check_search_person()
            old_data_to_compare = old_table_result[:field_index] + old_table_result[field_index + 1:]
            new_data_to_compare = new_table_result[:field_index] + new_table_result[field_index + 1:]
            assert old_data_to_compare == new_data_to_compare, (f"the user's data does not match after update, "
                                                                f"excluding field_index {field_index}")
            assert updated_value == new_table_result[field_index], "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()
            email = web_tables_page.add_new_person()[0][3]
            web_tables_page.search_some_person(email)
            web_tables_page.delete_person()
            text = web_tables_page.check_deleted()
            assert text == "No rows found", "the person has not been deleted"

        def test_web_table_change_count_row(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "the number of rows in the table has not been changed or has changed incorrectly"

    class TestButtonsPage:
        def test_double_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver)
            buttons_page.open()
            buttons_page.double_click_on_the_button()
            message = buttons_page.check_double_click_on_the_button()
            assert message == "You have done a double click", "the double click button did not work"

        def test_right_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver)
            buttons_page.open()
            buttons_page.right_click_on_the_button()
            message = buttons_page.check_right_click_on_the_button()
            assert message == "You have done a right click", "the right click button did not work"

        def test_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver)
            buttons_page.open()
            buttons_page.click_on_the_button()
            message = buttons_page.check_click_on_the_button()
            assert message == "You have done a dynamic click", "the click button did not work"

    class TestLinksPage:
        def test_of_switching_to_new_home_page(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            main_page = links_page.get_current_window_handle()
            links_page.click_on_the_home_link()
            list_page = links_page.get_list_windows_handles()
            links_page.switch_to_new_windows(list_page[1])
            url = links_page.get_url_page()
            new_page = links_page.get_current_window_handle()
            assert main_page != new_page, "error switching between tabs"
            assert url == "https://demoqa.com/", "the link does not match the home page"

        def test_of_switching_to_dynamic_link(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            main_page = links_page.get_current_window_handle()
            links_page.click_on_the_dynamic_link()
            list_page = links_page.get_list_windows_handles()
            links_page.switch_to_new_windows(list_page[1])
            url = links_page.get_url_page()
            new_page = links_page.get_current_window_handle()
            assert main_page != new_page, "error switching between tabs"
            assert url == "https://demoqa.com/", "the link does not match the home page"

        def test_api_created(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            response_status_code, response_reason = links_page.check_on_the_api_created()
            assert response_status_code == 201, "the status code does not match the response"
            assert response_reason == 'Created', "the status text does not match the response"

        def test_api_no_content(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            response_status_code, response_reason = links_page.check_on_the_api_no_content()
            assert response_status_code == 204, "the status code does not match the response"
            assert response_reason == 'No Content', "the status text does not match the response"

        def test_api_moved(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            response_status_code, response_reason = links_page.check_on_the_api_moved()
            assert response_status_code == 301, "the status code does not match the response"
            assert response_reason == 'Moved Permanently', "the status text does not match the response"

        def test_api_bad_request(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            response_status_code, response_reason = links_page.check_on_the_api_bad_request()
            assert response_status_code == 400, "the status code does not match the response"
            assert response_reason == 'Bad Request', "the status text does not match the response"

        def test_api_unauthorized(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            response_status_code, response_reason = links_page.check_on_the_api_unauthorized()
            assert response_status_code == 401, "the status code does not match the response"
            assert response_reason == 'Unauthorized', "the status text does not match the response"

        def test_api_forbidden(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            response_status_code, response_reason = links_page.check_on_the_api_forbidden()
            assert response_status_code == 403, "the status code does not match the response"
            assert response_reason == 'Forbidden', "the status text does not match the response"

        def test_api_not_found(self, driver):
            links_page = LinksPage(driver)
            links_page.open()
            response_status_code, response_reason = links_page.check_on_the_api_not_found()
            assert response_status_code == 404, "the status code does not match the response"
            assert response_reason == 'Not Found', "the status text does not match the response"

    class TestUploadAndDownloadPage:
        def test_download_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver)
            upload_and_download_page.open()
            upload_and_download_page.create_download_dir()
            upload_and_download_page.click_of_the_download_button()
            name_file = upload_and_download_page.get_name_download_file()
            upload_and_download_page.delite_download_file()
            assert name_file == "sampleFile.jpeg", "the name of the downloaded file does not match"

        def test_upload_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver)
            upload_and_download_page.open()
            upload_and_download_page.create_download_dir()
            created_file_name = upload_and_download_page.upload_file()
            uploaded_file_name = upload_and_download_page.getting_name_of_the_uploaded_file()
            upload_and_download_page.delite_download_file()
            assert created_file_name == uploaded_file_name, "the name of the uploaded file does not match"

    class TestDynamicPropertiesPage:
        def test_click_the_button_after_5_seconds(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            dynamic_properties_page.open()
            dynamic_properties_page.click_the_button_after_5_seconds()
            click_button_status = dynamic_properties_page.check_click_the_button_after_5_seconds()
            assert click_button_status == True, "the button was not clicked"

        def test_button_color_change(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            dynamic_properties_page.open()
            color_button_before, color_button_after = dynamic_properties_page.checking_for_button_color_changes()
            assert color_button_before != color_button_after, "the color of the button was not changed"
