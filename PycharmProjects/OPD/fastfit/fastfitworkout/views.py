from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, DeleteView
from .forms import AddExerForm
from .forms import EnterNameForm
from .forms import AddExerToTrainForm
from django.urls import reverse_lazy
from .models import Exercise
from .models import ExerciseInTraining


@login_required
def exerc_manage(request):
    return render(request, 'edit_train.html', {})


class AddExercise(LoginRequiredMixin, FormView): # mb CreateView --> get_absolute_url() --> models.Exercise
    form_class = AddExerForm
    template_name = 'add_train.html'
    success_url = 'exercise_management'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ViewListExercises(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'TESTLIST.html'
    context_object_name = 'Exercises'


class DeletePreview(ViewListExercises): template_name = 'delete.html'


class RemoveExercise(LoginRequiredMixin, DeleteView):
    model = Exercise
    success_url = '/workout/delete.html' # mb to list
    context_object_name = 'exercise'
    template_name = 'fastfitworkout/exercise_confirm_delete.html'

    def form_valid(self, form):
        return super(RemoveExercise, self).form_valid(form)


class TestTrain(LoginRequiredMixin, FormView):
    form_class = AddExerForm
    template_name = 'add_train.html'
    success_url = 'exercise_management'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EnterNameTraining(LoginRequiredMixin, FormView):
    form_class = EnterNameForm
    template_name = 'name.html'
    success_url = '???'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddExerToTrain(LoginRequiredMixin, FormView, ListView):
    form_class = AddExerToTrainForm
    template_name = 'testtrain (2).html'
    success_url = ''
    #context_object_name = 'exercise'

    #def get_queryset(self):
     #   return Exercise.objects.all()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
