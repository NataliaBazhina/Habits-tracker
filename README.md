# Habits-Tracker

**Бэкенд-часть SPA веб-приложения** для формирования полезных привычек по методике Джеймса Клира ("Атомные привычки")

## 📌 Возможности

✔️ **Аутентификация** (JWT)  
✔️ **CRUD-операции** с привычками  
✔️ Привязка приятных привычек и вознаграждений  
✔️ Публичные/приватные привычки  
✔️ **Telegram-напоминания** (Celery + Beat)  
✔️ **Документация** (Swagger/ReDoc)  
✔️ Покрытие тестами > 80%  
✔️ 100% соответствие PEP8 (flake8)  

---

## 🚀 Установка и запуск

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


