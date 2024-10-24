from typing import Iterable
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.shortcuts import reverse
from . import utils


class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="blog_authors", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.name:
            self.name = self.user.get_full_name()
        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(
        BlogAuthor, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    public = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    content = HTMLField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="blog_posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(self.unique_id)[:6]
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return self.author.user.get_full_name()

    def get_tags_list(self):
        return self.tags.all().values_list("name", flat=True)
        
    def get_absolute_url(self):
        return reverse('api:blog-detail', kwargs={'slug': self.slug})
    
    def get_full_url(self, request):
        return request.build_absolute_uri(self.get_absolute_url())

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


class Like(models.Model):
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
