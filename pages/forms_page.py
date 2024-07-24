import os
import random
import shutil
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_student_subjects, generated_image, \
    generated_student_state_and_city
from pages.base_page import BasePage
from config.links import FormsPageLinks
from locators.forms_page_locators import PracticeFormPageLocators
from selenium.webdriver.support.select import Select


class PracticeFormPage(BasePage):
    PAGE_URL = FormsPageLinks.PRACTICE_FORM
    locators = PracticeFormPageLocators()

    def fill_name_email_mobile_current_address_fields(self):
        person = next(generated_person())
        self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(person.email)
        self.element_is_visible(self.locators.MOBILE_NUMBER_FIELD).send_keys(person.mobile)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_FIELD).send_keys(person.current_address)
        return f"{person.firstname} {person.lastname}", person.email, str(person.mobile), person.current_address

    def fill_gender(self):
        gender_list = self.elements_are_present(self.locators.GENDER_RADIO_BUTTON)
        random_gender = random.choice(gender_list)
        random_gender.click()
        return random_gender.text

    def fill_date_of_birth(self):
        self.element_is_visible(self.locators.DATE_OF_BIRTH_CALENDAR).click()
        dropdown_calendar_month = Select(self.element_is_visible(self.locators.CALENDAR_MONTH_SELECT))
        dropdown_calendar_month.select_by_value(str(random.randint(0, 11)))
        dropdown_calendar_year = Select(self.element_is_visible(self.locators.CALENDAR_YEAR_SELECT))
        dropdown_calendar_year.select_by_value(str(random.randint(1900, 2100)))
        month_and_year = self.element_is_present(self.locators.GET_MONTH_AND_YEAR).text
        day_list = self.elements_are_present(self.locators.CALENDAR_DAY)
        random_day = random.choice(day_list)
        random_day.click()
        day = self.element_is_visible(self.locators.DATE_OF_BIRTH_CALENDAR).get_attribute("value")
        return f"{day[:2]} {month_and_year.replace(" ", ",")}"

    def fill_subjects_field(self):
        subjects = generated_student_subjects()
        for subject in subjects:
            self.element_is_visible(self.locators.SUBJECTS_FIELD).send_keys(subject)
            self.element_is_visible(self.locators.SUBJECTS_FIELD).send_keys(Keys.TAB)
        return ', '.join(subjects)

    def fill_hobbies_check_box(self):
        data = []
        hobbies_check_box_list = self.elements_are_present(self.locators.HOBBIES_CHECK_BOX)
        num_to_select = random.randint(1, len(hobbies_check_box_list))
        checkboxes_to_select = random.sample(hobbies_check_box_list, num_to_select)
        for checkbox in checkboxes_to_select:
            checkbox.click()
            data.append(checkbox.text)
        return ', '.join(data)

    def uploading_a_photo(self):
        self.create_download_dir()
        img = generated_image()
        self.element_is_visible(self.locators.PICTURE_CHOOSE_FILE_BUTTON).send_keys(img)
        self.delite_download_file()
        img_name = img.split()[-1].split('/')[-1]
        return img_name
    def create_download_dir(self):
        dir_path = os.path.join(os.getcwd(), "downloads")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def delite_download_file(self):
        dir_path = os.path.join(os.getcwd(), "downloads")
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            shutil.rmtree(dir_path)

    def fill_state_and_city_select(self):
        state, city = generated_student_state_and_city()
        select_state = self.element_is_visible(self.locators.SELECT_STATE)
        select_state.send_keys(state)
        select_state.send_keys(Keys.TAB)
        select_city = self.element_is_visible(self.locators.SELECT_CITY)
        select_city.send_keys(city)
        select_city.send_keys(Keys.TAB)
        return f"{state} {city}"

    def click_to_submit_button(self):
        submit_button = self.element_is_present(self.locators.SUBMIT_REGISTRATION_FORM_BUTTON)
        self.go_to_element(submit_button)
        submit_button.click()

    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
