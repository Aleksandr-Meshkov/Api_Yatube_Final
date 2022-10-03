# **REST API для проекта YaTube**
> - **Проект позволяет делать запросы к базе данных социальной сети YaTube [GitHub](https://github.com/Aleksandr-Meshkov/YaTube). Поддерживаются все
функции, которые есть в социальной сети (регистрация, получение списка постов и отдельного
поста, отправка поста и комментария, подписка на авторов), также реализована авторизация
по JWT - токенам при помощи библиотеки Djoser. Проект реализован строго  в соответствии с документацией ТЗ**

___
## **Стек технологий**

![CI](https://img.shields.io/badge/Django%20Rest%20Framework-3.12.4-success)
![CI](https://img.shields.io/badge/Django-2.2.16-green)
![CI](https://img.shields.io/badge/Requests-2.26.0-yellow)
![CI](https://img.shields.io/badge/Python-v3.8-blue)
![CI](https://img.shields.io/badge/-Djoser-yellowgreen)

## **Как запустить проект**

**Клонировать репозиторий и перейти в него в командной строке**

  - ```https://github.com/Aleksandr-Meshkov/Api_Yatube_Final```

  - ```cd api_final_yatube```

**Cоздать и активировать виртуальное окружение:**

  - ```python -m venv env```

  - ```source venv/Scripts/activate```

**Установить зависимости из файла requirements.txt:**

  - ```pip install -r requirements.txt```

**Выполнить миграции:**

  - ```python manage.py migrate```

**Запустить проект:**

  - ```python3 manage.py runserver```
___

## **Автор проекта**

https://github.com/Aleksandr-Meshkov

## **Документация**

http://127.0.0.1:8000/redoc/<br>
https://www.django-rest-framework.org/
