from uuid import uuid4


def upload_to(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"{uuid4().hex}.{ext}"
    return f"media/blogs/{new_filename}"
