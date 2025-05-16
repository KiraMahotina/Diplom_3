import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import allure
from base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке: "Восстановить пароль" на странице авторизации')
    def click_recovery_password_button(self):
        self.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Клик по полю: "Email" на странице авторизации')
    def click_email_input(self):
        self.click_element(LoginPageLocators.EMAIL_INPUT)

    @allure.step('Клик по кнопке: "Войти" на странице авторизации')
    def click_enter_button(self):
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Ожидание когда поле "Email" станет кликабельным')
    def wait_for_clickable_email_input(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)

    @allure.step('Ввод "email" в поле "Email" на странице авторизации')
    def input_email(self, data):
        self.input_text(LoginPageLocators.EMAIL_INPUT, data["email"])

    @allure.step('Ввод "password" в поле "Пароль" на странице авторизации')
    def input_correct_password(self, data):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, data["password"])

    @allure.step('Заполнение данных пользователя на странице авторизации')
    def login_page_authorization(self, data):
        self.wait_for_clickable_email_input()
        self.input_email(data)
        self.input_correct_password(data)
        self.click_enter_button()