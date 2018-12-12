from django import forms
from django.contrib.auth.forms import UserCreationForm
from Twitter.apps.users.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
