from selenium.webdriver.common.by import By

class MainPageLocators:

    ENTER_BUTTON = [By.XPATH, ".//button[text()='Войти в аккаунт']"]                                                                        # Кнопка "Войти в аккаунт" на главной странице
    CONSTRUCTOR_BLOCK = [By.CSS_SELECTOR, ".BurgerIngredients_ingredients__menuContainer__Xu3Mo"]                                           # Раздел "Конструктор" на главной странице
    CONSTRUCTOR_TITLE = [By.XPATH, ".//h1[text() = 'Соберите бургер']"]                                                                     # Заголовок раздела "Конструктор" на главной странице
    ORDERS_LIST_BLOCK = [By.CSS_SELECTOR, ".OrderFeed_list__OLh59"]                                                                         # Раздел "Лента заказов" на главной странице
    MAKE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]                                                                     # Кнопка "Оформить заказ" на главной странице
    ORDER_ID_IN_POPUP = [By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m')]"]                                                   # Номер только что оформленного заказа в popup
    POPUP_CLOSE_BUTTON = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]                                                    # Кнопка закрытия pop-up с только что оформленным заказом - крестик
    DEFAULT_ORDER_ID_IN_POPUP = "9999"                                                                                                      # Базовый номер заказа, отображаемый в pop-up в момент формирования номера оформленного заказа
    FLUORESCENT_BUN = [By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"]                                                               # Кнопка ингредиента 'Флюоресцентная булка R2-D3' в конструкторе на главной странице
    INGREDIENT_DETAILS_TITLE = [By.XPATH, ".//h2[contains(text(), 'Детали ингредиента')]"]                                                  # Заголовок pop-up "Детали ингредиента"
    INGREDIENT_DETAILS_EXIT_BUTTON = [By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]         # Кнопка закрытия pop-up "Детали ингредиента"
    BURGER_BASKET = [By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']"]                                                     # Корзина для добавления ингредиентов и оформления заказа
    FLUORESCENT_BUN_COUNTER = [By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]"]                                           # Каунтер 'Флюоресцентная булка R2-D3' в конструкторе на главной странице