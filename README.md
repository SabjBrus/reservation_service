# Reservation servise

Cервис бронирования жилья
В разработке

## Технологии

- Python 3.9
- FastAPI
- Uvicorn

## Запуск

1. Склонировать репозиторий:

   ```bash
   git clone https://github.com/SabjBrus/reservation_servise.git
   ```

2. Установка и активация виртуального окружения

    ```bash
    python3 -m venv venv
    ```

    ```bash
    source venv/Scripts/activate
    ```

3. Установка fastapi в виртуальном окружении

    ```bash
    pip install -r requirements.txt
    ```

4. Запуск проекта  
Проект доступен по адресу <http://localhost/>  
Панель администратора <http://localhost/admin/>

    ```bash
    uvicorn app.main:app --reload
    ```

5. Для кэширования необходим локальный запуск Redis
6. Для использования отложенных задач, необходимо запустить в отдельном
терминале Celery (--pool=solo только для Windows)

   ```bash
   celery -A app.tasks.celery:celery worker --loglevel=INFO --pool=solo
   ```

7. Для мониторинга Celery по адресу <http://localhost:5555/> запустить
в отдельном терминале flower:

   ```bash
   celery -A app.tasks.celery:celery flower
   ```
