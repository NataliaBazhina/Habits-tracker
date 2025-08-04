# Habits-Tracker

Бэкенд SPA приложения для формирования полезных привычек по методике Джеймса Клира с полной Docker-поддержкой
📌 Возможности

✔️ Готовая Docker-сборка (PostgreSQL + Redis + Celery)
✔️ Автоматические миграции при запуске
✔️ JWT-аутентификация через DRF
✔️ Telegram-ботам (Celery Beat + Redis)
✔️ Swagger/ReDoc документация
✔️ 100% PEP8 (flake8) + 83% тестов 

---

🚀 Запуск через Docker (рекомендуется)
1. Настройка окружения 

bash

git clone git@github.com:NataliaBazhina/Habits-tracker.git
cd Habits-tracker

2. Создайте .env файл:
ini

PostgreSQL

POSTGRES_DB=habits
POSTGRES_USER=NataliaBazhina
POSTGRES_PASSWORD=your_strong_password

Django

SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

Celery

CELERY_BROKER_URL=redis://redis:6379/0

Telegram

TELEGRAM_BOT_TOKEN=your_bot_token

3. Запуск системы

bash

docker compose up -d --build

4. Полезные команды:

    Проверить логи:
    bash

docker compose logs -f web

Создать суперпользователя:
bash

docker compose exec web python manage.py csu

Остановить:
bash

    docker compose down

🌐 Доступные эндпоинты

После запуска откройте в браузере:

    API Documentation: http://localhost:8000/swagger/

    Admin Panel: http://localhost:8000/admin/

    Public Habits: http://localhost:8000/habits/public/


## 🚀 Ручная установка и запуск

1. Клонирование репозитория

git clone git@github.com:NataliaBazhina/Habits-tracker.git

cd Habits-tracker

2. Настройка виртуального окружения

python -m venv .venv

Для Linux/Mac:
source .venv/bin/activate

Для Windows:
.venv\Scripts\activate

3. Установите зависимости

pip install -r requirements.txt

4. Настройка окружения

Создайте файл .env и добавьте:

SECRET_KEY=ваш_ключ

DB_NAME=habits

DB_USER=user

DB_PASSWORD=password

DB_HOST=localhost

DB_PORT=5432


CELERY_BROKER_URL=redis://localhost:6379/0

CELERY_RESULT_BACKEND=redis://localhost:6379/0

TELEGRAM_BOT_TOKEN=ваш_токен

5. Настройка базы данных

Примените миграции:

python manage.py migrate

Создайте суперпользователя:

python manage.py csu

6. Запуск сервера

python manage.py runserver

7. Запуск Celery

Запуск Celery worker:

celery -A config worker -l info

Запуск Beat:

celery -A config beat -l info

Запуск Celery worker и Beat одновременно: 

celery -A config worker --beat --loglevel=info

🤖 Интеграция с Telegram

Создайте бота через @BotFather

Сохраните токен в .env как TELEGRAM_TOKEN

Установите tg_chat_id пользователя вручную через /admin

📊 Тестирование

    Покрытие тестами: 83% (coverage_report.txt)

    Соответствие PEP8: 100% (flake8_report.txt)

📚 Примеры запросов

Регистрация пользователя

POST /users/register/

{
  "email": "test@example.com",

  "password": "123test"
}

Получение токена:

POST /users/login/

{
  "email": "test@example.com",

  "password": "123test"
}

Создание привычки:

{
  "place": "Спальная комната",

  "time": "8:00:00",

  "action": "Делать зарядку",

  "execution_time": 120,

  "periodicity": 1,

  "public_habit": true,

  "nice_habit": false,

  "reward": "Заряд бодрости на весь день"
}


Публичные привычки:
GET /habits/public/




