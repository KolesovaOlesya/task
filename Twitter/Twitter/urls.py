"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Twitter.apps.blog.views import PostsViewSet
from Twitter.apps.users.serializers import UserResetPasswordSerializer
from Twitter.apps.users.views import CreateUserViewSet, UsersViewSet, apilogin, apilogout

router = routers.DefaultRouter()
router.register(r'register', CreateUserViewSet, base_name='register')
router.register(r'users', UsersViewSet, base_name='users')
router.register(r'posts', PostsViewSet, base_name='posts')
router.register(r'change_password', UserResetPasswordSerializer, base_name='change_password')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/login/$', apilogin),
    url(r'^api/logout/$', apilogout),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('Twitter.apps.blog.urls')),
]
