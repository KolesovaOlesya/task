from django.forms import ModelForm
from Twitter.apps.blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
