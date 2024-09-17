from django.urls import path

from . import views

urlpatterns = [
    # path("blogs/", views.BlogsListCreateAPIView.as_view(), name="blog"),
    path("blogs/", views.BlogsListAPIView.as_view(), name="blog-list"),
    path("blogs/create/", views.BlogCreateAPIView.as_view(), name="blog-create"),
    path("blogs/<slug>/", views.BlogDetailAPIView.as_view(), name="blog-detail"),
    path("blogs/<slug>/update/", views.BlogEditAPIView.as_view(), name="blog-edit"),
    path(
        "blogs/<slug>/delete/", views.BlogDeleteAPIView.as_view(), name="blog-delete"
    ),
]
