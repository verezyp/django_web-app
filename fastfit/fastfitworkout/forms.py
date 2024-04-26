from django import forms
from .models import Exercise


class AddExerForm(forms.ModelForm):
    # exercise_name = forms.CharField(max_len=64)
    # muscle_group = forms.CharField(max_len=64)
    # technique_description = forms.CharField(max_len=256)
    class Meta:
        model = Exercise
        fields = '__all__'
        labels = {'exercise_name': 'Название', 'muscle_group': 'Группа мышц', 'technique_description': 'Описание'}
    # VALIDATION ?