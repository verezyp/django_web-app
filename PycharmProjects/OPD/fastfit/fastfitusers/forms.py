from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegUserForm(UserCreationForm):
    username = forms.CharField(max_length = 16, label='Никнейм')
    password1 = forms.CharField(max_length = 32, label='Пароль')
    password2 = forms.CharField(max_length = 32, label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']