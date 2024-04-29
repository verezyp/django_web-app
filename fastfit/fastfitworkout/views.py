from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, DeleteView
from django.views.generic.edit import FormMixin

from . import utilscustom
from .forms import AddExerForm, AddExerToTrainForm
from .forms import EnterNameForm
from .forms import AddExerToTrainForm, AE_Test_Form
from django.urls import reverse_lazy
from .models import Exercise, Training
from .models import ExerciseInTraining
from django.shortcuts import get_object_or_404



@login_required
def exerc_manage(request):
    return render(request, 'edit_train.html', {})


class AddExercise(LoginRequiredMixin, FormView):
    form_class = AddExerForm
    template_name = 'add_train.html'
    success_url = 'exercise_management'

    def form_valid(self, form, **kwargs):
        form.instance.uid = self.request.user.id
        form.save()
        return super().form_valid(form)


class ViewListExercises(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'TESTLIST.html'
    context_object_name = 'Exercises'

    def get_queryset(self):
        return Exercise.objects.filter(uid=self.request.user.id)


class DeletePreview(ViewListExercises): template_name = 'delete.html'


class RemoveExercise(LoginRequiredMixin, DeleteView):
    model = Exercise
    success_url = '/workout/delete.html'  # mb to list
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

    def form_valid(self, form):
        form.instance.uid = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):  # for dynamic db reloading of obj
        last_training_pk = Training.objects.order_by('pk').last().pk
        # training.uid = current.user.id
        return f'add_exr_to_train/{last_training_pk}/'  # reverse_lazy ?


# !!! add param 'user'/'user_id' to exerc db, exerc-training db --> show user's exercises and training (shows all rn)
# dict({'trainings' : {{'nametrain' : '*name*', 'exercises' : {{'nameexrc' : '*name*', 'sets' : '*sets*', 'reps' : trps ...}}}}})


class AddExerToTrain(LoginRequiredMixin, FormView):  # mb remove uid from form ---> form_valid: uid = ...

    template_name = 'testtrain (2).html'
    form_class = AddExerToTrainForm

    def get_success_url(self):
        return self.request.get_full_path()

    def get_context_data(self, **kwargs):  # VALIDATION train.pk belong uid
        context = super().get_context_data(**kwargs)

        context['Exercises'] = Exercise.objects.filter(uid=self.request.user.id)  # uid = current.user.id
        # context['Training'] = Training.objects.get(pk=self.kwargs['pk']) # if traning.uid = current.user.id
        context['Training'] = get_object_or_404(Training, pk=self.kwargs['pk'], uid=self.request.user.id)  # not sure;
        context['uid'] = 505  # self.request.user.id
        return context

    def form_valid(self, form):
        form.instance.uid = self.request.user.id
        form.save()  #

        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid. Form data:")
        for field in form.fields:
            print(f"{field}: {form.cleaned_data.get(field)}")
        return super().form_invalid(form)

# to do
'''

mb make a set() -> {Train1 : {exrc1 , exrc2, ..}, Train2 : {...} ...} # any train.uid == cur.uid and 

Training name 1 : {}
    exrc 1.1 name sets reps weight time
    exrc 1.2 name sets reps weight time
    ...
    
Training name 2 :
    exrc 2.1 name sets reps weight time
    exrc 2.2 name sets reps weight time
    ...
...

'''

# to remove train --> add train.id in train params in dict
class TrainListView(LoginRequiredMixin, TemplateView):
    template_name = 'TRAINLISTTEST.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TRAINS']= utilscustom.get_spec_set(self.request.user.id)
        return context
