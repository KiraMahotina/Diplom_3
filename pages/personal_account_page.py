import allure
from selenium.common.exceptions import TimeoutException
from base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
from selenium.webdriver.common.by import By

class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "История заказов"')
    def click_orders_history_button(self):
        self.click_element(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_personal_account_button(self):
        self.click_element(PersonalAccountPageLocators.EXIT_BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Закрыть попап деталей заказа')
    def click_close_order_details_button(self):
        self.click_element(PersonalAccountPageLocators.ORDER_DETAILS_POPUP_CLOSE_BUTTON)

    @allure.step('Ожидание раздела истории заказов')
    def wait_for_presence_element_orders_history_list(self):
        return self.wait_for_presence_of_element(PersonalAccountPageLocators.ORDERS_HISTORY_LIST)

    @allure.step('Ожидание нового заказа в истории')
    def wait_for_presence_new_order_by_id_in_orders_history(self, order_id):
        locator = self.make_order_locator_in_history(order_id)
        return self.wait_for_presence_of_element(locator)

    @allure.step('Ожидание кликабельности кнопки истории')
    def wait_for_clickable_orders_history_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Ожидание кликабельности кнопки выхода')
    def wait_for_clickable_exit_personal_account_button(self):
        self.wait_for_element_to_be_clickable(PersonalAccountPageLocators.EXIT_BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Ожидание отсутствия "account" в URL')
    def wait_for_text_account_not_in_url(self):
        self.wait_for_text_not_in_url(PersonalAccountPageLocators.TEXT_ACCOUNT)

    @allure.step('Ожидание "profile" в URL')
    def wait_for_text_profile_in_url(self):
        self.wait_for_url_contains(PersonalAccountPageLocators.TEXT_PROFILE)

    @allure.step('Создание локатора для истории заказов')
    def make_order_locator_in_history(self, order_id):
        return (By.XPATH, f"//div[contains(@class, 'OrderHistory_orderHistory__qy1VB')]//p[contains(text(), '{order_id}')]")
