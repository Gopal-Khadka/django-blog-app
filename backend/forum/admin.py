from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Category, Post, Thread


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]


@register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    search_fields = ["title", "category__name"]
    search_help_text = "Search title and category."
    list_display = ["title", "category", "user", "created_at"]
    list_filter = ["category", "created_at"]


@register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["thread__title", "content", "user__username"]
    search_help_text = "Search thread title, content and author."
    list_display = ["thread", "content", "user"]
    list_filter = ["thread", "created_at"]
