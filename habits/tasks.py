from django.utils import timezone
from habits.models import Habit
from habits.services import send_telegram_message
from celery import shared_task
from datetime import datetime

from django.utils import timezone
from habits.models import Habit
from habits.services import send_telegram_message
from celery import shared_task


@shared_task
def send_habbit_reminder():
    now = timezone.localtime(timezone.now()).time()

    habits = Habit.objects.filter(time__hour=now.hour, time__minute=now.minute)
    print(f"Найдено привычек: {habits.count()}")

    for habit in habits:
        message = f"🔔 Напоминание: {habit.action} в {habit.time.strftime('%H:%M')} на {habit.place}"
        send_telegram_message(habit.user.tg_chat_id, message)