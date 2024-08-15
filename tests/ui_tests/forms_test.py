from pages.forms_page import PracticeFormPage


class TestForms:
    class TestPracticeFormPage:
        def test_filling_out_the_student_registration_form(self, driver):
            practice_form_page = PracticeFormPage(driver)
            practice_form_page.open()

            firstname_lastname, email, mobile, current_address = (
                practice_form_page.fill_name_email_mobile_current_address_fields()
            )
            gender = practice_form_page.fill_gender()
            day_month_year = practice_form_page.fill_date_of_birth()
            subjects = practice_form_page.fill_subjects_field()
            hobbies = practice_form_page.fill_hobbies_check_box()
            img = practice_form_page.uploading_a_photo()
            state_and_city = practice_form_page.fill_state_and_city_select()
            practice_form_page.click_to_submit_button()
            tabel_result = practice_form_page.form_result()

            actual_result = [
                firstname_lastname, email, gender, mobile,
                day_month_year, subjects, hobbies, img,
                current_address, state_and_city
            ]

            assert actual_result == tabel_result, "the data does not match the result of the table"
