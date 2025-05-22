import allure
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestBasicFunctionality:


    # В данном тест-классе проверяется:
    # - переход по клику на «Конструктор»
    # - переход по клику на «Лента заказов»
    # - если кликнуть на ингредиент, появится всплывающее окно с деталями
    # - всплывающее окно закрывается кликом по крестику
    # - при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
    # - залогиненный пользователь может оформить заказ


    @allure.title('Проверка успешного открытия раздела "Конструктор" по клику на кнопку «Конструктор»')
    @allure.description('При клике на кнопку «Конструктор» на главной странице открывается блок "Конструктор"')
    def test_constructor_button(self, driver):   # Проверка: переход по клику на «Конструктор»
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_personal_account_button()
        header_page.click_constructor_button()
        with (allure.step("Assert: main_page.wait_for_presence_element_constructor()")):
            assert main_page.wait_for_presence_element_constructor(), "Ошибка: Переход в раздел «Конструктор» не происходит"


    @allure.title('Проверка успешного открытия раздела "Лента заказов" по клику на кнопку «Лента заказов»')
    @allure.description('При клике на кнопку «Лента заказов» открывается блок "Лента заказов"')
    def test_orders_list_button(self, driver):   # Проверка: переход по клику на «Лента заказов»
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        header_page.click_order_list_button()
        with (allure.step("Assert: main_page.wait_for_presence_element_orders_list()")):
            assert main_page.wait_for_presence_element_orders_list(), "Ошибка: Переход в раздел «Лента заказов» не происходит"


    @allure.title('Проверка появления pop-up "Детали ингредиента" при нажатии на ингредиент в конструкторе')
    @allure.description('При клике на ингредиент в конструкторе на главной странице появляется pop-up "Детали ингредиента"')
    def test_ingredient_details_popup(self, driver):   # Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_button()
        with (allure.step("Assert: main_page.wait_for_text_ingredient_details_popup()")):
            assert main_page.wait_for_text_ingredient_details_popup(), "Ошибка: Окно 'Детали ингредиента' не появляется"


    @allure.title('Проверяем закрытие pop-up "Детали ингредиента" кликом по кнопке закрытия - крестику')
    @allure.description('При клике на крестик - pop-up "Детали ингредиента" закрывается')
    def test_ingredient_details_popup_close_button(self, driver):   # Проверка: всплывающее окно закрывается кликом по крестику
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_button()
        main_page.click_ingredient_details_exit_button()
        with (allure.step("Assert: main_page.wait_for_presence_constructor_title()")):
            assert main_page.wait_for_presence_constructor_title(), "Ошибка: Окно 'Детали ингредиента' не закрывается при нажатии на крестик"


    @allure.title('Проверяем работу каунтера ингредиентов при добавлении ингредиента в корзину с бургерами / заказ')
    @allure.description('При добавлении "Флюоресцентная булка R2-D3" в корзину с бургерами / каунтер данной булки == 2')
    def test_ingredient_counter(self, driver):   # Проверка: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
        main_page = MainPage(driver)
        counter_default = main_page.get_ingredients_counter()
        main_page.add_bun_in_burger_basket()
        counter_after_adding_buns = main_page.get_ingredients_counter()
        with (allure.step("Assert: counter_default == '0' and counter_after_adding_buns == '2'")):
            assert (counter_default == "0"
                    and counter_after_adding_buns == "2"), "Ошибка: Каунтер ингредиента 'Флюоресцентная булка R2-D3' работает некорректно"


    @allure.title('Проверка успешного оформления заказа авторизованным пользователем')
    @allure.description('Авторизация пользователя, оформление заказа, проверка присутствия номера созданного заказа в pop-up после нажатия кнопки "Оформить заказ"')
    def test_exit_personal_account_button(self, driver, token_create_new_user_and_delete):   # Проверка: залогиненный пользователь может оформить заказ
        user_data = token_create_new_user_and_delete
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_enter_button()
        login_page.login_page_authorization(user_data)
        main_page.add_bun_in_burger_basket()
        main_page.click_make_order_button()
        main_page.wait_for_presence_order_id_in_popup()
        order_id_in_popup = main_page.get_order_id_in_popup()
        with (allure.step("Assert: order_id_in_popup is not None and len(order_id_in_popup) == 6 and isinstance(order_id_in_popup, str)")):
            assert (order_id_in_popup is not None
                    and len(order_id_in_popup) >= 4
                    and isinstance(order_id_in_popup, str)), "Ошибка: Проблема с оформлением заказа у залогиненного пользователя"
