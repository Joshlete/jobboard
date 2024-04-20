from django import forms
from django.forms import ModelForm
from .models import Job
from django.forms import ModelForm
from .models import Job, JobApplication


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "company",
            "description",
            "location",
            "deadline",
        ]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }


class ApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = ["email", "resume", "cover_letter"]
        widgets = {
            "resume": forms.Textarea(attrs={"rows": 4}),
            "cover_letter": forms.Textarea(attrs={"rows": 4}),
            
        }
