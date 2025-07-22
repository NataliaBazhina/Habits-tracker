from rest_framework.exceptions import ValidationError


def validate_reward_and_related_habit(habit):
    if habit.reward and habit.related_habit:
        raise ValidationError(
            "Нельзя указывать и награду, и связанную приятную привычку."
        )


def validate_nice_habit(habit):
    if habit.nice_habit:
        if habit.reward:
            raise ValidationError("Приятная привычка не может иметь награду.")
        if habit.related_habit:
            raise ValidationError("Приятная привычка не может иметь связанную привычку.")


def validate_related_habit_is_nice(habit):
    """
    Проверяет, что связанная привычка является приятной (nice_habit=True).
    """
    if habit.related_habit and not habit.related_habit.nice_habit:
        raise ValidationError("Связанная привычка должна быть приятной")


def validate_execution_time(execution_time):
    if execution_time > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")


def validate_periodicity(periodicity):
    if periodicity < 1:
        raise ValidationError(
            "Привычка должна выполняться хотя бы 1 раз в день. "
            "Укажите значение от 1 до 7."
        )

    if periodicity > 7:
        raise ValidationError(
            "Привычка не может выполняться реже чем 1 раз в 7 дней. "
            "Максимальная периодичность - 7 дней."
        )
