import algoliasearch_django as algoliasearch
from algoliasearch_django.decorators import register

from .models import BlogPost


@register(BlogPost)
class BlogPostIndex(algoliasearch.AlgoliaIndex):
    should_index = "public"
    fields = ["title", "content", "full_name", "published"]

    tags = "get_tags_list"
    settings = {
        "searchableAttributes": [
            "title",
            "content",
            "full_name",
        ],  # attributes to be searched for query
        "attributesForFaceting": [
            "published",
            # "public",
        ],  # attributes to be used for faceting(filtering)
    }
