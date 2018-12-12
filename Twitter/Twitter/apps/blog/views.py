from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Twitter.apps.blog.forms import PostForm
from Twitter.apps.blog.models import Post
from Twitter.apps.blog.serializers import PostSerializer
from Twitter.apps.users.models import User


class PostsListView(ListView):
    model = Post
    template_name = 'posts_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(author=self.request.user).order_by('-pub_date')
        else:
            return render(self.request, self.template_name, {})


class UsersPostsView(ListView):
    model = Post
    template_name = 'user_posts_list.html'

    def get_queryset(self):
        self.author = User.objects.get(id=self.kwargs['pk'])
        return Post.objects.filter(author=self.author).order_by('-pub_date')


class PostCreateView(CreateView):
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.pub_date = timezone.now()
        return super(PostCreateView, self).form_valid(form)


class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-pub_date')

