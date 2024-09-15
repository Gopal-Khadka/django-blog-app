from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogsListView.as_view(), name="index"),
    # path("blogs/", views.blogs, name="blogs"),
]
