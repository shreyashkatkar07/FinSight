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
    COMPLETED = "COMPLETED", "Completed"
    FAILED = "FAILED", "Failed"

class FileType(models.TextChoices):
    IMAGE = "IMAGE", "Image"
    TEXT = "TEXT", "Text"
    PDF = "PDF", "PDF"
    CSV = "CSV", "CSV"
    XLSX = "XLSX", "XLSX"

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
        max_length=20,
        choices=FileType.choices,
    )

    status = models.CharField(
        max_length=20,
        choices=ArtifactStatus.choices,
        default=ArtifactStatus.UPLOADED,
    )

    storage_path = models.TextField()

    error_message = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "artifacts"

    def __str__(self):
        return f"{self.file_name}"