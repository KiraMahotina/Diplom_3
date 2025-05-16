import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import allure
from base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Личный кабинет" в хедере страницы')
    def click_personal_account_button(self):
        self.click_element(HeaderPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "Конструктор" в хедере страницы')
    def click_constructor_button(self):
        self.click_element(HeaderPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов" в хедере страницы')
    def click_order_list_button(self):
        self.click_element(HeaderPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Ожидание отсутствия "login" в текущем URL')
    def wait_for_text_login_not_in_url(self):
        self.wait_for_text_not_in_url(HeaderPageLocators.TEXT_LOGIN)

    @allure.step('Ожидание появления кнопки "Лента заказов" в хедере страницы')
    def wait_for_presence_orders_history_button(self):
        self.wait_for_presence_of_element_located(HeaderPageLocators.ORDER_LIST_BUTTON)