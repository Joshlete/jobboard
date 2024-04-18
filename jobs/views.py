from django.shortcuts import render

jobs = [
    {
        "id": 1,
        "title": "Python Developer",
        "description": "We are looking for a Python developer to join our team.",
        "salary": 100000,
    },
    {
        "id": 2,
        "title": "Java Developer",
        "description": "We are looking for a Java developer to join our team.",
        "salary": 100000,
    },
    {
        "id": 3,
        "title": "JavaScript Developer",
        "description": "We are looking for a JavaScript developer to join our team.",
        "salary": 100000,
    },
    {
        "id": 4,
        "title": "React Developer",
        "description": "We are looking for a React developer to join our team.",
        "salary": 100000,
    },
    {
        "id": 5,
        "title": "Django Developer",
        "description": "We are looking for a Django developer to join our team.",
        "salary": 100000,
    },
]


def index(request):
    context = {
        "jobs": jobs,
    }
    return render(request, "jobs/index.html", context)


def job(request, pk):
    job = None
    for j in jobs:
        if j["id"] == pk:
            job = j
            break
    context = {
        "job": job,
    }
    return render(request, "jobs/job.html", context)
