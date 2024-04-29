from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
from django.shortcuts import get_object_or_404


# TRAININGS = {Train1 : { {name : NAME},  {EXRCS : {exrc1 : {name, sets, reps, weight, time} , exrc2 : {...}, ..}}}, Train2 : {...} ...}


'''
1) select from exrcintr uid=cur.uid

cycle :
    2) add to train1 train1 : name (name =  select name from training where training.id = ExrcInTrain.training_id )
    cycle:
        3) add to train1 EXRCS : name =  select name from exercise where exercise.id = ExrcInTrain.exercise_id, sets = ... ...
'''


def get_spec_set(cur_uid:int):
    TRAINS = {}
    #ted = {'trainings' : {{'nametrain' : '*name*', 'exercises' : {{'nameexrc' : '*name*', 'sets' : '*sets*', 'reps' : 'ree'}}}}}
    TrueSetTraining_Exercise = ExerciseInTraining.objects.filter(uid=cur_uid).order_by('training_id')
    was = set()
    ck = 0
    for train_obj in TrueSetTraining_Exercise:
        ck += 1
        #if train_obj.training_id not in was:
        was.add(train_obj.training_id)
        cur = dict()
        subdict = ExerciseInTraining.objects.filter(training_id=train_obj.training_id).order_by('training_id')
        # print(Training.objects.get(id=train_obj.training_id).name)
        # TRAINS['trainings'].update({'name' : Training.objects.get(id=train_obj.training_id).name})
        names = {}
        counter = 1
        for obj in subdict:
            names.update({f'Exercise{counter}' : {'name' : Exercise.objects.get(id=obj.exercise_id).exercise_name, 'params' : {'sets' : obj.sets, 'repetitions' : obj.repetitions, 'weight' : obj.weight,
                                                                                            'time' : obj.time }} })
            counter += 1
            #print(names)

        cur.update({train_obj.training_id :{'name' : Training.objects.get(id=train_obj.training_id).name, 'exercises' : names}})
        #cur.update({'name' : Training.objects.get(id=train_obj.training_id).name, 'exercises' : Exercise.objects.filter(id=subdict.exercise_id).exercise_name})
        #print(cur)
        TRAINS.update(cur)

        cur_exrc = dict()
    return TRAINS
    print(TRAINS)