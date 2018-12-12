from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase

from Twitter.apps.blog.models import Post


class TestUsersViewSet(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='ook')
        self.post1 = Post.objects.create(author=self.user1, message='jjjjjg', pub_date='2018-11-25 01:10:45.13588+07')
        self.post2 = Post.objects.create(author=self.user1, message='dddddd', pub_date='2018-11-25 01:10:45.13588+07')

    def test_get_posts(self):
        url = reverse('users-get-posts', kwargs={'pk': self.user1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(url, '/api/users/1/get_posts/')

