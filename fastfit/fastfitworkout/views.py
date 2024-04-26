from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, DeleteView
from .forms import AddExerForm
from django.urls import reverse_lazy
from .models import Exercise

@login_required
def exerc_manage(request):
    return render(request, 'edit_train.html', {})


class AddExercise(FormView): # mb CreateView --> get_absolute_url() --> models.Exercise
    form_class = AddExerForm
    template_name = 'add_train.html'
    success_url = 'exercise_management'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ViewListExercises(ListView):
    model = Exercise
    template_name = 'TESTLIST.html'
    context_object_name = 'Exercises'


class DeletePreview(ViewListExercises): template_name = 'delete.html'


class RemoveExercise(DeleteView): # unused
    model = Exercise
    success_url = '/workout/exercise_management' # to list
    context_object_name = 'exercise'
    template_name = 'fastfitworkout/exercise_confirm_delete.html'

    def form_valid(self, form):
        return super(RemoveExercise, self).form_valid(form)

