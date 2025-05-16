import allure
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from urls import Urls


class TestPersonalAccount:


    # В данном тест-классе проверяется:
    # - переход по клику на «Личный кабинет»
    # - переход в раздел «История заказов»
    # - выход из аккаунта


    @allure.title('Проверка успешного перехода на страницу личного кабинета по клику на кнопку «Личный кабинет»')
    @allure.description('После авторизации при клике на кнопку «Личный кабинет» происходит переход на страницу личного кабинета')
    def test_personal_account_button(self, driver, token_create_new_user_and_delete):   # Проверка: переход по клику на «Личный кабинет»
        user_data = token_create_new_user_and_delete
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        header_page.click_personal_account_button()
        login_page.login_page_authorization(user_data)
        header_page.wait_for_text_login_not_in_url()
        header_page.click_personal_account_button()
        personal_account_page.wait_for_text_profile_in_url()
        with (allure.step("Assert: personal_account_page.get_current_url() == Urls.PERSONAL_ACCOUNT_PAGE_URL")):
            assert personal_account_page.get_current_url() == Urls.PERSONAL_ACCOUNT_PAGE_URL, "Ошибка: Переход по клику на «Личный кабинет» не происходит"


    @allure.title('Проверка успешного открытия раздела "История заказов" по клику на кнопку «История заказов»')
    @allure.description('После авторизации при клике на кнопку «История заказов» в личном кабинете открывается блок "История заказов"')
    def test_orders_history_button(self, driver, token_create_new_user_and_delete):   # Проверка: переход в раздел «История заказов»
        user_data = token_create_new_user_and_delete
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        header_page.click_personal_account_button()
        login_page.login_page_authorization(user_data)
        header_page.wait_for_text_login_not_in_url()
        header_page.click_personal_account_button()
        personal_account_page.wait_for_clickable_orders_history_button()
        personal_account_page.click_orders_history_button()
        with (allure.step("Assert: personal_account_page.wait_for_presence_element_orders_history_list()")):
            assert personal_account_page.wait_for_presence_element_orders_history_list(), "Ошибка: Переход в раздел «История заказов» не происходит"


    @allure.title('Проверка успешного выхода из личного кабинета при нажатии на кнопку «Выход»')
    @allure.description('После авторизации при клике на кнопку «Выход» на странице личного кабинета происходит выход из личного кабинета и переход на страницу авторизации')
    def test_exit_personal_account_button(self, driver, token_create_new_user_and_delete):   # Проверка: выход из аккаунта
        user_data = token_create_new_user_and_delete
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        header_page.click_personal_account_button()
        login_page.login_page_authorization(user_data)
        header_page.wait_for_text_login_not_in_url()
        header_page.click_personal_account_button()
        personal_account_page.wait_for_clickable_exit_personal_account_button()
        personal_account_page.click_exit_personal_account_button()
        personal_account_page.wait_for_text_account_not_in_url()
        with (allure.step("Assert: login_page.get_current_url() == Urls.LOGIN_PAGE_URL")):
            assert login_page.get_current_url() == Urls.LOGIN_PAGE_URL, "Ошибка: Выход из аккаунта по кнопке 'Выход' не происходит"