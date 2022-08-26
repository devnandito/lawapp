"""Chapters models."""

# Django
from django.db import models

# Utilities
from lawapp.utils.models import CustomModel

class Chapter(CustomModel):
    """Chapter model."""

    description = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.description