# Reservation servise

API сервиса для бронирования, посторенного с использованием FastAPI.  
Веб-сервис предоставляет функциональность для регистрации и аутентификации,  
бронирования номеров в отелях.

## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)

## Запуск в Docker containers

1. Склонировать репозиторий:

   ```bash
   git clone https://github.com/SabjBrus/reservation_servise.git
   ```

2. Из директории reservation_service/ запустить Docker Compose:

   ```bash
   docker-compose up --build
   ```

- Проект доступен по адресу:  
<http://localhost:7777/>

- Swagger документация(эндпоинты и HTTP-запросы):  
<http://localhost:7777/v1/docs>

- Отслеживание отложенных задач через Flower:  
<http://localhost:5555/>

- Мониторинг через Prometheus:  
<http://localhost:9090/>

- Визуализация и анализ через Grafana:  
<http://localhost:3000/>

## Запуск без Docker

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

### Автор

- Жуков Борис
