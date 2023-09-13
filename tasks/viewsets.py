from rest_framework import viewsets, mixins
from tasks.models import TaskList, Task, Attachment
from tasks.serializers import TaskListSerializer , TaskSerializer , AttachmentSerializer
from tasks.permissions import IsAllowedToEditTaskListElseNone , IsAllowedToEditTaskElseNone , \
    IsAllowedToEditAttachmentElseNone


class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      # mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAllowedToEditTaskListElseNone, ]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAllowedToEditTaskElseNone, ]

class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAllowedToEditAttachmentElseNone, ]