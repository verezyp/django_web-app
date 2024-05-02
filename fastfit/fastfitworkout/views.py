from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from .forms import AddExerForm, AddExerToTrainForm
from .forms import AddExerToTrainForm
from .models import Exercise, Training
from .models import ExerciseInTraining
from django.shortcuts import get_object_or_404
from . import utilscustom


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


from django.db.models import Q

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

    def get_object(self, **kwargs):
        return get_object_or_404(Exercise, uid=self.request.user.id, id=self.kwargs['pk'])

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


class TrainListView(LoginRequiredMixin, TemplateView):
    template_name = 'TRAINLISTTEST.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TRAINS'] = utilscustom.get_spec_set_exrc(self.request.user.id)
        return context


class ClearTrainListView(TrainListView): template_name = 'CLEARLISTTRAIN.html'


class RemoveTrain(LoginRequiredMixin, DeleteView):
    model = Training
    success_url = '/workout/TRAINLISTTEST.html'
    template_name = 'fastfitworkout/exercise_confirm_delete.html'

    def get_object(self, **kwargs):
        return get_object_or_404(Training, uid=self.request.user.id, id=self.kwargs['pk'])


class RemoveExerciseFromTrain(LoginRequiredMixin, DeleteView):
    model = ExerciseInTraining
    success_url = '/workout/TRAINLISTTEST.html'
    template_name = 'fastfitworkout/exercise_confirm_delete.html'

    def get_object(self, **kwargs):
        return get_object_or_404(ExerciseInTraining, uid=self.request.user.id, id=self.kwargs['exrc_id'])


class UpdateExerciseInTraining(LoginRequiredMixin, UpdateView):
    model = ExerciseInTraining
    fields = ['sets', 'repetitions', 'weight', 'time']
    template_name = 'UPDATETEST.html'
    success_url = '/workout/TRAINLISTTEST.html'

    def get_object(self, **kwargs):
        return get_object_or_404(ExerciseInTraining, uid=self.request.user.id,
                                 id=self.kwargs['exrc_id'], training_id=self.kwargs['train_id'])
