from django.db import models

from apps.base.models import BaseTimeStampModel


class Author(BaseTimeStampModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=["first_name"])]

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.id}"
