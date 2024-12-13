

Это тестовое задание для реализации CRUD-приложения с использованием FastAPI. В приложении реализованы функции для работы с книгами и авторами


# Установка
**Клонируйте репозиторий**:
- git clone https://github.com/Equialy/library_app_em.git
- cd library_app_em


### Для работы на локальном компьютере установить виртуальное окружение
- python -m venv venv
- venv\Scripts\activate
- Установить зависимости python install -r requirements.txt 

**Настроить базу данных**:
- alembic upgrade head

**Запуск сервера**
- Запустить main.py

**Открыть в браузере**:
- Октрыть в браузере по адресу http://localhost:8000/docs

### Использование Docker-compose
Для использование Docker-compose выполните следующие шаги находясь в корне проекта:

- docker compose build
- docker compose up
- Запустится база и прогонятся миграции автоматически.



- Октрыть в браузере по адресу http://localhost:8003/docs

## Примечания:
- Так как задание тестовое .env файл был добавлен в репозиторий для быстрого поднятия приложения
- Тестовая база для тестов не создавалась и тесты проходят только на проверку эндпоинтов get запросов.