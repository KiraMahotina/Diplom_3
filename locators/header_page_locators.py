from selenium.webdriver.common.by import By

class HeaderPageLocators:

    CONSTRUCTOR_BUTTON = [By.XPATH,".//p[contains(., 'Конструктор')]"]                 # Кнопка "Конструктор" бургеров в хедере
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH,".//p[contains(text(), 'Личный Кабинет')]"]    # Кнопка "Личный кабинет" в хедере
    LOGO_BUTTON = [By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"]                  # Кнопка-логотип "Stellar burgers" в хедере
    ORDER_LIST_BUTTON = [By.XPATH, ".//p[text()='Лента Заказов']"]                     # Кнопка "Лента заказов" в хедере
    TEXT_LOGIN = "login"                                                               # Текст "login" для ожиданий в методах с URL