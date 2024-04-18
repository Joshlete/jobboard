from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("job/<int:pk>", views.job, name="job"),
    path("create-job/", views.createJob, name="create-job")
]
