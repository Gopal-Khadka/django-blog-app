from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from api.mixins import (
    AuthenticationMixin,
    ForumPermissionMixin,
    ForumCreatePermissionMixin,
)

from forum.models import Category, Post, Thread
from forum.serializers import CategorySerializer, ThreadSerializer


class ForumListAPIView(ForumPermissionMixin, AuthenticationMixin, generics.ListAPIView):
    """
    All the forum categories are listed here.

    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ForumCreateAPIView(
    ForumCreatePermissionMixin, AuthenticationMixin, generics.CreateAPIView
):
    """
    You can create category for the forum here.

    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ThreadListAPIView(
    ForumPermissionMixin, AuthenticationMixin, generics.ListAPIView
):
    """
    All the threads in this category are listed here.

    """

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class ThreadCreateAPIView(
    ForumCreatePermissionMixin, AuthenticationMixin, generics.CreateAPIView
):
    """
    You can create thread for the given forum category here.

    """

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    
    def perform_create(self, serializer):
        category_id = self.kwargs['category_id']  
        category = Category.objects.get(id=category_id) 
        serializer.save(user=self.request.user, category=category)  # 
