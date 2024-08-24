import os
import allure
import shutil
import random

from selenium.webdriver import Keys
from pages.base_page import BasePage
from config.links import FormsPageLinks
from locators.forms_page_locators import PracticeFormPageLocators
from generator.generator import generated_person, generated_student_subjects, generated_image, \
    generated_student_state_and_city


class PracticeFormPage(BasePage):
    PAGE_URL = FormsPageLinks.PRACTICE_FORM
    locators = PracticeFormPageLocators()

    @allure.step("Fill name, email, mobile, and current address fields")
    def fill_name_email_mobile_current_address_fields(self):
        person = next(generated_person())
        with allure.step(f"Fill first name field with '{person.firstname}'"):
            self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(person.firstname)
        with allure.step(f"Fill last name field with '{person.lastname}'"):
            self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(person.lastname)
        with allure.step(f"Fill email field with '{person.email}'"):
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(person.email)
        with allure.step(f"Fill mobile number field with '{person.mobile}'"):
            self.element_is_visible(self.locators.MOBILE_NUMBER_FIELD).send_keys(person.mobile)
        with allure.step(f"Fill current address field with '{person.current_address}'"):
            self.element_is_visible(self.locators.CURRENT_ADDRESS_FIELD).send_keys(person.current_address)
        return f"{person.firstname} {person.lastname}", person.email, str(person.mobile), person.current_address

    @allure.step("Choose gender")
    def fill_gender(self):
        gender_list = self.elements_are_present(self.locators.GENDER_RADIO_BUTTON)
        random_gender = random.choice(gender_list)
        with allure.step(f"Gender: '{random_gender.text}'"):
            random_gender.click()
        return random_gender.text

    @allure.step("Fill date of birth")
    def fill_date_of_birth(self):
        self.element_is_visible(self.locators.DATE_OF_BIRTH_CALENDAR).click()
        self.select_by_value(self.locators.CALENDAR_MONTH_SELECT, random.randint(0, 11))
        self.select_by_value(self.locators.CALENDAR_YEAR_SELECT, random.randint(1900, 2100))
        month_and_year = self.element_is_visible(self.locators.GET_MONTH_AND_YEAR).text
        month, year = month_and_year.split()
        day_list = self.elements_are_present(self.locators.DATE_SELECT_DAY(month))
        selected_day = random.choice(day_list)
        selected_day_text = selected_day.text
        format_day = self.format_date_number(int(selected_day_text))
        selected_day.click()
        selected_date = f"{format_day} {month},{year}"
        with allure.step(f"Selected date : {selected_date}'"):
            return selected_date

    @allure.step("Fill subjects field")
    def fill_subjects_field(self):
        subjects = generated_student_subjects()
        for subject in subjects:
            with allure.step(f"Add subject '{subject}'"):
                self.element_is_visible(self.locators.SUBJECTS_FIELD).send_keys(subject)
                self.element_is_visible(self.locators.SUBJECTS_FIELD).send_keys(Keys.TAB)
        return ', '.join(subjects)

    @allure.step("Choose hobbies checkboxes")
    def fill_hobbies_check_box(self):
        data = []
        hobbies_check_box_list = self.elements_are_present(self.locators.HOBBIES_CHECK_BOX)
        num_to_select = random.randint(1, len(hobbies_check_box_list))
        checkboxes_to_select = random.sample(hobbies_check_box_list, num_to_select)
        for checkbox in checkboxes_to_select:
            with allure.step(f"Select hobby '{checkbox.text}'"):
                checkbox.click()
                data.append(checkbox.text)
        return ', '.join(data)

    @allure.step("Upload a photo")
    def uploading_a_photo(self):
        self.create_download_dir()
        img = generated_image()
        with allure.step(f"Uploading image '{img.split('/')[-1]}'"):
            self.element_is_visible(self.locators.PICTURE_CHOOSE_FILE_BUTTON).send_keys(img)
        self.delete_download_file()
        img_name = img.split()[-1].split('/')[-1]
        return img_name

    @allure.step("Create download directory")
    def create_download_dir(self):
        dir_path = os.path.join(os.getcwd(), "downloads")
        if not os.path.exists(dir_path):
            with allure.step("Creating download directory"):
                os.makedirs(dir_path)

    @allure.step("Delete download directory")
    def delete_download_file(self):
        dir_path = os.path.join(os.getcwd(), "downloads")
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            with allure.step("Deleting download directory"):
                shutil.rmtree(dir_path)

    @allure.step("Select state and city")
    def fill_state_and_city_select(self):
        state, city = generated_student_state_and_city()
        with allure.step(f"Selecting state '{state}' and city '{city}'"):
            select_state = self.element_is_visible(self.locators.SELECT_STATE)
            select_state.send_keys(state)
            select_state.send_keys(Keys.TAB)
            select_city = self.element_is_visible(self.locators.SELECT_CITY)
            select_city.send_keys(city)
            select_city.send_keys(Keys.TAB)
        return f"{state} {city}"

    @allure.step("Click submit button")
    def click_to_submit_button(self):
        submit_button = self.element_is_present(self.locators.SUBMIT_REGISTRATION_FORM_BUTTON)
        with allure.step("Clicking submit button"):
            self.go_to_element(submit_button)
            submit_button.click()

    @allure.step("Retrieve data from the form")
    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data

    @staticmethod
    def format_date_number(number):
        if 1 <= number <= 9:
            return f"{number:02}"
        else:
            return str(number)
