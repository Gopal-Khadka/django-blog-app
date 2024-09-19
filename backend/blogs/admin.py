from django.contrib import admin
from .models import BlogPost, Likes, Comment, BlogAuthor, Contact, Tag
from filebrowser.sites import site


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "public",
        "published",
        "author_email",
        "created_at",
    )
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)

    def author_email(self, obj):
        return obj.author.user.email

    author_email.short_description = "Author's Email"


@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")
    search_fields = ("name", "author__email", "bio")


admin.site.register(Likes)
admin.site.register(Comment)
admin.site.register(Contact)
