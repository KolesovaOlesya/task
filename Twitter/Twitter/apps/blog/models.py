from django.db import models
from Twitter.apps.users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    message = models.TextField(max_length=140)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.message
