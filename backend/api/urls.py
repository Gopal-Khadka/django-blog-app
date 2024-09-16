from django.urls import path

from . import views

urlpatterns = [
    # path("blogs/", views.BlogsListCreateAPIView.as_view(), name="blog"),
    path("blogs/", views.BlogsListAPIView.as_view(), name="blog-list"),
    path("blogs/create/", views.BlogCreateAPIView.as_view(), name="blog-create"),
    path("blogs/<int:pk>/", views.BlogDetailAPIView.as_view(), name="blog-detail"),
    path("blogs/update/<int:pk>/", views.BlogEditAPIView.as_view(), name="blog-edit"),
    path(
        "blogs/delete/<int:pk>/", views.BlogDeleteAPIView.as_view(), name="blog-delete"
    ),
]
