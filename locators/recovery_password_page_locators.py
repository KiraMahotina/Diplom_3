from selenium.webdriver.common.by import By

class RecoveryPasswordPageLocators:

    EMAIL_INPUT = [By.XPATH, ".//input[@type='text' and @name='name']"]              # Поле ввода email на странице восстановления пароля
    RECOVERY_BUTTON = [By.XPATH, "//button[contains(text(), 'Восстановить')]"]       # Кнопка "Восстановить" на странице восстановления пароля