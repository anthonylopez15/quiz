from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    message = 'Allow only Admin Users.'

    def has_permission(self, request, view):
        return request.user.is_staff