from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import blog_views,forum_views

urlpatterns = [
    # path("blogs/", views.BlogsListCreateAPIView.as_view(), name="blog"),
    path("blogs/", blog_views.BlogsListAPIView.as_view(), name="blog-list"),
    path("blogs/create/", blog_views.BlogCreateAPIView.as_view(), name="blog-create"),
    path("blogs/<slug>/", blog_views.BlogDetailAPIView.as_view(), name="blog-detail"),
    path("blogs/<slug>/update/", blog_views.BlogEditAPIView.as_view(), name="blog-edit"),
    path("blogs/<slug>/delete/", blog_views.BlogDeleteAPIView.as_view(), name="blog-delete"),
    # search api view
    path("blogs/search", blog_views.AlgoliaSearchListAPIView.as_view(), name="blog-search"),
    # auth api views
    path("auth/", obtain_auth_token, name="auth"),
    # jwt token views
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    
    # forum views
    path("forum/", forum_views.ForumListAPIView.as_view(), name="forum-list"),
    path("forum/create/", forum_views.ForumCreateAPIView.as_view(), name="forum-create"),
    path("forum/<category_id>/thread/", forum_views.ThreadListAPIView.as_view(), name="thread-list"),
    path("forum/<category_id>/thread/create/", forum_views.ThreadCreateAPIView.as_view(), name="thread-create"),
    # path("forum/<slug>/update/", blog_views.BlogEditAPIView.as_view(), name="blog-edit"),
    # path("forum/<slug>/delete/", blog_views.BlogDeleteAPIView.as_view(), name="blog-delete"),
]
