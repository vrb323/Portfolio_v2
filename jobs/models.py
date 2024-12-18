from django.db import models

# Create your models here.
class Job(models.Model):
    images = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=700)
    job_description = models.CharField(max_length=1000, default="Default Job Description")

    def __str__(self):
        return self.summary
    
    
