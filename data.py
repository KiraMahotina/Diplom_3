import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


DATA = {"email": f"kroki.2011@mail.ru",                    # данные для проверок тестов со страницами восстановления пароля уже существующего аккаунта, где не требуется авторизация
        "password": "123Ki456"}