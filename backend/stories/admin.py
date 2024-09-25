from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import SuccessStory


@register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    search_fields = ["title","author__username","content"]
    search_help_text = "You can search title, author and content"
