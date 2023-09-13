from rest_framework import routers
from tasks.viewsets import TaskListViewSet, TaskViewSet, AttachmentViewSet

app_name = 'tasks'

router = routers.DefaultRouter()
router.register('task-lists', TaskListViewSet)
router.register('tasks', TaskViewSet)
router.register('attachments', AttachmentViewSet)
