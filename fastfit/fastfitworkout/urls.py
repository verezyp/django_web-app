from django.urls import path
from fastfitworkout import views

urlpatterns = [
    path('exercise_management', views.exerc_manage, name="exerc_manage"),
    path('add_exercise', views.AddExercise.as_view(), name="add_exercise"),
    path('TESTLIST.html', views.ViewListExercises.as_view(), name="TESTLIST"),
    path('delete.html', views.DeletePreview.as_view(), name="deleteprev"),
    path('remove/<int:pk>/', views.RemoveExercise.as_view(), name="remove"),
    path('name', views.EnterNameTraining.as_view(), name="name"),
    path('add_exr_to_train/<int:pk>/', views.AddExerToTrain.as_view(), name="add_exr"),
    path('TRAINLISTTEST.html', views.TrainListView.as_view(), name="TRAINLISTTEST"),
    path('CLEARLISTTRAIN.html', views.ClearTrainListView.as_view(), name="CLEARLISTTRAIN"),
    path('removetrain/<int:pk>/', views.RemoveTrain.as_view(), name="removetrain"),
    path('removeexercisetrain/<int:exrc_id>/', views.RemoveExerciseFromTrain.as_view(), name="removeexrctrain"),
    path('updateexercise/<int:train_id>/<int:exrc_id>/', views.UpdateExerciseInTraining.as_view(), name="updateexercise"),

]