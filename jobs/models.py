from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  location = models.CharField(max_length=100)
  deadline = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  available = models.BooleanField(default=True)

  class Meta:
    ordering = ['-updated_at', '-created_at']

  def __str__(self):
    return self.title
  
class JobApplication(models.Model):
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.EmailField(null=True, blank=True)
  resume = models.TextField(null=True, blank=True)
  cover_letter = models.TextField(null=True, blank=True)  

  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    unique_together = ('job', 'user')
    
  def __str__(self):
    return f"{self.job.title} - {self.user.username}"