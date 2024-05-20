from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import RegUserForm
from fastfitworkout.models import Exercise
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth.html'

    def get_success_url(self):
        return reverse_lazy('fastfitweb:main')


class RegUser(CreateView):
    form_class = RegUserForm
    template_name = 'reg.html'
    success_url = reverse_lazy('fastfitusers:login')


@receiver(post_save, sender=User)
def default_exercises_uploading(sender, instance, created, **kwargs):
    if created:
        user_id = instance.id
        defaults = []
        with open('fastfitusers\defaultsetexercises.txt', 'r',
                  encoding='utf-8') as default_file:
            content = default_file.read().split(':|')
            while content:
                try:
                    defaults.append(Exercise(exercise_name=content.pop(0), muscle_group=content.pop(0),
                                             technique_description=content.pop(0), uid=user_id))
                except IndexError:
                    break
        Exercise.objects.bulk_create(defaults)
