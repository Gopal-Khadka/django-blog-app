from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.validators import UniqueValidator,ValidationError
from django.utils.text import slugify

from .models import Category, Post, Thread


class PostInlineSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Post
        fields = ["content", "username"]


class ThreadInlineSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    posts = PostInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ["title", "username", "posts"]

    def to_representation(self, instance):
        # limit no of posts in each thread.
        representation = super().to_representation(instance)
        representation["posts"] = representation["posts"][:3]
        return representation


class CategorySerializer(serializers.ModelSerializer):
    threads = ThreadInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["name", "threads"]
        
    def validate_name(self, value):
        queryset = (
            Category.objects.exclude(id=self.instance.id)
            if self.instance
            else Category.objects.all()
        )
        validator = UniqueValidator(queryset,message="Given category name already exists.")
        validator(value,self.fields["name"])
        return value
