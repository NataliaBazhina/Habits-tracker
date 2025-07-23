from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Проверка, что пользователь является владельцем объекта."""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
