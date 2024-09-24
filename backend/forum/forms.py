from django import forms
from .models import Post


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop("id")
        super().__init__(*args, **kwargs)
        self.fields["content"].initial = Post.objects.filter(id=self.id).first().content
