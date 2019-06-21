from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

