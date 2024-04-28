from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, DeleteView
from django.views.generic.edit import FormMixin
from .forms import AddExerForm, AddExerToTrainForm
from .forms import EnterNameForm
from .forms import AddExerToTrainForm, AE_Test_Form
from django.urls import reverse_lazy
from .models import Exercise, Training
from .models import ExerciseInTraining


@login_required
def exerc_manage(request):
    return render(request, 'edit_train.html', {})


class AddExercise(LoginRequiredMixin, FormView):
    form_class = AddExerForm
    template_name = 'add_train.html'
    success_url = 'exercise_management'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uid'] = 505 #self.request.user.id
        return context

    def form_valid(self, form, **kwargs):
        form.instance.uid = self.request.user.id
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        print("Form is invalid. Form data:")
        for field in form.fields:
            print(f"{field}: {form.cleaned_data.get(field)}")
        return super().form_invalid(form)


class ViewListExercises(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'TESTLIST.html'
    context_object_name = 'Exercises'
    def get_queryset(self):
        return Exercise.objects.filter(uid=self.request.user.id)


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
        # exercise.uid = current.user.id
        form.save()
        return super().form_valid(form)


class EnterNameTraining(LoginRequiredMixin, CreateView):
    model = Training
    fields = ['name']
    template_name = 'name.html'

    def get_success_url(self): # for dynamic db reloading of obj
        last_training_pk = Training.objects.order_by('pk').last().pk
        # training.uid = current.user.id
        return f'add_exr_to_train/{last_training_pk}/' # reverse_lazy ?



#!!! add param 'user'/'user_id' to exerc db, exerc-training db --> show user's exercises and training (shows all rn)



class AddExerToTrain(LoginRequiredMixin, FormView):

    template_name = 'testtrain (2).html'
    form_class = AddExerToTrainForm

    def get_success_url(self):
        return self.request.get_full_path()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Exercises'] = Exercise.objects.all() # uid = current.user.id
        context['Training'] = Training.objects.get(pk=self.kwargs['pk']) # if traning.uid = current.user.id
        return context

    def form_valid(self, form):
         form.save()
         return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid. Form data:")
        for field in form.fields:
            print(f"{field}: {form.cleaned_data.get(field)}")
        return super().form_invalid(form)

# to do

# class TrainListView(ListView):
#     template_name = 'TRAINLISTTEST.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Exercises'] = ExerciseInTraining.objects.all()
#         context['Trainings'] = Training.objects.all()
#         return context