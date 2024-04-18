from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Job


def index(request):
    jobs = Job.objects.all()
    context = {
        "jobs": jobs,
    }
    return render(request, "jobs/index.html", context)


def job(request, pk):
    job = Job.objects.get(id=pk)
    context = {
        "job": job,
    }
    return render(request, "jobs/job.html", context)
