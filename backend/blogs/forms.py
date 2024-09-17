from django import forms
from tinymce.widgets import TinyMCE

from blogs.models import Contact, BlogPost, BlogAuthor
from blogs.validators import ValidateEmailDomains


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].validators.append(
            ValidateEmailDomains()
        )  # validate emails

    def clean_name(self):
        """
        Validate the name field from the ContactForm.

        This method is automatically called by Django when validating the form.
        It raises a ValidationError if the name is too short (less than 10 characters).
        """

        name = self.cleaned_data.get("name")
        if len(str(name)) < 10:
            raise forms.ValidationError("Name is too short.")
        if str(name).startswith("admin"):
            raise forms.ValidationError("Name cannot start with 'admin'.")
        return name


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = [
            "title",
            "author",
            "content"
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["author"].initial = self.user.author
        self.fields["author"].widget.attrs["readonly"] = True
