from django.forms import ModelForm, ImageField,FileInput
from .models import Blog, Profile


class BlogForm(ModelForm):
    image = ImageField(required=False)

    class Meta:
        model = Blog
        # fields = "__all__"
        exclude = ('user', 'likes')
