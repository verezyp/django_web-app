from django.urls import path
from fastfitworkout import views

urlpatterns = [
    path('exercise_management', views.exerc_manage, name="exerc_manage"),
    path('add_exercise', views.AddExercise.as_view(), name="add_exercise"),
    path('TESTLIST.html', views.ViewListExercises.as_view(), name="TESTLIST"),
    path('delete.html', views.DeletePreview.as_view(), name="deleteprev"),
    path('remove/<int:pk>/', views.RemoveExercise.as_view(), name="remove"),
]