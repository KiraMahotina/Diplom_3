import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import allure
from selenium.common.exceptions import TimeoutException
from seletools.actions import drag_and_drop
from base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Войти в аккаунт" на главной странице')
    def click_enter_button(self):
        self.click_element(MainPageLocators.ENTER_BUTTON)

    @allure.step('Клик по кнопке "Флюоресцентная булка R2-D3" в конструкторе на главной странице')
    def click_fluorescent_bun_button(self):
        self.click_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step('Клик по крестику - кнопке закрытия pop-up "Детали ингредиента"')
    def click_ingredient_details_exit_button(self):
        self.click_element(MainPageLocators.INGREDIENT_DETAILS_EXIT_BUTTON)

    @allure.step('Клик по кнопке "Оформить заказ" на главной странице')
    def click_make_order_button(self):
        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Клик по крестику - кнопке закрытия pop-up с только что оформленным заказом')
    def click_popup_close_button(self):
        self.click_element(MainPageLocators.POPUP_CLOSE_BUTTON)

    @allure.step('Ожидание появления элемента кнопка "Войти в аккаунт" на главной странице')
    def wait_for_presence_enter_button(self):
        self.wait_for_presence_of_element_located(MainPageLocators.ENTER_BUTTON)

    @allure.step('Ожидание появления номера оформленного заказа в pop-up')
    def wait_for_presence_order_id_in_popup(self):
        self.wait_for_presence_of_changing_elements_located(MainPageLocators.ORDER_ID_IN_POPUP, MainPageLocators.DEFAULT_ORDER_ID_IN_POPUP)


    @allure.step('Скролл до кнопки: "Войти в аккаунт" на главной странице')
    def scroll_to_enter_button(self):
        self.scroll_to_element(MainPageLocators.ENTER_BUTTON)

    @allure.step('Ожидание появления элемента / раздела "Конструктор" на главной странице')
    def wait_for_presence_element_constructor(self):
        try:
            self.wait_for_presence_of_element_located(MainPageLocators.CONSTRUCTOR_BLOCK)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание появления элемента / раздела "Лента заказов" на главной странице')
    def wait_for_presence_element_orders_list(self):
        try:
            self.wait_for_presence_of_element_located(MainPageLocators.ORDERS_LIST_BLOCK)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание появления элемента / текста "Детали ингредиента" на странице')
    def wait_for_text_ingredient_details_popup(self):
        try:
            self.wait_for_presence_of_element_located(MainPageLocators.INGREDIENT_DETAILS_TITLE)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание появления заголовка конструктора "Соберите бургер" на главной странице')
    def wait_for_presence_constructor_title(self):
        try:
            self.wait_for_presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
            return True
        except TimeoutException:
            return False

    @allure.step("Перетаcкиваем булку в корзину для создания бургера и оформления заказа")
    def add_bun_in_burger_basket(self):
        source = self.wait_for_visibility_of_element_located(MainPageLocators.FLUORESCENT_BUN)
        target = self.wait_for_visibility_of_element_located(MainPageLocators.BURGER_BASKET)
        drag_and_drop(self.driver, source, target)

    @allure.step("Получение количество ингредиентов из каунтера ингредиента 'Флюоресцентная булка R2-D3'")
    def get_ingredients_counter(self):
        return self.get_element_text(MainPageLocators.FLUORESCENT_BUN_COUNTER)

    @allure.step("Получение номера оформленного заказа из pop-up")
    def get_order_id_in_popup(self):
        return self.get_element_text(MainPageLocators.ORDER_ID_IN_POPUP)

    @allure.step('Создание заказа в разделе "Конструктор" на главной странице и извлечение order_id')
    def making_order_and_return_order_id(self):
        self.add_bun_in_burger_basket()
        self.click_make_order_button()
        self.wait_for_presence_order_id_in_popup()
        order_id = self.get_order_id_in_popup()
        # Если ID в формате "#0227435", уберите решётку:
        return order_id.lstrip()