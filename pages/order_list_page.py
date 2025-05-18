import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
from locators.order_list_page_locators import OrderListPageLocators
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import allure
from selenium.common.exceptions import TimeoutException
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class OrderListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке первому заказу в списке на странице "Лента заказов"')
    def click_first_order_in_order_list(self):
        self.click_element(OrderListPageLocators.FIRST_ORDER_IN_ORDER_LIST)

    @allure.step('Получение данных счетчика заказов "Выполнено за все время"')
    def get_all_orders_counter(self):
        return self.get_element_text(OrderListPageLocators.ALL_ORDERS_COUNTER)

    @allure.step('Получение данных счетчика заказов "Выполнено за сегодня"')
    def get_today_orders_counter(self):
        return self.get_element_text(OrderListPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Ожидание когда первый заказ в списке на странице "Лента заказов" станет кликабельным')
    def wait_for_clickable_first_order_in_order_list(self):
        self.wait_for_element_to_be_clickable(OrderListPageLocators.FIRST_ORDER_IN_ORDER_LIST)

    @allure.step('Ожидание появления элемента / текста "Состав" на странице')
    def wait_for_presence_text_ingredients_order_details_popup(self):
        try:
            self.wait_for_presence_of_element_located(OrderListPageLocators.INGREDIENTS_TEXT_IN_POPUP)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание появления заказа по номеру order_id на странице "Лента заказов"')
    def wait_for_presence_new_order_by_id_in_order_list(self, order_id, timeout=50):
        locator = self.make_order_locator_by_id(order_id)
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание появления заказа по номеру order_id в разделе "В Работе" на странице "Лента заказов"')
    def wait_for_presence_new_order_by_id_in_section_orders_in_progress(self, order_id, timeout=50):
        locator = self.make_order_locator_by_id_in_section_orders_in_progress(order_id)
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False