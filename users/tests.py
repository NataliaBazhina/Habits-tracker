from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("users:register")
        self.login_url = reverse("users:login")

    def test_user_registration(self):
        """Тестирование регистрации через API"""
        data = {
            "email": "test@example.com",
            "password": "testpass123",
            "first_name": "Test",
            "last_name": "User",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

    def test_user_login_success(self):
        """Тестирование успешного входа"""
        # Создаем пользователя напрямую через модель
        user = User.objects.create(
            email="login@example.com", first_name="Login", last_name="User"
        )
        user.set_password("testpass123")  # Хэшируем пароль
        user.save()

        login_data = {"email": "login@example.com", "password": "testpass123"}
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_user_login_failure(self):
        """Тестирование неудачного входа"""
        user = User.objects.create(
            email="fail@example.com", first_name="Fail", last_name="User"
        )
        user.set_password("testpass123")
        user.save()

        login_data = {"email": "fail@example.com", "password": "wrongpassword"}
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
