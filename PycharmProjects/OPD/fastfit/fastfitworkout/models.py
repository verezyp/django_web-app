from django.db import models


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=64)
    muscle_group = models.CharField(max_length=64)
    technique_description = models.CharField(max_length=512)

    def __str__(self):
        return self.exercise_name


class Training(models.Model):
    name = models.CharField(max_length=64)
    exercises = models.ManyToManyField(Exercise, through='ExerciseInTraining')

    def __str__(self):
        return self.name


class ExerciseInTraining(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    time = models.CharField(max_length=64)
    sets = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight = models.FloatField()

    def __str__(self):
        return
