import allure
import random
import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.epic("UI Tests")
@allure.feature("Elements")
class TestElements:

    @allure.story("Text Box")
    class TestTextBoxPage:

        @allure.title("Text box")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver)
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = (
                text_box_page.check_filled_form()
            )
            with allure.step("Checking that full name"):
                assert full_name == output_name, "full name is not equal to output"
            with allure.step("Checking that email"):
                assert email == output_email, "email is not equal to output"
            with allure.step("Checking that current address"):
                assert current_address == output_current_address, "current address is not equal to output"
            with allure.step("Checking that permanent address"):
                assert permanent_address == output_permanent_address, "permananet address is not equal to output"

    @allure.story("Check Box")
    class TestCheckBoxPage:

        @allure.title("Check box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver)
            check_box_page.open()

            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            checked_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()

            with allure.step("Checking that selected checkboxes match output result"):
                assert checked_checkboxes == output_result, "checkboxes have not been selected"

    @allure.story("Radio Button")
    class TestRadioButtonPage:

        @allure.title("Yes radio button")
        def test_yes_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver)
            radio_button_page.open()

            radio_button_page.click_yes_radio_button()
            yes_radio_status = radio_button_page.check_status_yes_radio_button()

            with allure.step("Checking that 'Yes' radio button is selected"):
                assert yes_radio_status, "'Yes' radio button is not selected"

        @allure.title("Impressive radio button")
        def test_impressive_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver)
            radio_button_page.open()

            radio_button_page.click_impressive_radio_button()
            impressive_radio_status = radio_button_page.check_status_impressive_radio_button()

            with allure.step("Verify that 'Impressive' radio button is selected"):
                assert impressive_radio_status, "'Impressive' radio button is not selected"

        @allure.title("No radio button")
        @pytest.mark.xfail(reason="the no radio button is not clickable")
        def test_no_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver)
            radio_button_page.open()

            radio_button_page.click_no_radio_button()
            no_radio_status = radio_button_page.check_status_no_radio_button()

            with allure.step("Checking that 'No' radio button is selected"):
                assert no_radio_status, "'No' radio button is not selected"

    @allure.story("Web Tables")
    class TestWebTablesPage:

        @allure.title("Web table add person")
        def test_web_table_add_person(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()

            web_tables_page.add_20_rows_to_the_table()
            initial_data = web_tables_page.check_new_added_person()
            new_persons = web_tables_page.add_new_person(random.randint(1, 10))
            table_result = web_tables_page.check_new_added_person()
            initial_data_set = set(tuple(person) for person in initial_data)
            table_result_set = set(tuple(person) for person in table_result)
            new_persons_set = set(tuple(person) for person in new_persons)
            expected_data_set = initial_data_set.union(new_persons_set)

            for person in new_persons:
                with allure.step(f"Checking that the added person {person} is found in the table"):
                    assert tuple(person) in table_result_set, "the added person was not found in the table"

            with allure.step("Checking that the table result matches the expected data set"):
                assert expected_data_set == table_result_set, "no users have been added to the table"

        @allure.title("Web table search person")
        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()

            key_word = web_tables_page.add_new_person()[0][random.randint(0, 5)]
            web_tables_page.search_some_person(key_word)
            table_result = web_tables_page.check_search_person()

            with allure.step(f"Checking that the person with keyword '{key_word}' is found in the table"):
                assert key_word in table_result, "the person was not found in the table"

        @allure.title("Web table update person info")
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

            with allure.step("Checking that the user's data matches after the update, excluding the updated field"):
                assert old_data_to_compare == new_data_to_compare, (
                    f"the user's data does not match after update, excluding field_index {field_index}"
                )
            with allure.step("Checking that the updated value is correctly displayed in the table"):
                assert updated_value == new_table_result[field_index], "the person card has not been changed"

        @allure.title("Web table delete person")
        def test_web_table_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()

            email = web_tables_page.add_new_person()[0][3]
            web_tables_page.search_some_person(email)
            web_tables_page.delete_person()
            text = web_tables_page.check_deleted()

            with allure.step("Checking that the person has been deleted from the table"):
                assert text == "No rows found", (
                    "the person has not been deleted"
                )

        @allure.title("Web table change count row")
        def test_web_table_change_count_row(self, driver):
            web_tables_page = WebTablesPage(driver)
            web_tables_page.open()

            count = web_tables_page.select_up_to_some_rows()
            with allure.step("Checking that the number of rows in the table has been updated correctly"):
                assert count == [5, 10, 20, 25, 50, 100], (
                    "the number of rows in the table has not been changed or has changed incorrectly"
                )

    @allure.story("Buttons")
    class TestButtonsPage:

        @allure.title("Double click on the button")
        def test_double_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver)
            buttons_page.open()

            buttons_page.double_click_on_the_button()
            message = buttons_page.check_double_click_on_the_button()

            with allure.step("Checking that the double click button action produces the correct message"):
                assert message == "You have done a double click", (
                    "the double click button did not work"
                )

        @allure.title("Right click on the button")
        def test_right_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver)
            buttons_page.open()

            buttons_page.right_click_on_the_button()
            message = buttons_page.check_right_click_on_the_button()

            with allure.step("Checking that the right click button action produces the correct message"):
                assert message == "You have done a right click", (
                    "the right click button did not work"
                )

        @allure.title("Click on the button")
        def test_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver)
            buttons_page.open()

            buttons_page.click_on_the_button()
            message = buttons_page.check_click_on_the_button()

            with allure.step("Checking that the click button action produces the correct message"):
                assert message == "You have done a dynamic click", (
                    "the click button did not work"
                )

    @allure.story("Links")
    class TestLinksPage:

        @allure.title("Switching to new home page")
        def test_of_switching_to_new_home_page(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            main_page = links_page.get_current_window_handle()
            links_page.click_on_the_home_link()
            list_page = links_page.get_list_windows_handles()
            links_page.switch_to_new_windows(list_page[1])
            url = links_page.get_url_page()
            new_page = links_page.get_current_window_handle()

            with allure.step("Checking that the switch to the new window was successful"):
                assert main_page != new_page, (
                    "error switching between tabs"
                )
            with allure.step("Checking that the URL of the new page matches the expected home page URL"):
                assert url == "https://demoqa.com/", (
                    "the link does not match the home page"
                )

        @allure.title("Switching to dynamic link")
        def test_of_switching_to_dynamic_link(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            main_page = links_page.get_current_window_handle()
            links_page.click_on_the_dynamic_link()
            list_page = links_page.get_list_windows_handles()
            links_page.switch_to_new_windows(list_page[1])
            url = links_page.get_url_page()
            new_page = links_page.get_current_window_handle()

            with allure.step("Checking that the switch to the new window was successful"):
                assert main_page != new_page, (
                    "error switching between tabs"
                )
            with allure.step("Checking that the URL of the new page matches the expected home page URL"):
                assert url == "https://demoqa.com/", (
                    "the link does not match the home page"
                )

        @allure.title("API created")
        def test_api_created(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            response_status_code, response_reason = links_page.check_on_the_api_created()

            with allure.step("Checking that the API response status code is 201"):
                assert response_status_code == 201, (
                    "the status code does not match the response"
                )
            with allure.step("Checking that the API response status text is 'Created'"):
                assert response_reason == 'Created', (
                    "the status text does not match the response"
                )

        @allure.title("API no content")
        def test_api_no_content(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            response_status_code, response_reason = links_page.check_on_the_api_no_content()

            with allure.step("Checking that the API response status code is 204"):
                assert response_status_code == 204, (
                    "the status code does not match the response"
                )
            with allure.step("Checking that the API response status text is 'No Content'"):
                assert response_reason == 'No Content', (
                    "the status text does not match the response"
                )

        @allure.title("API moved")
        def test_api_moved(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            response_status_code, response_reason = links_page.check_on_the_api_moved()

            with allure.step("Checking that the API response status code is 301"):
                assert response_status_code == 301, (
                    "the status code does not match the response"
                )
            with allure.step("Checking that the API response status text is 'Moved Permanently'"):
                assert response_reason == 'Moved Permanently', (
                    "the status text does not match the response"
                )

        @allure.title("API bad request")
        def test_api_bad_request(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            response_status_code, response_reason = links_page.check_on_the_api_bad_request()

            with allure.step("Checking that the API response status code is 400"):
                assert response_status_code == 400, (
                    "the status code does not match the response"
                )
            with allure.step("Checking that the API response status text is 'Bad Request'"):
                assert response_reason == 'Bad Request', (
                    "the status text does not match the response"
                )

        @allure.title("API unauthorized")
        def test_api_unauthorized(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            response_status_code, response_reason = links_page.check_on_the_api_unauthorized()

            with allure.step("Checking that the API response status code is 401"):
                assert response_status_code == 401, (
                    "the status code does not match the response"
                )
            with allure.step("Checking that the API response status text is 'Unauthorized'"):
                assert response_reason == 'Unauthorized', (
                    "the status text does not match the response"
                )

        @allure.title("API forbidden")
        def test_api_forbidden(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            response_status_code, response_reason = links_page.check_on_the_api_forbidden()

            with allure.step("Checking that the API response status code is 403"):
                assert response_status_code == 403, (
                    "the status code does not match the response"
                )
            with allure.step("Checking that the API response status text is 'Forbidden'"):
                assert response_reason == 'Forbidden', (
                    "the status text does not match the response"
                )

        @allure.title("API not found")
        def test_api_not_found(self, driver):
            links_page = LinksPage(driver)
            links_page.open()

            response_status_code, response_reason = links_page.check_on_the_api_not_found()

            with allure.step("Checking that the API response status code is 404"):
                assert response_status_code == 404, (
                    "the status code does not match the response"
                )
            with allure.step("Checking that the API response status text is 'Not Found'"):
                assert response_reason == 'Not Found', (
                    "the status text does not match the response"
                )

    @allure.story("Upload and Download")
    class TestUploadAndDownloadPage:

        @allure.title("Download file")
        def test_download_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver)
            upload_and_download_page.open()

            upload_and_download_page.create_download_dir()
            upload_and_download_page.click_of_the_download_button()
            name_file = upload_and_download_page.get_name_download_file()
            upload_and_download_page.delite_download_file()

            with allure.step("Checking that the name of the downloaded file is 'sampleFile.jpeg'"):
                assert name_file == "sampleFile.jpeg", (
                    "the name of the downloaded file does not match"
                )

        @allure.title("Upload file")
        def test_upload_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver)
            upload_and_download_page.open()

            upload_and_download_page.create_download_dir()
            created_file_name = upload_and_download_page.upload_file()
            uploaded_file_name = upload_and_download_page.getting_name_of_the_uploaded_file()
            upload_and_download_page.delite_download_file()

            with allure.step("Checking that the name of the uploaded file matches the created file name"):
                assert created_file_name == uploaded_file_name, "the name of the uploaded file does not match"

    @allure.story("Dynamic Properties")
    class TestDynamicPropertiesPage:

        @allure.title("Click the button after 5 seconds")
        def test_click_the_button_after_5_seconds(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            dynamic_properties_page.open()

            dynamic_properties_page.click_the_button_after_5_seconds()
            click_button_status = dynamic_properties_page.check_click_the_button_after_5_seconds()

            with allure.step("Checking that the button was clicked after 5 seconds"):
                assert click_button_status is True, "the button was not clicked"

        @allure.title("Button color change")
        def test_button_color_change(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            dynamic_properties_page.open()

            color_button_before, color_button_after = dynamic_properties_page.checking_for_button_color_changes()

            with allure.step("Checking that the color of the button has changed"):
                assert color_button_before != color_button_after, "the color of the button was not changed"

        @allure.title("Appearance of an invisible button")
        def test_appearance_of_an_invisible_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver)
            dynamic_properties_page.open()

            button_invisibility_status = dynamic_properties_page.check_button_is_invisible()
            button_visibility_status = dynamic_properties_page.check_button_is_visible()

            with allure.step("Checking that the button is invisible"):
                assert button_invisibility_status is True, "the button is not invisible"

            with allure.step("Checking that the button has become visible"):
                assert button_visibility_status is True, "the button has not become visible"
