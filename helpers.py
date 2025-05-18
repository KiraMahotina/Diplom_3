import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import allure
from faker import Faker


fake = Faker('ru_RU')


@allure.step("Генерация валидного набора данных для создания нового пользователя")
def generate_valid_creating_user_data():
    email = fake.email()
    password = fake.password(length=8, special_chars=False)
    name = fake.first_name()
    return email, password, name


class Helpers:

    @allure.step("Генерация данных для создания нового пользователя")
    def generate_new_user_and_return_email_password_name_dict(self):
        email, password, name = generate_valid_creating_user_data()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload
