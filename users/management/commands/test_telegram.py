from django.core.management.base import BaseCommand

from habits.services import send_telegram_message
from users.models import User


class Command(BaseCommand):
    help = "Тест отправки сообщения в Telegram"

    def handle(self, *args, **options):
        user = User.objects.filter(tg_chat_id__isnull=False).first()

        if not user:
            self.stdout.write(self.style.ERROR("Нет пользователей с tg_chat_id!"))
            return

        message = "✅ Это тестовое сообщение от HabitTrackerBot!"
        send_telegram_message(message, user.tg_chat_id)

        self.stdout.write(
            self.style.SUCCESS(
                f"Сообщение отправлено пользователю {user.email}"
            )
        )