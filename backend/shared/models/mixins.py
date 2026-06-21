import uuid

from django.db import models


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActiveFlagMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True