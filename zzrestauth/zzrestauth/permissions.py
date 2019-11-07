from rest_framework import permissions


class ReadOnlyPermissions(permissions.BasePermission):
    """Read-only permissions"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
