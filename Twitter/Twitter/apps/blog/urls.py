from django.conf.urls import url
from django.urls import include
from . import views
from Twitter.apps.users import views as view

urlpatterns = [
    url(r'^create/$', views.PostCreateView.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UsersPostsView.as_view()),
    url(r'^users/$', view.UsersListView.as_view()),
    url(r'^user', include('Twitter.apps.users.urls')),
    url(r'^', views.PostsListView.as_view()),
]
