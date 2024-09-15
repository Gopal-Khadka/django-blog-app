from django.forms import ValidationError


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
