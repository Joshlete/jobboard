from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm



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

@login_required(login_url='login')
def createJob(request):
    form = JobForm()
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {'form': form}
    return render(request, "jobs/job-form.html", context)

@login_required(login_url='login')
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
    context = {'form': form}
    return render(request, "jobs/job-form.html", context)

@login_required(login_url='login')
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    if job.user != request.user:
        return redirect("index")
    
    if request.method == "POST":
        job.delete()
        return redirect("index")        
    return render(request, "jobs/delete.html", {"job": job})

@login_required(login_url='login')
def registerJob(request, pk):
    job = Job.objects.get(id=pk)
    if job.user != request.user:
        return redirect("index")
    
    job.registered_users.add(request.user)
    return redirect("index")
