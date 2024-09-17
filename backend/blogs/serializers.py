import uuid
from rest_framework import serializers
from rest_framework.reverse import reverse
from django.utils.text import slugify

from .models import BlogPost
from .validators import UniqueTitleValidator, ValidateImageFileExtension


# TODO: Use this serializer as inline-serializer for AuthorSerializer
class BlogPostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(source="author.user.username", read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    endpoint = serializers.SerializerMethodField(read_only=True)
    published = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")

    class Meta:
        model = BlogPost
        fields = [
            "unique_id",
            "title",
            "slug",
            "author",
            "content",
            "published",
            "endpoint",
            "edit_url",
            "created_at",
        ]

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse(viewname="blog-edit", request=request, kwargs={"slug": obj.slug})

    def get_endpoint(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse(
            viewname="blog-detail", request=request, kwargs={"slug": obj.slug}
        )

    def update(self, instance, validated_data):
        # Ensure slug is updated if title changes
        instance.title = validated_data.get("title", instance.title)
        instance.slug = slugify(instance.title) + "-" + str(instance.unique_id)[:6]
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance

    # def validate_image(self, value):
    #     if not value:
    #         # if no image, return None without any validation
    #         return None

    #     validator = ValidateImageFileExtension()
    #     validator(value)
    #     return value

    # def validate_title(self, value):
    #     queryset = (
    #         BlogPost.objects.exclude(id=self.instance.id)
    #         if self.instance
    #         else BlogPost.objects.all()
    #     )
    #     validator = UniqueTitleValidator(queryset)
    #     validator(value)
    #     return value
