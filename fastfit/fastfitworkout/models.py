from django.db import models

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=64)
    muscle_group = models.CharField(max_length=64)
    technique_description = models.CharField(max_length=512)

    def __str__(self):
        return self.exercise_name