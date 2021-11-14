from django.db import models
from django.db.models.base import Model

# Create your models here.
class Expert(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='expert/')
    facebook_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    short_description= models.TextField()
    image = models.ImageField(upload_to='project/')
    project_url= models.URLField(null=True)
    

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    short_description= models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name



    