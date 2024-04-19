from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("job/<int:pk>", views.job, name="job"),
    path("create-job/", views.createJob, name="create-job"),
    path("update-job/<int:pk>", views.updateJob, name="update-job"),
    path("delete-job/<int:pk>", views.deleteJob, name="delete-job"),
    path("register-job/<int:pk>", views.jobApplication, name="register-job"),
    path("update-application/<int:pk>", views.editApplication, name="update-application"),
    path("profile/", views.profile, name="profile")
    
]
