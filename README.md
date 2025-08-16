# Habits-Tracker

🚀 Приложение для формирования полезных привычек по методике Джеймса Клира с полной Docker-поддержкой и Telegram-интеграцией.

📌 🔧 Технологии

    Backend: Django + DRF

    База данных: PostgreSQL

    Кеширование/очереди: Redis + Celery

    Веб-сервер: Nginx

    Контейнеризация: Docker + Docker Compose

    CI/CD: GitHub Actions (тесты, линтинг, деплой)

    Документация: Swagger/ReDoc

    Тестирование: 83% coverage, 100% PEP8 (flake8)

🚀 Быстрый старт (Docker)
1. Клонирование репозитория

git clone git@github.com:NataliaBazhina/Habits-tracker.git

cd Habits-tracker

2. Настройка окружения

Создайте .env файл на основе .env.example:

POSTGRES_DB=habits
POSTGRES_USER=NataliaBazhina
POSTGRES_PASSWORD=your_strong_password

SECRET_KEY=your_django_secret_key

CELERY_BROKER_URL=redis://redis:6379/0

TELEGRAM_BOT_TOKEN=your_bot_token

3. Запуск системы

docker compose up -d --build

4. Полезные команды:

Проверить логи:

docker compose logs -f web

Создать суперпользователя:

docker compose exec web python manage.py csu

Остановить:

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


⚙️ CI/CD (GitHub Actions)

    Линтинг: Flake8

    Тесты: Django Tests (SQLite)

    Сборка: Docker-образы

    Деплой: Автоматический на сервер через SSH

📄 Документация

    Swagger: http://localhost:8000/swagger/

    ReDoc: http://localhost:8000/redoc/




