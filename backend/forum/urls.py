from django.urls import path
from . import views

app_name = "forum"
urlpatterns = [
    path("", views.CategoryTemplateView.as_view(), name="show-categories"),
    path("categories/<int:id>/", views.show_threads, name="show-threads"),
    path("threads/<int:thread_id>/posts", views.show_posts, name="show-posts"),
    path("posts/<int:post_id>/edit/", views.edit_post, name="edit-post"),
    path("posts/<int:post_id>/delete/", views.delete_post, name="delete-post"),
]
