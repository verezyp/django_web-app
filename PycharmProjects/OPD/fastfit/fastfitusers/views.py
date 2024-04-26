from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import RegUserForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth.html'

    def get_success_url(self):
        return reverse_lazy('fastfitweb:main')


class RegUser(CreateView):
    form_class = RegUserForm
    template_name = 'reg.html'
    success_url = reverse_lazy('fastfitusers:login')
