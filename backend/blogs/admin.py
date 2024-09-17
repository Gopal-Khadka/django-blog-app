from django.contrib import admin
from .models import BlogPost, Likes, Comment, BlogAuthor, Contact
from filebrowser.sites import site


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
        "author_email",
    )
    search_fields = ("title", "content")

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
