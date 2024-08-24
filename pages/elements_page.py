import allure
import os
import time
import shutil
import random
import requests

from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from config.links import ElementsPageLinks
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators


class TextBoxPage(BasePage):
    PAGE_URL = ElementsPageLinks.TEXT_BOX
    locators = TextBoxPageLocators()

    @allure.step("Fill all fields in the text box form")
    def fill_all_fields(self):
        with allure.step("Fill in the 'Full Name' field"):
            person_info = next(generated_person())
            full_name = person_info.full_name
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)

        with allure.step("Fill in the 'Email' field"):
            email = person_info.email
            self.element_is_visible(self.locators.EMAIL).send_keys(email)

        with allure.step("Fill in the 'Current Address' field"):
            current_address = person_info.current_address
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)

        with allure.step("Fill in the 'Permanent Address' field"):
            permanent_address = person_info.permanent_address
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)

        with allure.step("Click the 'Submit' button"):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        return full_name, email, current_address, permanent_address

    @allure.step("Check the filled form details")
    def check_filled_form(self):
        with allure.step("Retrieve and verify the 'Full Name' field"):
            full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]

        with allure.step("Retrieve and verify the 'Email' field"):
            email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]

        with allure.step("Retrieve and verify the 'Current Address' field"):
            current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]

        with allure.step("Retrieve and verify the 'Permanent Address' field"):
            permananet_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permananet_address


class CheckBoxPage(BasePage):
    PAGE_URL = ElementsPageLinks.CHECK_BOX
    locators = CheckBoxPageLocators()

    @allure.step("Open full checkbox list")
    def open_full_list(self):
        with allure.step("Click 'Expand All' button to view all checkboxes"):
            self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("Click a random checkbox")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEMS_LIST)
        count = 21
        while count != 0:
            with allure.step(f"Clicking on checkbox item {count}"):
                item = item_list[random.randint(1, 15)]
                self.go_to_element(item)
                item.click()
                count -= 1

    @allure.step("Get checked checkboxes")
    def get_checked_checkboxes(self):
        with allure.step("Retrieve the list of checked checkboxes"):
            checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
            data = [box.find_element(*self.locators.TITLE_ITEM).text for box in checked_list]
            return str(data).replace(" ", "").replace(".doc", "").lower()

    @allure.step("Get output result of the checkbox")
    def get_output_result(self):
        with allure.step("Retrieve the output result of the checked checkboxes"):
            result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
            data = [result.text for result in result_list]
            return str(data).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    PAGE_URL = ElementsPageLinks.RADIO_BUTTON
    locators = RadioButtonPageLocators()

    @allure.step("Click 'Yes' radio button")
    def click_yes_radio_button(self):
        with allure.step("Click 'Yes' radio button"):
            self.element_is_visible(self.locators.YES_RADIO_ACTIVE).click()

    @allure.step("Click 'Impressive' radio button")
    def click_impressive_radio_button(self):
        with allure.step("Click 'Impressive' radio button"):
            self.element_is_visible(self.locators.IMPRESSIVE_RADIO_ACTIVE).click()

    @allure.step("Click 'No' radio button")
    def click_no_radio_button(self):
        with allure.step("Click 'No' radio button"):
            self.element_is_visible(self.locators.NO_RADIO_ACTIVE).click()

    @allure.step("Check status of 'Yes' radio button")
    def check_status_yes_radio_button(self):
        with allure.step("Check if 'Yes' radio button is selected"):
            return self.element_is_present(self.locators.YES_RADIO_STATUS).is_selected()

    @allure.step("Check status of 'Impressive' radio button")
    def check_status_impressive_radio_button(self):
        with allure.step("Check if 'Impressive' radio button is selected"):
            return self.element_is_present(self.locators.IMPRESSIVE_RADIO_STATUS).is_selected()

    @allure.step("Check status of 'No' radio button")
    def check_status_no_radio_button(self):
        with allure.step("Check if 'No' radio button is selected"):
            return self.element_is_present(self.locators.NO_RADIO_STATUS).is_selected()


