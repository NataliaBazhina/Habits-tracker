from datetime import time

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from habits.models import Habit
from habits.validators import (validate_execution_time, validate_nice_habit,
                               validate_periodicity,
                               validate_related_habit_is_nice,
                               validate_reward_and_related_habit)
from users.models import User


class HabitValidatorsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="testuser@example.com", first_name="Test", last_name="User"
        )

        self.nice_habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time=time(8, 0),
            action="пить кофе",
            nice_habit=True,
            execution_time=120,
            periodicity=1,
        )

        self.regular_habit = Habit.objects.create(
            user=self.user,
            place="Спортзал",
            time=time(19, 0),
            action="делать зарядку",
            nice_habit=False,
            execution_time=90,
            periodicity=2,
        )

    def test_validate_reward_and_related_habit(self):
        """Тест валидации одновременного указания награды
        и связанной привычки.
        """
        habit = Habit(
            user=self.user,
            place="Парк",
            time=time(7, 0),
            action="бегать",
            reward="шоколадка",
            related_habit=self.nice_habit,
            execution_time=60,
            periodicity=1,
        )

        with self.assertRaises(ValidationError) as context:
            validate_reward_and_related_habit(habit)

        self.assertEqual(
            str(context.exception.detail[0]),
            "Нельзя указывать и награду, и связанную приятную привычку.",
        )

    def test_validate_nice_habit_with_reward(self):
        """Тест валидации приятной привычки с наградой"""
        habit = Habit(
            user=self.user,
            place="Кровать",
            time=time(23, 0),
            action="читать книгу",
            nice_habit=True,
            reward="чай",
            execution_time=300,
            periodicity=1,
        )

        with self.assertRaises(ValidationError) as context:
            validate_nice_habit(habit)

        self.assertEqual(
            str(context.exception.detail[0]),
            "Приятная привычка не может иметь награду.",
        )

    def test_validate_nice_habit_with_related_habit(self):
        """Тест валидации приятной привычки со связанной привычкой"""
        habit = Habit(
            user=self.user,
            place="Кухня",
            time=time(9, 0),
            action="завтракать",
            nice_habit=True,
            related_habit=self.regular_habit,
            execution_time=600,
            periodicity=1,
        )

        with self.assertRaises(ValidationError) as context:
            validate_nice_habit(habit)

        self.assertEqual(
            str(context.exception.detail[0]),
            "Приятная привычка не может иметь связанную привычку.",
        )

    def test_validate_related_habit_is_nice(self):
        """Тест валидации что связанная привычка является приятной"""
        habit = Habit(
            user=self.user,
            place="Офис",
            time=time(13, 0),
            action="гулять",
            related_habit=self.regular_habit,
            execution_time=120,
            periodicity=1,
        )

        with self.assertRaises(ValidationError) as context:
            validate_related_habit_is_nice(habit)

        self.assertEqual(
            str(context.exception.detail[0]), "Связанная привычка должна быть приятной"
        )

    def test_validate_execution_time_too_long(self):
        """Тест валидации времени выполнения привычки"""
        with self.assertRaises(ValidationError) as context:
            validate_execution_time(121)

        self.assertEqual(
            str(context.exception.detail[0]),
            "Время выполнения не должно превышать 120 секунд.",
        )

    def test_validate_periodicity_too_small(self):
        """Тест валидации слишком маленькой периодичности"""
        with self.assertRaises(ValidationError) as context:
            validate_periodicity(0)

        self.assertEqual(
            str(context.exception.detail[0]),
            "Привычка должна выполняться хотя бы 1 раз в день."
            " Укажите значение от 1 до 7.",
        )

    def test_validate_periodicity_too_large(self):
        """Тест валидации слишком большой периодичности"""
        with self.assertRaises(ValidationError) as context:
            validate_periodicity(8)

        self.assertEqual(
            str(context.exception.detail[0]),
            "Привычка не может выполняться реже чем 1 раз в 7 дней. "
            "Максимальная периодичность - 7 дней.",
        )

    def test_valid_habit_passes_all_validations(self):
        """Тест что корректная привычка проходит все валидации"""
        habit = Habit(
            user=self.user,
            place="Балкон",
            time=time(7, 30),
            action="дышать свежим воздухом",
            reward="кофе",
            execution_time=60,
            periodicity=1,
        )

        validate_reward_and_related_habit(habit)
        validate_nice_habit(habit)
        validate_related_habit_is_nice(habit)
        validate_execution_time(habit.execution_time)
        validate_periodicity(habit.periodicity)
