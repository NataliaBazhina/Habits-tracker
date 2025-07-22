from rest_framework.viewsets import ModelViewSet
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    """
    ViewSet для работы с привычками пользователя.
    Обеспечивает стандартные CRUD-операции (создание, чтение, обновление, удаление).
    Все операции доступны только для аутентифицированных пользователей.
    Пользователь видит и может изменять только свои привычки.
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        """Возвращает привычки текущего пользователя"""
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        """Создает новую привычку, автоматически привязывая ее к текущему пользователю"""

        serializer.save(user=self.request.user)
