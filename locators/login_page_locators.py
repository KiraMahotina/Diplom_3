from selenium.webdriver.common.by import By

class LoginPageLocators:

    EMAIL_INPUT = [By.XPATH, ".//input[@type='text' and @name='name']"]                                                                     # Поле ввода email на странице авторизации
    PASSWORD_INPUT = [By.XPATH, ".//input[@type='password' and @name='Пароль']"]                                                            # Поле ввода пароля на странице авторизации
    ENTER_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти')]"]                          # Кнопка "Войти" на странице авторизации
    REGISTER_BUTTON = [By.XPATH, ".//a[contains(@class, 'Auth_link__') and @href='/register']"]                                             # Кнопка "Зарегистрироваться" на странице авторизации
    RECOVERY_PASSWORD_BUTTON = [By.XPATH,".//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"]                                    # Кнопка "Восстановить пароль" на странице авторизации