from django.db import models

# Create your models here.

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=)