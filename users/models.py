from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=24,
        unique=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
