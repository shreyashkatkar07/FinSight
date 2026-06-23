from django.conf import settings
from django.db import models

from apps.artifacts.models import Artifact
from shared.models.mixins import (
    UUIDMixin,
    TimestampMixin,
    ActiveFlagMixin,
)


class EventType(models.TextChoices):
    CREDIT = "CREDIT", "Credit"
    DEBIT = "DEBIT", "Debit"


class FinancialEvent(
    UUIDMixin,
    TimestampMixin,
    ActiveFlagMixin,
):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="financial_events",
    )

    artifact = models.ForeignKey(
        Artifact,
        on_delete=models.CASCADE,
        related_name="financial_events",
        null=True,
        blank=True,
    )

    merchant = models.CharField(
        max_length=255,
        db_index=True,
        default="UNKNOWN",
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    currency = models.CharField(
        max_length=10,
        default="INR",
    )

    event_type = models.CharField(
        max_length=20,
        choices=EventType.choices,
    )

    description = models.TextField()

    transaction_date = models.DateField(
        db_index=True,
    )

    raw_data = models.JSONField(
        default=dict,
        blank=True,
    )

    class Meta:
        db_table = "financial_events"
        ordering = [
            "-transaction_date",
            "-created_at",
        ]

    def __str__(self) -> str:
        return (
            f"{self.merchant} | "
            f"{self.event_type} | "
            f"{self.amount} {self.currency}"
        )