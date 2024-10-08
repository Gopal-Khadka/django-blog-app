from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


from blogs.models import BlogPost
from blogs.serializers import BlogPostSerializer

from api import client
from api.mixins import AuthorPermissionMixin, AuthenticationMixin


class BlogsListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogEditAPIView(
    AuthenticationMixin, AuthorPermissionMixin, generics.UpdateAPIView
):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
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


class BlogCreateAPIView(
    AuthenticationMixin, AuthorPermissionMixin, generics.CreateAPIView
):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

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


class BlogDeleteAPIView(
    AuthenticationMixin, AuthorPermissionMixin, generics.DestroyAPIView
):
    serializer_class = BlogPostSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user.author)

    def get_object(self):
        slug = self.kwargs.get("slug")
        try:
            return BlogPost.objects.get(slug=slug)
        except BlogPost.DoesNotExist:
            raise NotFound("Blog post not found")


# Algolia Search API CLIENT
class AlgoliaSearchListAPIView(AuthenticationMixin, generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        user = None
        # only return searches by current user
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get("q")
        if query is None:
            return Response(BlogPost.objects.none(), status=400)
        published = str(request.GET.get("published")) != "0"
        tags = request.GET.get("tags") or None

        results = client.perform_search(query, tags=tags, published=published)
        # results = client.perform_search(query, tags=tags, published=published,user=user)
        return Response(results, status=200)
