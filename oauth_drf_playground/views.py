from django.contrib.auth.models import User, Group

from oauth_drf_playground.serializer import UserSerializer, GroupSerializer

from rest_framework import generics, permissions

from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        TokenHasReadWriteScope,
    ]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
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
