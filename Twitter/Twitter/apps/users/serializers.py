from rest_framework import serializers
from Twitter.apps.blog.serializers import PostSerializer
from Twitter.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_style': 'password'}, write_only=True)
    posts = PostSerializer(read_only=True, many=True)
    posts_count = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'posts', 'posts_count')


class UserResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='user.password', style={'input_type': 'password'})
    new_password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ("password", 'new_password')