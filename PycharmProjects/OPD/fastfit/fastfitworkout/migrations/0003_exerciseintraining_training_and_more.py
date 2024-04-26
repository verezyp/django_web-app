# Generated by Django 5.0.4 on 2024-04-26 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfitworkout', '0002_alter_exercise_technique_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseInTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=64)),
                ('sets', models.PositiveIntegerField()),
                ('repetitions', models.PositiveIntegerField()),
                ('weight', models.FloatField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastfitworkout.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('exercises', models.ManyToManyField(through='fastfitworkout.ExerciseInTraining', to='fastfitworkout.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exerciseintraining',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastfitworkout.training'),
        ),
    ]
