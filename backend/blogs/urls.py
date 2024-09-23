from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.logInUser, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logOutUser, name="logout"),
    path("about/", views.about, name="about"),
    # blog urls
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/create/", views.create_blogs, name="blogs-create"),
    path("blogs/search/", views.search_blogs, name="blogs-search"),
    path("blogs/<slug:slug>/", views.show_blogs, name="blogs-show"),
]
