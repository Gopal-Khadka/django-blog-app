from django.db import models
from django.contrib.auth.models import User
from .validators import ValidateImageFileExtension


class BlogAuthor(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="blog_authors", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(
        BlogAuthor, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to="blogs",
        null=True,
        blank=True,
        validators=[ValidateImageFileExtension()],
    )
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " - " + self.author.name


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content + " - " + self.author.username


class Likes(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="likes")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.author.username + " - " + self.post.title


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    message = models.TextField(null=False, default="Random query")
    created_at = models.DateTimeField(auto_now_add=True)
