class Urls:
    BASE_PAGE_URL = "https://stellarburgers.nomoreparties.site"                             # Главная страница (базовый URL)
    LOGIN_PAGE_URL = f"{BASE_PAGE_URL}/login"                                               # Страница авторизации
    PERSONAL_ACCOUNT_PAGE_URL = f"{BASE_PAGE_URL}/account/profile"                          # Страница Личного кабинета
    ORDER_LIST_PAGE_URL = f"{BASE_PAGE_URL}/feed"                                           # Страница с Лентой заказов
    ORDER_HISTORY_PAGE_URL = f"{BASE_PAGE_URL}/account/order-history"                       # Страница с Историей заказов
    REGISTRATION_PAGE_URL = f"{BASE_PAGE_URL}/register"                                     # Страница Регистрации пользователя
    RECOVERY_PASSWORD_PAGE_URL = f"{BASE_PAGE_URL}/forgot-password"                         # Страница Восстановления пароля
    RESET_PASSWORD_PAGE_URL = f"{BASE_PAGE_URL}/reset-password"                             # Страница Сброса пароля

class UrlsAPI:
    BASE_PAGE_URL = "https://stellarburgers.nomoreparties.site"                             # Главная страница (базовый URL)
    API_POST_CREATING_USER = f"{BASE_PAGE_URL}/api/auth/register"                           # Создание пользователя (POST)
    API_POST_LOGIN_USER = f"{BASE_PAGE_URL}/api/auth/login"                                 # Логин пользователя в системе (POST)
    API_PATCH_USER_DATA = f"{BASE_PAGE_URL}/api/auth/user"                                  # Изменение данных пользователя (PATCH)
    API_DELETE_USER = f"{BASE_PAGE_URL}/api/auth/user"                                      # Удаление пользователя (DELETE)
    API_POST_MAKING_ORDER = f"{BASE_PAGE_URL}/api/orders"                                   # Создание заказа (POST)
    API_GET_USER_ORDERS = f"{BASE_PAGE_URL}/api/orders"                                     # Получение заказов конкретного пользователя (GET)