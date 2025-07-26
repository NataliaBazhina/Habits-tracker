from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginations import HabitPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """
    ViewSet для работы с привычками пользователя.
    Все операции доступны только для аутентифицированных пользователей.
    Пользователь видит и может изменять только свои привычки.
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        """Возвращает привычки текущего пользователя"""
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        """Создает новую привычку, автоматически
        привязывая ее к текущему пользователю.
        """

        serializer.save(user=self.request.user)


class PublicHabitListAPIView(ListAPIView):
    """Список публичных привычек (read-only)"""

    queryset = Habit.objects.filter(public_habit=True)
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitPagination
