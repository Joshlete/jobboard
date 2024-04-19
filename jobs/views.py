from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import JobForm, ApplicationForm
from django.contrib import messages


def index(request):
    jobs = Job.objects.all()
    context = {
        "jobs": jobs,
    }
    return render(request, "index.html", context)


def profile(request):
    # get all jobs created by the user
    jobs = Job.objects.filter(user=request.user)
    applications = JobApplication.objects.filter(user=request.user)

    context = {
        "jobs": jobs,
        "applications": applications,
    }
    return render(request, "profile.html", context)


def job(request, pk):
    job = Job.objects.get(id=pk)

    # check if user has applied to the job
    has_applied = JobApplication.objects.filter(job=job, user=request.user).exists()

    context = {
        "job": job,
        "has_applied": has_applied,
    }
    return render(request, "jobs/job.html", context)


@login_required(login_url="login")
def createJob(request):
    form = JobForm()
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {"form": form}
    return render(request, "jobs/job-form.html", context)


@login_required(login_url="login")
def updateJob(request, pk):
    # check if user is the owner of the job
    job = Job.objects.get(id=pk)
    if job.user != request.user:
        return redirect("index")

    form = JobForm(instance=job)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {"form": form}
    return render(request, "jobs/job-form.html", context)


@login_required(login_url="login")
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    if job.user != request.user:
        return redirect("index")

    if request.method == "POST":
        job.delete()
        return redirect("index")
    return render(request, "jobs/delete.html", {"job": job})


@login_required(login_url="login")
def jobApplication(request, pk):
    job = Job.objects.get(id=pk)
    if JobApplication.objects.filter(job=job, user=request.user).exists():
        return redirect("index")  # User has already applied

    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.job = job
            job_application.user = request.user
            job_application.save()
            return redirect("index")
    context = {"form": form}
    return render(request, "applications/application-form.html", context)


@login_required(login_url="login")
def editApplication(request, pk):
    application = JobApplication.objects.get(id=pk)
    if application.user != request.user:
        return redirect("index")

    form = ApplicationForm(instance=application)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("profile")
    context = {"form": form}
    return render(request, "applications/application-form.html", context)
