from django.db import models
from django.contrib.auth.models import User


class SuccessStory(models.Model):
    title = models.CharField(max_length=125, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    src_url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "SuccessStories"

    def __str__(self) -> str:
        return self.title + " - " + self.author.username
