from django.conf import settings
from django.db import models

from shared.models.mixins import (
    UUIDMixin,
    TimestampMixin,
    ActiveFlagMixin,
)


class ArtifactStatus(models.TextChoices):
    UPLOADED = "UPLOADED", "Uploaded"
    PROCESSING = "PROCESSING", "Processing"
    PROCESSED = "PROCESSED", "Processed"
    FAILED = "FAILED", "Failed"


class Artifact(
    UUIDMixin,
    TimestampMixin,
    ActiveFlagMixin,
):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="artifacts",
    )

    file_name = models.CharField(
        max_length=255,
    )

    file_type = models.CharField(
        max_length=50,
    )

    status = models.CharField(
        max_length=20,
        choices=ArtifactStatus.choices,
        default=ArtifactStatus.UPLOADED,
    )

    storage_path = models.TextField()

    class Meta:
        db_table = "artifacts"

    def __str__(self):
        return f"{self.file_name}"