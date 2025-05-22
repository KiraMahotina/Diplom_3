import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from base_page import BasePage
from locators.order_list_page_locators import OrderListPageLocators

class OrderListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по первому заказу в списке')
    def click_first_order_in_order_list(self):
        self.click_element(OrderListPageLocators.FIRST_ORDER_IN_ORDER_LIST)

    @allure.step('Получение счетчика всех заказов')
    def get_all_orders_counter(self):
        return self.get_element_text(OrderListPageLocators.ALL_ORDERS_COUNTER)

    @allure.step('Получение счетчика заказов за сегодня')
    def get_today_orders_counter(self):
        return self.get_element_text(OrderListPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Ожидание кликабельности первого заказа')
    def wait_for_clickable_first_order_in_order_list(self):
        self.wait_for_element_to_be_clickable(OrderListPageLocators.FIRST_ORDER_IN_ORDER_LIST)

    @allure.step('Ожидание текста "Состав" в попапе')
    def wait_for_presence_text_ingredients_order_details_popup(self):
        return self.wait_for_visibility_of_element(OrderListPageLocators.INGREDIENTS_TEXT_IN_POPUP)

    @allure.step('Ожидание нового заказа по ID в ленте')
    def wait_for_presence_new_order_by_id_in_order_list(self, order_id, timeout=50):
        locator = self.make_order_locator_by_id(order_id)
        return self.wait_for_presence_of_element(locator, timeout)

    @allure.step('Ожидание нового заказа в разделе "В работе"')
    def wait_for_presence_new_order_by_id_in_section_orders_in_progress(self, order_id, timeout=50):
        locator = self.make_order_locator_in_progress_section(order_id)
        return self.wait_for_presence_of_element(locator, timeout)

    @allure.step('Создание локатора по ID заказа')
    def make_order_locator_by_id(self, order_id):
        return (By.XPATH, f"//p[contains(text(), '{order_id}')]")

    @allure.step('Создание локатора для раздела "В работе"')
    def make_order_locator_in_progress_section(self, order_id):
        return (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(., '{order_id}')]")
