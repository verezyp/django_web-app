from django import forms
from .models import Exercise
from .models import Training
from .models import ExerciseInTraining


class AddExerForm(forms.ModelForm):
    # exercise_name = forms.CharField(max_len=64)
    # muscle_group = forms.CharField(max_len=64)
    # technique_description = forms.CharField(max_len=256)
    class Meta:
        model = Exercise
        fields = '__all__'
        labels = {'exercise_name': 'Название', 'muscle_group': 'Группа мышц', 'technique_description': 'Описание'}
    # VALIDATION ?


class AddExer2TrainForm(forms.Form):
    name = forms.ModelChoiceField(label='Название', widget=forms.Select, queryset=Exercise.objects.all())
    series = forms.IntegerField(label='Количество подходов')
    rep_per_series = forms.IntegerField(label='Количество повторений')
    specific_param = forms.IntegerField(label='Вес(кг) / Дистанция (км) / -')


class EnterNameForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name']


class AE_Test_Form(forms.Form):
    sets = forms.IntegerField()
    repetitions = forms.IntegerField()
    weight = forms.IntegerField()


class AddExerToTrainForm(forms.ModelForm):
    class Meta:
        model = ExerciseInTraining
        fields = '__all__'