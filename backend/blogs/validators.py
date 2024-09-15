from django.forms import ValidationError
from rest_framework.validators import UniqueValidator


# callable validator class
class ValidateEmailDomains:
    message = "Email must be from Gmail, Yahoo or Outlook."

    def __call__(self, value):
        """
        Validates if the given value is an email that ends with Gmail, Yahoo or Outlook domain.

        Args:
            value (str): The email to be validated.

        Raises:
            ValidationError: If the email does not end with Gmail, Yahoo or Outlook domain.
        """
        email_domains = ("@gmail.com", "@yahoo.com", "@outlook.com")
        if not value.endswith(email_domains):
            raise ValidationError(message=self.message)


class UniqueTitleValidator:
    def __init__(self, queryset, lookup="iexact"):
        self.queryset = queryset
        self.lookup = lookup

    def __call__(self, value):
        if self.queryset.filter(**{f"title__{self.lookup}": value}).exists():
            raise ValidationError("A blog with this title already exists.")


class ValidateImageFileExtension:
    def __call__(self, value):
        img_extensions = (".png", ".jpg", ".jpeg")
        if not value.name.endswith(img_extensions):
            raise ValidationError("Only PNG, JPG and JPEG images are allowed.")
