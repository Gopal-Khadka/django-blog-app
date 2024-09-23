from django.urls import path
from . import views

app_name = "forum"
urlpatterns = [
    path("", views.CategoryTemplateView.as_view(), name="show-categories"),
    path("categories/<int:id>/", views.show_threads, name="show-threads"),
    path("categories/<int:cat_id>/threads/<int:thread_id>/posts", views.show_posts, name="show-posts"),
]
