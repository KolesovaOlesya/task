from django.utils import timezone
from rest_framework import serializers
from Twitter.apps.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'message', 'pub_date')
        extra_kwargs = {'pub_date': {'read_only': True}, 'author': {'read_only': True}}

