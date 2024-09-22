import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Thread(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    category = models.ForeignKey(
        Category, related_name="threads", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="threads", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_id = str(uuid.uuid4())[:6]
            self.slug = slugify(self.title) + "-" + unique_id
        return super().save(*args, **kwargs)


class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return f"Post by {self.user.username} in {self.thread.title}"
