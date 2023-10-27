from django.forms import ModelForm, ImageField
from .models import Blog, Profile


class BlogForm(ModelForm):
    image = ImageField(required=False)

    class Meta:
        model = Blog
        # fields = "__all__"
        exclude = ('user',)
