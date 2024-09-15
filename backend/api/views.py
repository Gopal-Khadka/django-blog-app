from rest_framework import generics


from blogs.models import BlogPost
from blogs.serializers import BlogPostSerializer


class BlogsListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
