import os
import random
from config.data import Person
from faker import Faker
from PIL import Image

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.random_number(10, True),

    )


def generated_file():
    file_name = f"{random.randint(0, 999)}.txt"
    file_path = os.path.join(os.getcwd(), "downloads", file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Hellow World{random.randint(0, 999)}")
    return file_name, file_path


def generated_student_subjects():
    subjects = [
        "Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
        "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"
    ]
    num_subjects = random.randint(1, len(subjects))
    selected_subjects = random.sample(subjects, num_subjects)
    return selected_subjects


def generated_image():
    width = random.randint(100, 1000)
    height = random.randint(100, 1000)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    downloads_folder = os.path.join(os.getcwd(), 'downloads')
    img = Image.new('RGB', (width, height), color)
    file_path = os.path.join(downloads_folder, 'output_image.png')
    img.save(file_path)
    return file_path


def generated_student_state_and_city():
    states_and_city = {
        "NCR": [
            "Delhi",
            "Gurgaon",
            "Noida"
        ],
        "Uttar Pradesh": [
            "Agra",
            "Lucknow",
            "Merrut"
        ],
        "Haryana": [
            "Karnal",
            "Panipat"
        ],
        "Rajasthan": [
            "Jaipur",
            "Jaiselmer"
        ]
    }
    random_region = random.choice(list(states_and_city.keys()))
    cities = states_and_city[random_region]
    random_city = random.choice(cities)
    return random_region, random_city
