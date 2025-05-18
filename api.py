import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import requests
import allure
from urls import UrlsAPI
from helpers import generate_valid_creating_user_data


class Api:


    @allure.step("Создание нового пользователя, авторизация и получение токена")
    def create_new_user_authorization_get_token(self):
        with allure.step("Генерация данных нового пользователя"):
            email, password, name = generate_valid_creating_user_data()
            payload = {
                "email": email,
                "password": password,
                "name": name
            }
            with allure.step(f"Отправка POST-запроса на {UrlsAPI.API_POST_CREATING_USER} для создания нового пользователя"):
                response = requests.post(UrlsAPI.API_POST_CREATING_USER, data=payload)

        with allure.step(f"Отправка POST-запроса на {UrlsAPI.API_POST_LOGIN_USER} для авторизации пользователя"):
            token_response = requests.post(UrlsAPI.API_POST_LOGIN_USER, data={"email": email,"password": password})
            if token_response.status_code == 200 and response.json()["success"] == True:
                with allure.step(f"Извлечение токена из ответа и передача "):
                    token = token_response.json().get("accessToken")
                    return {"Authorization": token, "email": email, "password": password}
        return None
    