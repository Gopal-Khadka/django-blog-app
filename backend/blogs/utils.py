from uuid import uuid4
from urllib.parse import quote

def get_share_links(request,post):
    """
    Generate share links of the blog post for the social medias.
    
    Args:
        request: request object of view
        post: blog post object
    Returns:
        tuples of facebook, twitter, whatsapp and linkedin url.
    """
    
    encoded_title = quote(post.title)
    encoded_url = quote(post.get_full_url(request))
    
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}"
    twitter_url = f"https://twitter.com/intent/tweet?text={encoded_title}&url={encoded_url}"
    whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_title} {encoded_url}"
    linkedin_url = f"https://www.linkedin.com/shareArticle?mini=true&url={encoded_url}&title={encoded_title}"
    
    
    return facebook_url, twitter_url,whatsapp_url,linkedin_url


def upload_to(instance, filename):
    """
    Generate a unique filename by appending a uuid4 hex string to the filename.

    Args:
        instance: The model instance that the file is being uploaded for.
        filename: The original filename of the uploaded file.

    Returns:
        A string representing the new filename.
    """
    ext = filename.split(".")[-1]
    new_filename = f"{uuid4().hex}.{ext}"
    return f"media/blogs/{new_filename}"
