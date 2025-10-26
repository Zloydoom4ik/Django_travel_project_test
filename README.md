# Travel Project

Django проект для путешествий.

## Установка

1. Клонируй репозиторий
2. Создай виртуальное окружение: `python -m venv venv`
3. Активируй виртуальное окружение:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Установи зависимости: `pip install -r requirements.txt`
5. Создай файл `.env` в корне проекта с переменными окружения
6. Запусти миграции: `python manage.py migrate`
7. Создай супер-пользователя: `python manage.py createsuperuser`
8. Запусти сервер: `python manage.py runserver`

## Структура проекта

- `places/` - приложение для мест
- `homepage/` - приложение для главной страницы
- `templates/` - HTML шаблоны
- `static_dev/` - статические файлы
- `media/` - загруженные медиафайлы