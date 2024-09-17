from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.exceptions import NotFound

from blogs.models import BlogPost
from blogs.serializers import BlogPostSerializer


class BlogsListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogEditAPIView(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs.get("slug")
        try:
            return BlogPost.objects.get(slug=slug)
        except BlogPost.DoesNotExist:
            raise NotFound("Blog post not found")

    def perform_update(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "No content from author"

        serializer.save(content=content)


class BlogCreateAPIView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "No content from author"

        serializer.save(author=self.request.user.author, content=content)


class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "slug"

    def get_object(self):
        slug = self.kwargs.get("slug")
        try:
            return BlogPost.objects.get(slug=slug)
        except BlogPost.DoesNotExist:
            raise NotFound("Blog post not found")


class BlogDeleteAPIView(generics.DestroyAPIView):
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user.author)

    def get_object(self):
        slug = self.kwargs.get("slug")
        try:
            return BlogPost.objects.get(slug=slug)
        except BlogPost.DoesNotExist:
            raise NotFound("Blog post not found")
