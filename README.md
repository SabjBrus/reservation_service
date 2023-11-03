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

    ```bash
    uvicorn app.main:app --reload
    ```
