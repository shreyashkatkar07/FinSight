from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models

from shared.models.mixins import (
    UUIDMixin,
    TimestampMixin,
)

from .managers import UserManager


class User(
    UUIDMixin,
    TimestampMixin,
    AbstractBaseUser,
    PermissionsMixin,
):
    email = models.EmailField(
        unique=True,
        db_index=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email