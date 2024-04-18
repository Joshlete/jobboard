from django.db import models

class Job(models.Model):
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