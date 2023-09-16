from rest_framework import viewsets, mixins, filters
from tasks.models import TaskList, Task, Attachment
from tasks.serializers import TaskListSerializer , TaskSerializer , AttachmentSerializer
from tasks.permissions import IsAllowedToEditTaskListElseNone , IsAllowedToEditTaskElseNone , \
    IsAllowedToEditAttachmentElseNone
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', ]
    filterset_fields = ['status', ]

class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAllowedToEditAttachmentElseNone, ]