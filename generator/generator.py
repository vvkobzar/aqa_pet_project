import os
import random

from config.data import Person
from faker import Faker

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

    )


def generated_file():
    file_name = f"{random.randint(0, 999)}.txt"
    file_path = os.path.join(os.getcwd(), "downloads", file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Hellow World{random.randint(0, 999)}")
    return file_name, file_path
