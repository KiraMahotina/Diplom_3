import allure
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.reset_password_page import ResetPasswordPage
from urls import Urls
from data.data import DATA


class TestRecoveryPassword:


    # В данном тест-классе проверяется:
    # - переход на страницу восстановления пароля по кнопке «Восстановить пароль»
    # - ввод почты и клик по кнопке «Восстановить»
    # - клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его


    @allure.title('Проверка успешного перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('При клике по кнопке "Восстановить пароль" на странице авторизации происходит переход на страницу восстановления пароля')
    def test_recovery_password_button(self, driver):   # Проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        main_page.click_enter_button()
        login_page.click_recovery_password_button()
        with (allure.step("Assert: recovery_password_page.get_current_url() == Urls.RECOVERY_PASSWORD_PAGE_URL")):
            assert recovery_password_page.get_current_url() == Urls.RECOVERY_PASSWORD_PAGE_URL, "Ошибка: Переход на страницу восстановления пароля по кнопке «Восстановить пароль» не происходит"


    @allure.title('Проверка успешного перехода на страницу сброса пароля по кнопке "Восстановить"')
    @allure.description('При вводе почты и клике по кнопке "Восстановить" на странице восстановления пароля происходит переход на страницу сброса пароля')
    def test_recovery_button(self, driver):   # Проверка: переход на страницу сброса пароля при вводе почты и клику по кнопке «Восстановить»
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        main_page.click_enter_button()
        login_page.click_recovery_password_button()
        recovery_password_page.input_email(DATA)
        recovery_password_page.click_recovery_button()
        reset_password_page.wait_for_visibility_save_button()
        with (allure.step("Assert: reset_password_page.get_current_url() == Urls.RESET_PASSWORD_PAGE_URL")):
            assert reset_password_page.get_current_url() == Urls.RESET_PASSWORD_PAGE_URL, "Ошибка: Переход на страницу сброса пароля при вводе почты и клику по кнопке «Восстановить» не происходит"


    @allure.title('Проверка активации и подсветки поля "Пароль" при нажатии кнопки "Показать/скрыть пароль"')
    @allure.description('При нажатии кнопки "Показать/скрыть пароль" на странице сброса пароля поле "Пароль" становится активным и подсвечивается')
    def test_show_hide_password_button(self, driver):   # Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        main_page.click_enter_button()
        login_page.click_recovery_password_button()
        recovery_password_page.input_email(DATA)
        recovery_password_page.click_recovery_button()
        reset_password_page.wait_for_visibility_save_button()
        reset_password_page.click_show_hide_password_button()
        div_class = reset_password_page.get_attribute_div_class()
        label_class = reset_password_page.get_attribute_label_class()
        with (allure.step("Assert: ResetPasswordPageLocators.TEXT_INPUT_PASSWORD_ACTIVE in div_class and ResetPasswordPageLocators.TEXT_INPUT_PASSWORD_FOCUSED in label_class")):
            assert (ResetPasswordPageLocators.TEXT_INPUT_PASSWORD_ACTIVE in div_class
                    and ResetPasswordPageLocators.TEXT_INPUT_PASSWORD_FOCUSED in label_class), "Ошибка: Клик по кнопке показать/скрыть пароль не делает поле активным — не подсвечивает его"