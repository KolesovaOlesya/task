from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.views.generic.base import View
from django.views.generic.list import ListView
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.utils import json
from Twitter.apps.blog.models import Post
from Twitter.apps.blog.serializers import PostSerializer
from Twitter.apps.users.forms import RegisterForm
from Twitter.apps.users.models import User
from Twitter.apps.users.serializers import UserSerializer, UserResetPasswordSerializer


class UsersListView(ListView):
    model = User
    template_name = 'users_list.html'


class RegisterFormView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/users/login/"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


@permission_classes((AllowAny,))
class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(http_method_names=['POST'])
@permission_classes((AllowAny,))
def apilogin(request):
    username = (json.loads(request.body.decode('utf-8')))['username']
    password = (json.loads(request.body.decode('utf-8')))['password']
    user = authenticate(request, username=username, password=password)
    login(request._request, user)
    return Response()


@api_view(http_method_names=['GET'])
@permission_classes((AllowAny,))
def apilogout(request):
    logout(request)
    return Response()


class UsersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.prefetch_related('posts').all()
    serializer_class = UserSerializer

    @action(methods=['GET'], detail=True)
    def get_posts(self, request, pk):
        self.author = User.objects.get(id=self.kwargs['pk'])
        queryset = Post.objects.filter(author=self.author)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return super().get_queryset().annotate(posts_count=Count('posts', distinct=True))

    @action(detail=False, permission_classes=[IsAuthenticated], methods=['post'], serializer_class=UserResetPasswordSerializer)
    def reset_user_password(self, request):
        reset_password_serializer = UserResetPasswordSerializer(request.user, data=request.data)
        if reset_password_serializer.is_valid():
            if not request.user.check_password(request.data.get('password')):
                return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            request.user.set_password(request.data.get('new_password'))
            request.user.save()
            return Response({"Message": ["Password reset successfully"]}, status=status.HTTP_200_OK)
