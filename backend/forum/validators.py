from rest_framework.validators import ValidationError


class UniqueAttrValidator:
    def __init__(self, queryset, model, attr, lookup="iexact"):
        self.queryset = queryset
        self.lookup = lookup
        self.model = model
        self.attr = attr

    def __call__(self, value):
        """
        Checks if the given `value` already exists in the database.

        Args:
            value (str): The value to check.

        Raises:
            ValidationError: If the value already exists in the database.
        """

        if self.queryset.filter(**{f"{self.attr}__{self.lookup}": value}).exists():
            raise ValidationError(f"A {self.model} with this {self.attr} already exists.")
