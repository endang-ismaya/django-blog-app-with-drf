from django.db import models

from apps.author.models import Author
from apps.base.models import BaseTimeStampModel


class Blog(BaseTimeStampModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
