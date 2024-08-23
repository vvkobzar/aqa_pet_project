import os
import random
import allure

from config.data import Person
from faker import Faker
from PIL import Image

faker_ru = Faker('ru_RU')
Faker.seed()


@allure.step("Generate random person data")
def generated_person():
    with allure.step("Generating person details"):
        person = Person(
            full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
            firstname=faker_ru.first_name(),
            lastname=faker_ru.last_name(),
            username=faker_ru.user_name(),
            password=faker_ru.password(),
            age=random.randint(10, 80),
            salary=random.randint(10000, 100000),
            department=faker_ru.job(),
            email=faker_ru.email(),
            current_address=faker_ru.address(),
            permanent_address=faker_ru.address(),
            mobile=faker_ru.random_number(10, True),
        )
    allure.attach(str(person), name="Generated Person", attachment_type=allure.attachment_type.JSON)
    yield person


@allure.step("Generate a random text file")
def generated_file():
    file_name = f"{random.randint(0, 999)}.txt"
    file_path = os.path.join(os.getcwd(), "downloads", file_name)
    with allure.step(f"Creating file: {file_path}"):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Hello World {random.randint(0, 999)}")
    allure.attach.file(file_path, name=file_name, attachment_type=allure.attachment_type.TEXT)
    return file_name, file_path


@allure.step("Generate random student subjects")
def generated_student_subjects():
    subjects = [
        "Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
        "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"
    ]
    num_subjects = random.randint(1, len(subjects))
    selected_subjects = random.sample(subjects, num_subjects)
    allure.attach(str(selected_subjects), name="Selected Subjects", attachment_type=allure.attachment_type.JSON)
    return selected_subjects


@allure.step("Generate random image")
def generated_image():
    width = random.randint(100, 1000)
    height = random.randint(100, 1000)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    downloads_folder = os.path.join(os.getcwd(), 'downloads')
    file_path = os.path.join(downloads_folder, 'output_image.png')
    with allure.step(f"Creating image {file_path} with size ({width}x{height}) and color {color}"):
        img = Image.new('RGB', (width, height), color)
        img.save(file_path)
    allure.attach.file(file_path, name="Generated Image", attachment_type=allure.attachment_type.PNG)
    return file_path


@allure.step("Generate random state and city")
def generated_student_state_and_city():
    states_and_city = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }
    random_region = random.choice(list(states_and_city.keys()))
    cities = states_and_city[random_region]
    random_city = random.choice(cities)
    allure.attach(f"State: {random_region}, City: {random_city}", name="Selected State and City", attachment_type=allure.attachment_type.TEXT)
    return random_region, random_city


@allure.step("Generate random color names")
def generator_color_names():
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Voilet', 'Indigo', 'Magenta', 'Aqua']
    num_subjects = random.randint(1, len(colors))
    selected_colors = random.sample(colors, num_subjects)
    allure.attach(str(selected_colors), name="Selected Colors", attachment_type=allure.attachment_type.JSON)
    return selected_colors


@allure.step("Randomly retrieve ISBN from book list")
def random_selection_of_isbn_from_the_book_list(books):
    with allure.step("Selecting random ISBNs from book list"):
        isbn = [book.isbn for book in books]
        num_subjects = random.randint(1, len(isbn))
        isbn_books = random.sample(isbn, num_subjects)
        allure.attach(str(isbn_books), name="Selected ISBNs", attachment_type=allure.attachment_type.JSON)
        return isbn_books
