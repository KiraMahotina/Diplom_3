import allure
from selenium.common.exceptions import TimeoutException
from base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "История заказов" на странице личного кабинета')
    def click_orders_history_button(self):
        self.click_element(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход" на странице личного кабинета')
    def click_exit_personal_account_button(self):
        self.click_element(PersonalAccountPageLocators.EXIT_BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Клик по крестику - кнопке закрытия pop-up с деталями заказа в разделе "История заказов"')
    def click_close_order_details_button(self):
        self.click_element(PersonalAccountPageLocators.ORDER_DETAILS_POPUP_CLOSE_BUTTON)

    @allure.step('Ожидание появления элемента / раздела "История заказов" на странице личного кабинета')
    def wait_for_presence_element_orders_history_list(self):
        try:
            self.wait_for_presence_of_element_located(PersonalAccountPageLocators.ORDERS_HISTORY_LIST)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание появления заказа по номеру order_id в разделе раздела "История заказов" на странице личного кабинета')
    def wait_for_presence_new_order_by_id_in_orders_history(self, order_id):
        locator = self.make_order_locator_by_id(order_id)
        try:
            self.wait_for_presence_of_element_located(locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание когда кнопка "История заказов" на странице личного кабинета станет кликабельной')
    def wait_for_clickable_orders_history_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Ожидание когда кнопка "Выход" на странице личного кабинета станет кликабельной')
    def wait_for_clickable_exit_personal_account_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.EXIT_BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Ожидание отсутствия "account" в текущем URL')
    def wait_for_text_account_not_in_url(self):
        self.wait_for_text_not_in_url(PersonalAccountPageLocators.TEXT_ACCOUNT)

    @allure.step('Ожидание присутствия "profile" в текущем URL')
    def wait_for_text_profile_in_url(self):
        self.wait_for_url_contains(PersonalAccountPageLocators.TEXT_PROFILE)