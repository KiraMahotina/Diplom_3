import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import pytest
import allure
import requests
from selenium import webdriver
from urls import Urls, UrlsAPI
from api import Api


@pytest.fixture(params=['firefox', 'chrome'], autouse=True)
def driver(request):
    driver = None
    with allure.step(f'Открываем браузер {request.param}'):
        if request.param == 'firefox':
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(Urls.BASE_PAGE_URL)
        elif request.param == 'chrome':
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(Urls.BASE_PAGE_URL)
    yield driver
    with allure.step(f'Закрываем браузер {request.param}'):
        driver.quit()


@pytest.fixture(autouse=True)
def token_create_new_user_and_delete():
    api = Api()
    token_data = api.create_new_user_authorization_get_token()
    yield token_data
    if token_data:
        with allure.step(f"Отправка PATCH-запроса на {UrlsAPI.API_DELETE_USER} для удаления пользователя"):
            requests.delete(UrlsAPI.API_DELETE_USER, headers=token_data)