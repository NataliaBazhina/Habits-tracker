from django.test import TestCase
from unittest.mock import patch, MagicMock
from users.models import User
from habits.services import send_telegram_message


class TelegramServiceTest(TestCase):
    """Тесты для отправки Telegram-сообщений"""

    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        cls.user = User.objects.create(
            email="test@example.com",
            tg_chat_id="123456"
        )

    @patch('habits.services.requests.post')
    def test_send_telegram_message_correct_params(self, mock_post):
        """Проверяем корректность параметров вызова"""
        # Настраиваем мок
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        # Вызываем функцию
        test_message = "Тестовое сообщение"
        send_telegram_message(self.user.tg_chat_id, test_message)

        # Проверяем вызов requests.post
        mock_post.assert_called_once()

        # Получаем аргументы вызова
        called_url = mock_post.call_args[0][0]
        called_params = mock_post.call_args[1]['params']

        # Проверяем URL (без токена)
        self.assertIn("api.telegram.org", called_url)
        self.assertIn("/sendMessage", called_url)

        # Проверяем параметры
        self.assertEqual(called_params['chat_id'], self.user.tg_chat_id)
        self.assertEqual(called_params['text'], test_message)

    @patch('habits.services.requests.post')
    def test_send_telegram_message_with_none_chat_id(self, mock_post):
        """Проверяем поведение при None в chat_id"""
        send_telegram_message(None, "Сообщение")

        mock_post.assert_called_once()