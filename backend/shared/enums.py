from django.db import models

class Category(models.TextChoices):
    FOOD = "FOOD", "Food"
    SHOPPING = "SHOPPING", "Shopping"
    TRAVEL = "TRAVEL", "Travel"
    BILLS = "BILLS", "Bills"
    HEALTH = "HEALTH", "Health"
    ENTERTAINMENT = "ENTERTAINMENT", "Entertainment"
    TRANSFER = "TRANSFER", "Transfer"
    INCOME = "INCOME", "Income"
    OTHER = "OTHER", "Other"