from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        help_text='Required. Enter a valid email address that will be used for account verification.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']