class WebTablesPage(BasePage):
    PAGE_URL = ElementsPageLinks.WEB_TABLES
    locators = WebTablesPageLocators()

    @allure.step("Add new person(s) to the web table")
    def add_new_person(self, count=1):
        added_persons = []
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            with allure.step(f"Adding new person: {firstname} {lastname}"):
                self.element_is_visible(self.locators.ADD_BUTTON).click()
                self.element_is_visible(self.locators.FIRST_NAME).send_keys(firstname)
                self.element_is_visible(self.locators.LAST_NAME).send_keys(lastname)
                self.element_is_visible(self.locators.EMAIL).send_keys(email)
                self.element_is_visible(self.locators.AGE).send_keys(age)
                self.element_is_visible(self.locators.SALARY).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
                self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

            new_person = [firstname, lastname, str(age), email, str(salary), department]
            added_persons.append(new_person)
            count -= 1
        return added_persons

    @allure.step("Check newly added person(s) in the web table")
    def check_new_added_person(self):
        with allure.step("Check the newly added person(s) in the web table"):
            person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
            data = [person.text.splitlines() for person in person_list]
            return data

    @allure.step("Search for a person by keyword")
    def search_some_person(self, key_word):
        with allure.step(f"Search for a person with keyword: {key_word}"):
            search_field = self.element_is_visible(self.locators.SEARCH_FIELD)
            search_field.click()
            search_field.clear()
            search_field.send_keys(key_word)

    @allure.step("Check search result for a person")
    def check_search_person(self):
        with allure.step("Check the search result for the person"):
            return self.element_is_visible(self.locators.ROW_PERSON).text.splitlines()

    @allure.step("Update person information")
    def update_person_info(self):
        with allure.step("Update information for a person"):
            person_info = next(generated_person())
            fields = {
                'firstname': person_info.firstname,
                'lastname': person_info.lastname,
                'age': person_info.age,
                'email': person_info.email,
                'salary': person_info.salary,
                'department': person_info.department
            }
            field_to_update = random.choice(list(fields.keys()))
            field_index = list(fields.keys()).index(field_to_update)

            self.element_is_visible(self.locators.UPDATE_BUTTON).click()

            with allure.step(f"Updating field '{field_to_update}' with value '{fields[field_to_update]}'"):
                if field_to_update == 'firstname':
                    self.element_is_visible(self.locators.FIRST_NAME).clear()
                    self.element_is_visible(self.locators.FIRST_NAME).send_keys(fields['firstname'])
                if field_to_update == 'lastname':
                    self.element_is_visible(self.locators.LAST_NAME).clear()
                    self.element_is_visible(self.locators.LAST_NAME).send_keys(fields['lastname'])
                if field_to_update == 'email':
                    self.element_is_visible(self.locators.EMAIL).clear()
                    self.element_is_visible(self.locators.EMAIL).send_keys(fields['email'])
                if field_to_update == 'age':
                    self.element_is_visible(self.locators.AGE).clear()
                    self.element_is_visible(self.locators.AGE).send_keys(fields['age'])
                if field_to_update == 'salary':
                    self.element_is_visible(self.locators.SALARY).clear()
                    self.element_is_visible(self.locators.SALARY).send_keys(fields['salary'])
                if field_to_update == 'department':
                    self.element_is_visible(self.locators.DEPARTMENT).clear()
                    self.element_is_visible(self.locators.DEPARTMENT).send_keys(fields['department'])
                self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return field_index, str(fields[field_to_update])

    @allure.step("Delete a person from the web table")
    def delete_person(self):
        with allure.step("Delete a person from the web table"):
            self.element_is_visible(self.locators.DELETE_PERSON_BUTTON).click()

    @allure.step("Check if the person was deleted")
    def check_deleted(self):
        return self.element_is_visible(self.locators.NO_ROWS_FOUND).text

    @allure.step("Select a number of rows to display in the web table")
    def select_up_to_some_rows(self):
        data = []
        count_row_select = self.element_is_visible(self.locators.COUNT_ROW_LIST)
        dropdown = Select(count_row_select)
        all_options = dropdown.options
        for option in all_options:
            dropdown.select_by_index(all_options.index(option))
            data.append(self.check_count_rows())
        return data

    @allure.step("Check the count of rows in the web table")
    def check_count_rows(self):
        with allure.step("Get the count of rows in the web table"):
            list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
            return len(list_rows)

    @allure.step("Add 20 rows to the web table")
    def add_20_rows_to_the_table(self):
        with allure.step("Select 20 rows in the web table"):
            count_row_select = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            dropdown = Select(count_row_select)
            dropdown.select_by_value('20')


class ButtonsPage(BasePage):
    PAGE_URL = ElementsPageLinks.BUTTONS
    locators = ButtonsPageLocators()

    @allure.step("Double click on the button")
    def double_click_on_the_button(self):
        with allure.step("Double-click on the 'Double Click Me' button"):
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME_BUTTON))

    @allure.step("Right click on the button")
    def right_click_on_the_button(self):
        with allure.step("Right-click on the 'Right Click Me' button"):
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_ME_BUTTON))

    @allure.step("Click on the button")
    def click_on_the_button(self):
        with allure.step("Click on the 'Click Me' button"):
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()

    @allure.step("Check the result of double click")
    def check_double_click_on_the_button(self):
        with allure.step("Check the result of double-clicking the button"):
            return self.element_is_present(self.locators.DOUBLE_CLICK_MESSAGE).text

    @allure.step("Check the result of right click")
    def check_right_click_on_the_button(self):
        with allure.step("Check the result of right-clicking the button"):
            return self.element_is_present(self.locators.RIGHT_CLICK_MESSAGE).text

    @allure.step("Check the result of a simple click")
    def check_click_on_the_button(self):
        with allure.step("Check the result of clicking the button"):
            return self.element_is_present(self.locators.CLICK_ME_MESSAGE).text


