from django.urls import path
from fastfitweb import views


urlpatterns = [
    path('', views.pilot, name="pilot"),
    path('main', views.main, name="main"),
]