import allure
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage



class TestOrderListSection:


    # В данном тест-классе проверяется:
    # - если кликнуть на заказ, откроется всплывающее окно с деталями
    # - заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
    # - при создании нового заказа счётчик «Выполнено» за всё время увеличивается
    # - при создании нового заказа счётчик «Выполнено» за сегодня увеличивается
    # - после оформления заказа его номер появляется в разделе «В работе»


    @allure.title('Проверяем появление всплывающего окна с деталями заказа при клике на заказа на странице "Лента заказов"')
    @allure.description('Переход на страницу "Лента заказов", клик на первый заказ в списке, ожидание всплывающего окна с деталями заказа')
    def test_order_details_popup(self, driver):   # Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями
        header_page = HeaderPage(driver)
        order_list_page = OrderListPage(driver)
        header_page.click_order_list_button()
        order_list_page.wait_for_clickable_first_order_in_order_list()
        order_list_page.click_first_order_in_order_list()
        with (allure.step("Assert: order_list_page.wait_for_presence_text_ingredients_order_details_popup()")):
            assert order_list_page.wait_for_presence_text_ingredients_order_details_popup(), "Ошибка: Не открывается всплывающее окно с деталями заказа при клике на заказ"


    @allure.title('Проверяем отображение заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    @allure.description('Создаем новый заказ авторизованным пользователем, извлекаем номер из pop-up при создании заказа, ищем заказ по id в «Истории заказов», ищем заказ id в «Ленте заказов»')
    def test_same_order_in_orders_history_and_order_list(self, driver, token_create_new_user_and_delete):   # Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
        user_data = token_create_new_user_and_delete
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_list_page = OrderListPage(driver)
        header_page.click_personal_account_button()
        login_page.login_page_authorization(user_data)
        header_page.wait_for_text_login_not_in_url()
        header_page.click_constructor_button()
        order_id_in_popup = main_page.making_order_and_return_order_id()
        header_page.click_personal_account_button()
        personal_account_page.wait_for_clickable_orders_history_button()
        personal_account_page.click_orders_history_button()
        personal_account_page.wait_for_presence_new_order_by_id_in_orders_history(order_id_in_popup)
        header_page.click_order_list_button()
        with (allure.step("Assert: order_list_page.wait_for_presence_new_order_by_id_in_order_list(order_id_in_popup)")):
            assert order_list_page.wait_for_presence_new_order_by_id_in_order_list(order_id_in_popup), "Ошибка: Заказы пользователя из раздела «История заказов» не отображаются на странице «Лента заказов»"


    @allure.title('Проверяем увеличение счётчика «Выполнено» за все время на странице "Лента заказов" при оформлении нового заказа')
    @allure.description('Фиксируем значение счетчика до создания заказа, создаем новый заказ авторизованным пользователем, фиксируем увеличение счетчика «Выполнено» за все время')
    def test_all_orders_counter(self, driver, token_create_new_user_and_delete):   # Проверка: при создании нового заказа счётчик «Выполнено» за всё время увеличивается
        user_data = token_create_new_user_and_delete
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        header_page.click_personal_account_button()
        login_page.login_page_authorization(user_data)
        header_page.wait_for_text_login_not_in_url()
        header_page.click_order_list_button()
        main_page.wait_for_presence_element_orders_list()
        all_orders_counter_before = int(order_list_page.get_all_orders_counter())
        header_page.click_constructor_button()
        main_page.making_order_and_return_order_id()
        header_page.click_order_list_button()
        main_page.wait_for_presence_element_orders_list()
        all_orders_counter_after = int(order_list_page.get_all_orders_counter())
        with (allure.step("Assert: all_orders_counter_after - all_orders_counter_before >= 1")):
            assert all_orders_counter_after - all_orders_counter_before >= 1, "Ошибка: Не увеличивается счётчик «Выполнено» за все время на странице 'Лента заказов' при создании нового заказа"    # Выставлен assert >=1, т.к. пару раз при прогоне теста в час пик другие студенты тоже параллельно создают заказы, и бывает попадало, что счетчик успевал прирастать на 2-3 заказа просто за время перехода от созданного заказа на страницу "Лента заказов"


    @allure.title('Проверяем увеличение счётчика «Выполнено» за сегодня на странице "Лента заказов" при оформлении нового заказа')
    @allure.description('Фиксируем значение счетчика до создания заказа, создаем новый заказ авторизованным пользователем, фиксируем увеличение счетчика «Выполнено» за сегодня')
    def test_today_orders_counter(self, driver, token_create_new_user_and_delete):   # Проверка: при создании нового заказа счётчик «Выполнено» за сегодня увеличивается
        user_data = token_create_new_user_and_delete
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        header_page.click_personal_account_button()
        login_page.login_page_authorization(user_data)
        header_page.wait_for_text_login_not_in_url()
        header_page.click_order_list_button()
        main_page.wait_for_presence_element_orders_list()
        today_orders_counter_before = int(order_list_page.get_today_orders_counter())
        header_page.click_constructor_button()
        main_page.making_order_and_return_order_id()
        header_page.click_order_list_button()
        main_page.wait_for_presence_element_orders_list()
        today_orders_counter_after = int(order_list_page.get_today_orders_counter())
        with (allure.step("Assert: today_orders_counter_after - today_orders_counter_before >= 1")):
            assert today_orders_counter_after - today_orders_counter_before >= 1, "Ошибка: Не увеличивается счётчик «Выполнено» за сегодня на странице 'Лента заказов' при создании нового заказа"    # Выставлен assert >=1, т.к. пару раз при прогоне теста в час пик другие студенты тоже параллельно создают заказы, и бывает попадало, что счетчик успевал прирастать на 2-3 заказа просто за время перехода от созданного заказа на страницу "Лента заказов"


    @allure.title('Проверяем появление номера нового заказа в разделе «В работе» на странице "Лента заказов"')
    @allure.description('Создаем новый заказ авторизованным пользователем, извлекаем номер из pop-up при создании заказа, проверяем появление номера заказа в разделе «В работе» на странице "Лента заказов"')
    def test_order_id_in_section_orders_in_progress(self, driver, token_create_new_user_and_delete):   # Проверка: после оформления заказа его номер появляется в разделе «В работе»
        user_data = token_create_new_user_and_delete
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_list_page = OrderListPage(driver)
        header_page.click_personal_account_button()
        login_page.login_page_authorization(user_data)
        header_page.wait_for_text_login_not_in_url()
        header_page.click_constructor_button()
        order_id_in_popup = main_page.making_order_and_return_order_id()
        header_page.click_order_list_button()
        with (allure.step("Assert: order_list_page.wait_for_presence_new_order_by_id_in_section_orders_in_progress(order_id_in_popup)")):
            assert order_list_page.wait_for_presence_new_order_by_id_in_section_orders_in_progress(order_id_in_popup), "Ошибка: Не появляется номер заказа в разделе «В работе» на странице 'Лента заказов' после его оформления"
