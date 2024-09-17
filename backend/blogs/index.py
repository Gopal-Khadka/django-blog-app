import algoliasearch_django as algoliasearch
from algoliasearch_django.decorators import register

from .models import BlogPost


@register(BlogPost)
class BlogPostIndex(algoliasearch.AlgoliaIndex):
    should_index = "published"
    fields = ["title", "content", "full_name"]
