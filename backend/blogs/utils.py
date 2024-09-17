from uuid import uuid4


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
