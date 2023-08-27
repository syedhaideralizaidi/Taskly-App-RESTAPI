from django.contrib.auth.models import User
from rest_framework import viewsets, mixins

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly,]
