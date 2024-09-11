# Автоматизированный тест для saucedemo.com

Этот проект содержит автоматизированный тест для проверки процесса покупки на сайте saucedemo.com с использованием Python и Selenium WebDriver.

## Требования

- Python 3.7+
- pip (менеджер пакетов Python)
- Google Chrome
- ChromeDriver

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/your-username/saucedemo-test.git
   cd saucedemo-test
   ```

2. Создайте и активируйте виртуальное окружение:
   ```
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

4. Скачайте и установите ChromeDriver:
   - Перейдите на [страницу загрузки ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Скачайте версию, соответствующую вашей версии Google Chrome
   - Распакуйте файл и добавьте путь к ChromeDriver в системную переменную PATH

## Запуск теста

Для запуска теста выполните следующую команду:

```
python test_saucedemo.py
```

## Структура проекта

- `test_saucedemo.py`: Основной файл с тестом
- `requirements.txt`: Список зависимостей проекта
- `README.md`: Документация проекта

## Дополнительная информация

Этот тест автоматизирует следующий сценарий:
1. Авторизация на сайте saucedemo.com
2. Выбор товара и добавление его в корзину
3. Оформление покупки
4. Проверка успешного завершения покупки

При возникновении проблем или вопросов, пожалуйста, создайте Issue в этом репозитории.
