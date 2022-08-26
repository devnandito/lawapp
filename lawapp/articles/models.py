"""Articles models."""

# Django
from django.db import models

# Utilities
from lawapp.utils.models import CustomModel

# Models
from lawapp.laws.models import Law
from lawapp.chapters.models import Chapter

class Article(CustomModel):
    """Article model."""

    fklaw = models.ForeignKey(
        Law,
        on_delete = models.CASCADE
    )
    fkchapter = models.ForeignKey(
        Chapter,
        on_delete = models.CASCADE
    )
    num = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.description