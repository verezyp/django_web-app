from .models import Exercise, Training, ExerciseInTraining


def get_spec_set(cur_uid:int):
    TRAINS = {}
    TrueSetTraining_Exercise = Training.objects.filter(uid=cur_uid).order_by('-id')
    for train_obj in TrueSetTraining_Exercise:
        cur = dict()
        sub_queryset = ExerciseInTraining.objects.filter(training_id=train_obj.id).order_by('training_id')
        exercise_dict = {}
        current_exercise_counter = 1
        for obj in sub_queryset:
            exercise_dict.update({f'Exercise{current_exercise_counter}' : {'id' : obj.id,  'name' : Exercise.objects.get(id=obj.exercise_id).exercise_name, 'params' : {'sets' : obj.sets, 'repetitions' : obj.repetitions, 'weight' : obj.weight,
                                                                                            'time' : obj.time }} })
            current_exercise_counter += 1
        cur.update({train_obj.id : {'name' : Training.objects.get(id=train_obj.id).name, 'exercises' : exercise_dict}})
        TRAINS.update(cur)
    return TRAINS