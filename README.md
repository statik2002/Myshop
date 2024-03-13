# Интернет магазин MyShop

## Описание

Для создания применяется Django (backend) и Vuejs (frontend). Взаимодействие происходит с примененением Django REST Framework.

## Требования
- Django 5.0
- NodeJS 20

## Установка

1. Скачиваем или делаем Fork
2. Создаем виртуальное окружение `python3 -m venv env` и активируем командой `source env/bin/activate`
3. Устанавливаем python зависимости `pip install -r requirements.txt`
4. Устанавливаем завивимости NodeJS командой `npm install`
5. Создаем файл `.env` в котором прописываем:

    * SECRET_KEY=[you secret key]
    * DEBUG=True
    * ALLOWED_HOSTS='127.0.0.1,localhost'

    * EMAIL_HOST=[you smpt server]
    * EMAIL_HOST_USER=[you email]
    * EMAIL_HOST_PASSWORD=[you password]
    * EMAIL_USE_SSL=True
    * EMAIL_PORT=465
    * DEFAULT_FROM_EMAIL=[you from email]
6. Выполняем миграции командой `python manage.py migrate`
7. Создаем супер пользователя командой `python manage.py createsuperuser`

## Использование
- Запускаем Django командой `python manage.py runserver`
- Запускаем frontend командой `npm run dev`

По адресу `http://127.0.0.1:8000/admin` доступна админ панель Django, по адресу `http://localhost:5173/` доступен непосредственно frontend.