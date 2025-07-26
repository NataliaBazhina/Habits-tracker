from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (validate_execution_time, validate_nice_habit,
                               validate_periodicity,
                               validate_related_habit_is_nice,
                               validate_reward_and_related_habit)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        habit = Habit(**data)

        validate_reward_and_related_habit(habit)
        validate_nice_habit(habit)
        validate_related_habit_is_nice(habit)

        if "execution_time" in data:
            validate_execution_time(data["execution_time"])

        if "periodicity" in data:
            validate_periodicity(data["periodicity"])

        return data
