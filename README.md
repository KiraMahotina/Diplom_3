# Автоматизированное тестирование веб-приложения Stellar Burgers

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.8+-green)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-7.2+-orange)](https://docs.pytest.org/)

Проект содержит автоматизированные тесты для веб-приложения "Stellar Burgers" с использованием Selenium и Pytest.

## 📋 Основные тестируемые функции
- **Авторизация и регистрация**
- **Восстановление пароля**
- **Личный кабинет пользователя**
- **Конструктор бургеров**
- **Лента заказов**
- **История заказов**
- **Оформление заказов**

## 🛠 Технологии
- **Selenium WebDriver** - автоматизация браузера
- **Pytest** - фреймворк для тестирования
- **Allure** - генерация отчетов
- **Page Object Model** - паттерн проектирования
- **Faker** - генерация тестовых данных

## ⚙️ Установка
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/yourusername/stellar-burgers-tests.git
Установить зависимости:

bash
pip install -r requirements.txt
🚀 Запуск тестов
Общий запуск всех тестов:

powershell
$env:PYTHONPATH="."; pytest tests/ -v
Запуск конкретного тестового класса:

powershell
$env:PYTHONPATH="."; pytest tests/test_order_list_section.py -v
Запуск с генерацией Allure-отчета:

powershell
$env:PYTHONPATH="."; pytest tests/ -v --alluredir=allure-results
allure serve allure-results
🗂 Структура проекта
project/
├── tests/               # Тестовые сценарии
├── pages/               # Page Object-классы
├── locators/            # Локаторы элементов
├── data.py              # Тестовые данные
├── urls.py              # URL-адреса приложения
├── conftest.py          # Фикстуры Pytest
└── helpers.py           # Вспомогательные функции
🌍 Переменные окружения
BASE_PAGE_URL - базовый URL тестируемого приложения (по умолчанию: https://stellarburgers.nomoreparties.site)

📊 Отчетность
Для визуализации результатов используйте Allure:

bash
pytest --alluredir=allure-results
allure serve allure-results