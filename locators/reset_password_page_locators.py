from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:

    SAVE_BUTTON = [By.XPATH, ".//button[text()='Сохранить']"]                                       # Кнопка "Сохранить" на странице сброса пароля
    SHOW_HIDE_PASSWORD_BUTTON = [By.XPATH, ".//div[contains(@class, 'input__icon-action')]"]        # Кнопка "Показать / скрыть пароль" на странице сброса пароля
    PASSWORD_DIV = [By.XPATH, ".//div[contains(@class, 'input_type_text')]"]                        # Локатор на проверку фокуса поля "Пароль" на странице сброса пароля при нажатии кнопки "Показать / скрыть пароль"
    PASSWORD_LABEL = [By.XPATH, ".//label[text()='Пароль']"]                                        # Локатор на проверку подсветки поля "Пароль" на странице сброса пароля при нажатии кнопки "Показать / скрыть пароль"
    TEXT_INPUT_PASSWORD_FOCUSED = "input__placeholder-focused"                                      # Текст "input__placeholder-focused" для поиска в классе
    TEXT_INPUT_PASSWORD_ACTIVE = "input_status_active"                                              # Текст "input_status_active" для поиска в классе