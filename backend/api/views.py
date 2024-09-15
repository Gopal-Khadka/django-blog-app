from rest_framework import generics


from blogs.models import BlogPost
from blogs.serializers import BlogPostSerializer


class BlogsListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # redefine perform_create method to save author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class BlogsListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogEditAPIView(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogCreateAPIView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "No content from author"

        serializer.save(author=self.request.user.author, content=content)
