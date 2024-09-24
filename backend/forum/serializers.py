from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.validators import UniqueValidator, ValidationError
from django.utils.text import slugify

from .models import Category, Post, Thread
from .validators import UniqueAttrValidator


class PostInlineSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Post
        fields = ["content", "username"]


class ThreadSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    posts = PostInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ["title", "username", "posts"]

    def to_representation(self, instance):
        # limit no of posts in each thread.
        representation = super().to_representation(instance)
        representation["posts"] = representation["posts"][:3]
        return representation

    def validate_title(self, value):
        validator = UniqueAttrValidator(
            queryset=Thread.objects.all(), model="thread", attr="title"
        )
        validator(value)
        return value


class CategorySerializer(serializers.ModelSerializer):
    threads = ThreadSerializer(many=True, read_only=True)
    create_url = serializers.SerializerMethodField(read_only=True)
    list_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ["name", "create_url", "list_url", "threads"]

    def get_create_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse(
            viewname="thread-create", request=request, kwargs={"category_id": obj.pk}
        )

    def get_list_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse(
            viewname="thread-list", request=request, kwargs={"category_id": obj.pk}
        )

    def validate_name(self, value):
        queryset = (
            Category.objects.exclude(id=self.instance.id)
            if self.instance
            else Category.objects.all()
        )
        validator = UniqueValidator(
            queryset, message="Given category name already exists."
        )
        validator(value, self.fields["name"])
        return value