class LinksPage(BasePage):
    PAGE_URL = ElementsPageLinks.LINKS
    locators = LinksPageLocators()

    @allure.step("Click on the home link")
    def click_on_the_home_link(self):
        with allure.step("Click the 'Home' link"):
            self.element_is_visible(self.locators.HOME_LINK).click()

    @allure.step("Click on the dynamic link")
    def click_on_the_dynamic_link(self):
        with allure.step("Click the 'Dynamic Home' link"):
            self.element_is_visible(self.locators.DYNAMIC_HOME_LINK).click()

    @allure.step("Check API created status")
    def check_on_the_api_created(self):
        with allure.step("Check API 'Created' status"):
            response = requests.get(ElementsPageLinks.API_CREATED)
            return response.status_code, response.reason

    @allure.step("Check API no content status")
    def check_on_the_api_no_content(self):
        with allure.step("Check API 'No Content' status"):
            response = requests.get(ElementsPageLinks.API_NO_CONTENT)
            return response.status_code, response.reason

    @allure.step("Check API moved status")
    def check_on_the_api_moved(self):
        with allure.step("Check API 'Moved' status"):
            response = requests.get(ElementsPageLinks.API_MOVED)
            return response.status_code, response.reason

    @allure.step("Check API bad request status")
    def check_on_the_api_bad_request(self):
        with allure.step("Check API 'Bad Request' status"):
            response = requests.get(ElementsPageLinks.API_BAD_REQUEST)
            return response.status_code, response.reason

    @allure.step("Check API unauthorized status")
    def check_on_the_api_unauthorized(self):
        with allure.step("Check API 'Unauthorized' status"):
            response = requests.get(ElementsPageLinks.API_UNAUTHORIZED)
            return response.status_code, response.reason

    @allure.step("Check API forbidden status")
    def check_on_the_api_forbidden(self):
        with allure.step("Check API 'Forbidden' status"):
            response = requests.get(ElementsPageLinks.API_FORBIDDEN)
            return response.status_code, response.reason

    @allure.step("Check API not found status")
    def check_on_the_api_not_found(self):
        with allure.step("Check API 'Not Found' status"):
            response = requests.get(ElementsPageLinks.API_NOT_FOUND)
            return response.status_code, response.reason


class UploadAndDownloadPage(BasePage):
    PAGE_URL = ElementsPageLinks.UPLOAD_AND_DOWNLOAD
    locators = UploadAndDownloadPageLocators()

    @allure.step("Create download directory if it doesn't exist")
    def create_download_dir(self):
        with allure.step("Create download directory if it doesn't exist"):
            dir_path = os.path.join(os.getcwd(), "downloads")
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

    @allure.step("Click on the download button")
    def click_of_the_download_button(self):
        with allure.step("Click the 'Download' button"):
            self.element_is_visible(self.locators.DOWNLOAD_BUTTON).click()
            time.sleep(1)

    @allure.step("Get the name of the downloaded file")
    def get_name_download_file(self):
        with allure.step("Get the name of the downloaded file"):
            dir_path = os.path.join(os.getcwd(), "downloads")
            files = os.listdir(dir_path)
            return files[0]

    @allure.step("Delete the downloaded file")
    def delite_download_file(self):
        with allure.step("Delete the downloaded file"):
            dir_path = os.path.join(os.getcwd(), "downloads")
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                shutil.rmtree(dir_path)

    @allure.step("Upload a file")
    def upload_file(self):
        with allure.step("Upload a file"):
            file_name, path = generated_file()
            self.element_is_visible(self.locators.CHOOSE_FILE_BUTTON).send_keys(path)
            return file_name

    @allure.step("Get the name of the uploaded file")
    def getting_name_of_the_uploaded_file(self):
        with allure.step("Get the name of the uploaded file"):
            file_path = self.element_is_visible(self.locators.UPLOADED_FILE_PATH).text
            return file_path.split('\\')[-1]


class DynamicPropertiesPage(BasePage):
    PAGE_URL = ElementsPageLinks.DYNAMIC_PROPERTIES
    locators = DynamicPropertiesPageLocators()

    @allure.step("Click the button that will enable after 5 seconds")
    def click_the_button_after_5_seconds(self):
        with allure.step("Click the button that will enable after 5 seconds"):
            self.element_is_clickable(self.locators.WILL_ENABLE_5_SECONDS_BUTTON).click()

    @allure.step("Check if the button is enabled after 5 seconds")
    def check_click_the_button_after_5_seconds(self):
        with allure.step("Check if the button is enabled after 5 seconds"):
            return self.element_is_visible(self.locators.WILL_ENABLE_5_SECONDS_BUTTON).is_enabled()

    @allure.step("Check if button color changes")
    def checking_for_button_color_changes(self):
        with allure.step("Check if the button color changes"):
            color_button = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON)
            color_button_before = color_button.value_of_css_property('color')
            time.sleep(5)
            color_button_after = color_button.value_of_css_property('color')
            return color_button_before, color_button_after

    @allure.step("Check if the button is invisible")
    def check_button_is_invisible(self):
        with allure.step("Check if the button is invisible"):
            return self.elements_is_not_visible(self.locators.INVISIBLE_BUTTON)

    @allure.step("Check if the button is visible")
    def check_button_is_visible(self):
        with allure.step("Check if the button is visible"):
            return self.element_is_visible(self.locators.INVISIBLE_BUTTON).is_displayed()
