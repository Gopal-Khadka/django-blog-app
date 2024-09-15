from django.urls import path

from . import views

urlpatterns = [
    path("blogs/list", views.BlogsListAPIView.as_view(), name="blog-list"),
    path("blogs/update/<int:pk>", views.BlogEditAPIView.as_view(), name="blog-edit"),
    path("blogs/create/", views.BlogCreateAPIView.as_view(), name="blog-create"),
]
