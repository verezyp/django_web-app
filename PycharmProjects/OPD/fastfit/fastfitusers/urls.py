from django.urls import path
from fastfitusers import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.LoginUser.as_view(), name="login"),
    path('register', views.RegUser.as_view(), name="register"),
    path('logout', LogoutView.as_view(), name="logout"),
]