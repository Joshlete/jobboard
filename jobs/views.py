from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def createJob(request):
    if request.method == "POST":
        title = request.POST.get("title")
        company = request.POST.get("company")
        description = request.POST.get("description")
        location = request.POST.get("location")
        deadline = request.POST.get("deadline")
        job = Job(
            title=title,
            description=description,
            company=company,
            location=location,
            deadline=deadline,
        )
        job.save()
        return redirect("index")
    context = {}
    return render(request, "jobs/job-form.html", context)
