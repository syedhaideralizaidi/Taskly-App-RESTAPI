from rest_framework import permissions

class IsAllowedToEditTaskListElseNone(permissions.BasePermission):
    """
        Custom permission for TaskListViewSet to only allow the creater editing permission.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        pass

class IsAllowedToEditTaskElseNone(permissions.BasePermission):
    """
        Custom permission for TaskViewSet to only allow the members of house access to its tasks.
    """
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.profile.house is not None
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task_list.house

class IsAllowedToEditAttachmentElseNone(permissions.BasePermission):
    """
        Custom permission for AttachmentViewSet to only allow the members of house access to its tasks.
    """
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.profile.house is not None
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task.task_list.house
