from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from api.mixins import AuthenticationMixin, ForumPermissionMixin

from forum.models import Category, Post, Thread
from forum.serializers import CategorySerializer


class ForumListAPIView(ForumPermissionMixin, AuthenticationMixin, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ForumCreateAPIView(ForumPermissionMixin, AuthenticationMixin,generics.CreateAPIView):
    """ 
    You can create category for the forum here.

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
