from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """Custom Permissions for UserViewSet to only allow users to edit their own user, Otherwise, GET and POST only"""

    def has_permission(self, request, view):
        """GET and POST only"""
        return True

    def has_object_permission(self, request, view, obj):
        """GET request is only allowed because it is SAFE METHOD"""
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            """If user is not anonymous and specific object is related to user then return TRUE"""
            return request.user == obj

        return False


class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """Custom Permissions for ProfileViewSet to only allow users to edit their own profile, Otherwise, GET and POST
    only"""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            """obj is profile in this case"""
            return request.user.profile == obj

        return False
