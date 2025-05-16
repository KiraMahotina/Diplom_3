import allure
from base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators


class RecoveryPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод "email" в поле "Email" на странице восстановления пароля')
    def input_email(self, data):
        self.input_text(RecoveryPasswordPageLocators.EMAIL_INPUT, data["email"])

    @allure.step('Клик по кнопке "Восстановить" на странице восстановления пароля')
    def click_recovery_button(self):
        self.click_element(RecoveryPasswordPageLocators.RECOVERY_BUTTON)