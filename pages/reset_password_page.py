import allure
from base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание появления элемента кнопка "Сохранить" на странице сброса пароля')
    def wait_for_visibility_save_button(self):
        self.wait_for_visibility_of_element_located(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Клик по кнопке "Показать / скрыть пароль" на странице сброса пароля')
    def click_show_hide_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step('Получение текста названия div_class из DOM')
    def get_attribute_div_class(self):
        div = self.get_attribute(ResetPasswordPageLocators.PASSWORD_DIV)
        return div

    @allure.step('Получение текста названия div_label из DOM')
    def get_attribute_label_class(self):
        label = self.get_attribute(ResetPasswordPageLocators.PASSWORD_LABEL)
        return label