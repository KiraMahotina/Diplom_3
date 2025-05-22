from selenium.webdriver.common.by import By

class OrderListPageLocators:

    FIRST_ORDER_IN_ORDER_LIST = [By.XPATH, "//a[contains(@class, 'OrderHistory_link')]"]                                                                             # Первый заказ в списке на странице "Лента заказов"
    INGREDIENTS_TEXT_IN_POPUP = [By.XPATH, ".//*[text()='Cостав']"]                                                                                                   # Класс со словом "Состав" в сплывающем окне с деталями заказа
    ALL_ORDERS_COUNTER = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]"]                               # Счетчик заказов "Выполнено за все время" на странице "Лента заказов"
    TODAY_ORDERS_COUNTER = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]"]
    NONE_ORDERS_IN_ORDERS_IN_PROGRESS = [By.XPATH, f".//ul[contains(@class, 'OrderFeed_orderList__')]/li[text()='Все текущие заказы готовы!')]"]# Счетчик заказов "Выполнено за сегодня" на странице "Лента заказов"