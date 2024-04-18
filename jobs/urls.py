from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("job/<int:pk>", views.job, name="job"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
]
