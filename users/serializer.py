from django.contrib.auth.models import Group

from .models import CustomUser

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'phone_number',
            'email',
            'first_name',
            'last_name',
        )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'name',
        )
