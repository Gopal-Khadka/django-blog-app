from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


from forum.models import Category, Post, Thread
from forum.serializers import CategorySerializer


class ForumListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
