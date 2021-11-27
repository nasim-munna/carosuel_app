from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
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

class Service(models.Model):
    name = models.CharField(max_length=30)
    short_description= models.TextField()
    image = models.ImageField(upload_to='service/')

    def __str__(self):
        return self.name

class Partner(models.Model):

    image = models.ImageField(upload_to='partner/')
    hover_image = models.ImageField(upload_to='partner/')

class Award(models.Model):
    name = models.CharField(max_length=30)
    short_description= models.TextField()
    image = models.ImageField(upload_to='award/')

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    department =models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name


STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug =models.SlugField(max_length=200,unique=True)
    author =models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)
    image = models.ImageField(upload_to='blog/',blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title