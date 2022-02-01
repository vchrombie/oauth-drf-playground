from django.contrib.auth.models import Group

from rest_framework import generics, permissions

from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope

from .models import CustomUser
from .serializer import UserSerializer, GroupSerializer


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        TokenHasReadWriteScope,
    ]


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        TokenHasReadWriteScope,
    ]


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        TokenHasScope,
    ]
    required_scopes = [
        'groups',
    ]
