from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:

    EXIT_BUTTON_PERSONAL_ACCOUNT = [By.CLASS_NAME, "Account_button__14Yp3"]                                 # Кнопка "Выход" на странице личного кабинета
    ORDERS_HISTORY_BUTTON = [By.XPATH, ".//a[text()='История заказов']"]                                    # Кнопка "История заказов" на странице личного кабинета
    ORDERS_HISTORY_LIST = [By.XPATH,".//div[contains(@class, 'OrderHistory_orderHistory__qy1VB')]"]         # Раздел "История заказов" на странице личного кабинета
    ORDER_DETAILS_POPUP_CLOSE_BUTTON = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]      # Кнопка закрытия pop-up с деталями заказа - крестик
    TEXT_ACCOUNT = "account"                                                                                # Текст "account" для ожиданий в методах с URL
    TEXT_PROFILE = "profile"                                                                                # Текст "profile" для ожиданий в методах с URL